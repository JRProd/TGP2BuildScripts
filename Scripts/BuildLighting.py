import subprocess
import os
import glob

from P4 import P4, P4Exception

from . import Environment as env

game_name = env.get_env_variable('Game','game_name')

def build_lighting( log_file ):
    log_file.write( '----------------------------------------------------------------------------------------------------\n' )
    log_file.write( '{} - Step 3: Starting Lighting Build\n'.format( game_name ) )
    log_file.write( '----------------------------------------------------------------------------------------------------\n' )


    # Compile the list of maps
    map_dir = env.get_env_variable('Game', 'map_dir')
    map_names = env.get_env_variable('Game', 'maps').split(' ')
    perforce_map_files = []

    log_file.write('Building lighting for these maps: ')
    for map in map_names:
        log_file.write(map + " ")

        # Find all maps, and submaps that match <dir>\**\<map>*.umap
        found_maps = glob.glob(map_dir + '\**\\' + map + '*.umap', recursive=True)
        
        # For all the found maps create a mapping to the build data
        for found_map in found_maps:
            perforce_map_files.append( found_map)
            perforce_map_files.append( found_map[0:found_map.index('.')] + '_BuiltData.uasset' )

    log_file.write( '\n' )
    log_file.write('Found a total of {} maps to build lighting on\n'.format( (int)(len(perforce_map_files) / 2)))
    log_file.flush()

     # Check the file out from P4
    p4 = P4()
    p4.user = env.get_env_variable('Perforce', 'user_name')
    p4.password = env.get_env_variable('Perforce', 'user_password')
    p4.client = env.get_env_variable('Perforce', 'client')

    try:
        p4.connect()

        # Checkout requested maps
        for map in perforce_map_files:
            try:
                p4.run('edit', map)
            except:
                log_file.write('Failed to open map {}\n'.format(map))
                log_file.flush()
        
        # Build the lighting
        uproject_file = env.get_env_variable( "Game", "uproject_file" )
        ue4_binaries_dir = env.get_env_variable( 'Local', "ue4_binaries_dir" )
        subprocess.run( [ ue4_binaries_dir + 'UE4Editor-Cmd.exe', uproject_file, "-p4", "-submit", "-run=resavepackages" , "-buildlighting", "-quality=Production", "-AllowCommandletRendering", "-map" + ' '.join(map_names)], stdout=log_file )
        log_file.flush()

        # Add maps back for addition to p4
        for map in perforce_map_files:
            log_file.write("adding " + map + '\n')
            p4.run('add', map)
        log_file.flush()

        change = p4.fetch_change()
        change._description = '[Daily_Builds] Built lighting for the follow maps:\n' + '\n\t'.join(perforce_map_files)
        p4.run_submit( change ) 

        log_file.write('Lighting successfully built and submitted\n')
        log_file.flush()

        return True
    except P4Exception:
        log_file.write('Perforce error encountered')
        for e in p4.errors:
            log_file.write( str(e) )

        log_file.flush()

        return False
    except Exception as e:
        log_file.write( str(e) )
        log_file.flush()
        return False
