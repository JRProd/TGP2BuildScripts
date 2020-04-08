import datetime

from P4 import P4

import Environment as env

game_name = env.get_env_variable('Game','game_name')

def update_version_number():
    print( '----------------------------------------------------------------------------------------------------' )
    print( '{} - Step 1: Update the version number'.format( game_name ) )
    print( '----------------------------------------------------------------------------------------------------' )

    # Create the version file
    date_value = str(datetime.datetime.now().date()).replace('-', '')
    version_file_path ='Project_Files/HaberDashers/Content/Versioning/' + date_value + '.txt'

    # Perforce Settings
    p4 = P4()
    p4.user = env.get_env_variable('Perforce', 'user_name')
    p4.password = env.get_env_variable('Perforce', 'user_password')
    p4.client = env.get_env_variable('Perforce', 'client')

    # Connect to the perforce server
    success = p4.connect()
    print( success )

    try:
        result = p4.run('have', version_file_path)
        print( '[WARNING] - Daily build already created for today' )
        value = input("Overwrite daily build version [Y/N]: ")
        if value == 'Y' or value == 'y':
            print( 'Overwriting old daily build version')
            return True
        else:
            print( 'Build Script canceled by user')
            return False
    except Exception:
        pass

    open( version_file_path, mode='w')
    print()

    # Upload the version file to perforce
    p4.run('add', version_file_path)
    p4.run('submit', '-d', '[SD][AUTOMATED] Update Build Version')

    print( 'Uploaded to perforce: ' + version_file_path )

    return True

if __name__ == '__main__':
    update_version_number()