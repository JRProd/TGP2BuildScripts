import os

from shutil import copy

from P4 import P4, P4Exception

from . import Environment as env

game_name = env.get_env_variable('Game','game_name')

def update_version_number( log_file, major, minor ):
    log_file.write( '----------------------------------------------------------------------------------------------------\n' )
    log_file.write( '{} - Step 2: Update the version number\n'.format( game_name ) )
    log_file.write( '----------------------------------------------------------------------------------------------------\n' )

    # Determine if automatic versioning is used by the config file
    try:
        automatic_versioning = env.get_env_variable('Version', 'automatic')
    
    # If no versioning disinction continue
    except Exception as e:
        log_file.write('Automatic versioning system skipped because no [Version] automatic value found\n')
        return True

    if 'False' in automatic_versioning:
        log_file.write('Automatic versioning system is disabled\n')
        return True
    elif not 'True' in automatic_versioning:
        log_file.write("Unknown value {} in [Version] automatic. Expected 'True'/'False' values\n".format(automatic_versioning) )
        return False
    log_file.flush()

    version_number = ''

    # Open ini file
    version_ini = env.get_env_variable('Version', 'version_ini')
    version_header = env.get_env_variable('Version', 'version_header')
    version_tag = env.get_env_variable('Version', 'version_tag')
    with open( env.get_env_variable('Version', 'version_ini'), 'r') as file:
        file_list = file.read().split('\n')

    # Parse ini file for specific header
    after_header = False
    found_version = False
    for line_item in file_list:
        if line_item == version_header:
            after_header = True
            
        if line_item == '':
            after_header = False

        if after_header and version_tag in line_item:
            version_item = line_item.split('=')
            version_number = version_item[1]
            found_version = True
        
    if not found_version:
        log_file.write('Failed to find version number\n')
        return False

    # Update the version number
    new_version = get_version_number(major, minor, version_number)
    log_file.write('Version number updated to {}\n'.format(new_version))
    log_file.flush()

    # Check the file out from P4
    p4 = P4()
    p4.user = env.get_env_variable('Perforce', 'user_name')
    p4.password = env.get_env_variable('Perforce', 'user_password')
    p4.client = env.get_env_variable('Perforce', 'client')

    try:
        p4.connect()

        p4.run( 'edit', version_ini )

        # Open temporary file for writing
        with open( version_ini + '.tmp', 'w' ) as out_file:
            with open( version_ini, 'r') as in_file:
                for line in in_file:
                    if version_number in line:
                        # Replace version with new version
                        out_file.write(version_tag + '=' + new_version)
                    else:
                        out_file.write(line)

        # Replace old file with new file
        copy(version_ini + '.tmp', version_ini)
        os.remove( version_ini + '.tmp')

        change = p4.fetch_change()
        change._description = '[Daily_Builds] Updated the version number to ' + new_version
        # p4.run_submit( change )

        log_file.write('New version number successfully submitted to perforce\n')
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

def get_version_number(major, minor, version):
    split_version = version.split('.')
    if major:
        split_version[0] = str(int(split_version[0]) + 1)
        split_version[1] = '0'
        split_version[2] = '0'
        return '.'.join(split_version)

    if minor:
        split_version[1] = str(int(split_version[1]) + 1)
        split_version[2] = '0'
        return '.'.join(split_version)

    # If not major or minor, must be hotfix
    split_version[2] = str(int(split_version[2]) + 1)
    return '.'.join(split_version)
 