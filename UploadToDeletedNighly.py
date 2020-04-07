import subprocess

import Environment as env

game_name = env.get_env_variable('Game', 'game_name')

def upload_to_deleted_nightly():
    print( '----------------------------------------------------------------------------------------------------' )
    print( '{} - Step 4: Uploading the completed build to Deleted Nightly'.format( game_name ) )
    print( '----------------------------------------------------------------------------------------------------' )

    # Get variables for network connection
    bound_drive_letter = env.get_env_variable('Local', 'drive_letter')
    deleted_nightly_dir = env.get_env_variable('SMU', 'deleted_nightly_dir')
    executable_dir = env.get_env_variable('SMU', 'remote_archive_dir')

    print( executable_dir)

    smu_username= env.get_env_variable('SMU', 'user_name')
    smu_password= env.get_env_variable('SMU', 'user_password')

    # Maps the network drive to 'K:'
    print(subprocess.run( ['net', 'use', bound_drive_letter, deleted_nightly_dir, '/user:' + smu_username, smu_password, '/persistent:no' ] ))


    # Removes the network drive 'K:'
    print( subprocess.run(['net', 'use', bound_drive_letter, '/d']))

if __name__ == '__main__':
    upload_to_deleted_nightly()