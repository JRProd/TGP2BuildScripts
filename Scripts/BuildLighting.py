import subprocess
import os

from P4 import P4, P4Exception

from . import Environment as env

game_name = env.get_env_variable('Game','game_name')

def build_lighting():
    print( '----------------------------------------------------------------------------------------------------' )
    print( '{} - Step 3: Starting Lighting Build'.format( game_name ) )
    print( '----------------------------------------------------------------------------------------------------' )

    maps = []

    # Compile the list of maps
    map_dir = env.get_env_variable('Game', 'map_dir')
    map_names = env.get_env_variable('Game', 'maps').split(';')

    for map in map_names:
        full_path_map = map_dir + map
        maps.append( full_path_map + '.umap')

        maps.append( full_path_map + '_BuiltData.uasset')


     # Check the file out from P4
    p4 = P4()
    p4.user = env.get_env_variable('Perforce', 'user_name')
    p4.password = env.get_env_variable('Perforce', 'user_password')
    p4.client = env.get_env_variable('Perforce', 'client')

    try:
        p4.connect()

        # Checkout requested maps
        for map in maps:
            try:
                p4.run('edit', map)
            except:
                pass
        
        # Build the lighting
        uproject_file = env.get_env_variable( "Game", "uproject_file" )
        ue4_binaries_dir = env.get_env_variable( 'Local', "ue4_binaries_dir" )
        print(subprocess.run( [ ue4_binaries_dir + 'UE4Editor-Cmd.exe', uproject_file, '-verbose', "-p4", "-submit", "-run=resavepackages" , "-buildlighting", "-quality=production", "-allowcommandletrendering", "-map" + ' '.join(maps)] ) )

        # Add maps back for addition to p4
        for map in maps:
            print("adding " + map)
            p4.run('add', map)

        change = p4.fetch_change()
        change._description = '[Daily_Builds] Built lighting for the follow maps:\n' + '\n\t'.join(maps)
        p4.run_submit( change ) 

        return True
    except P4Exception:
        print('ERROR: Error capture in P4')
        for e in p4.errors:
            print(e)

        return False
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    build_lighting()
