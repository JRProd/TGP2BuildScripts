import subprocess

import Environment as env

game_name = env.GetEnvVariable('Game', 'game_name')

def UploadToDeletedNightly():
    print( '----------------------------------------------------------------------------------------------------' )
    print( '{} - Step 4: Uploading the completed build to Deleted Nightly'.format( game_name ) )
    print( '----------------------------------------------------------------------------------------------------' )

    # Get variables for network connection
    bound_drive_letter = env.GetEnvVariable('Local', 'drive_letter')
    deleted_nightly_dir = env.GetEnvVariable('SMU', 'deleted_nightly_dir')
    executable_dir = env.GetEnvVariable('SMU', 'remote_archive_dir')

    print( executable_dir)

    smu_username= env.GetEnvVariable('SMU', 'user_name')
    smu_password= env.GetEnvVariable('SMU', 'user_password')

    # Maps the network drive to 'K:'
    print(subprocess.run( ['net', 'use', bound_drive_letter, deleted_nightly_dir, '/user:' + smu_username, smu_password, '/persistent:no' ] ))


    # Removes the network drive 'K:'
    print( subprocess.run(['net', 'use', bound_drive_letter, '/d']))

if __name__ == '__main__':
    UploadToDeletedNightly()