import subprocess

game_name = 'HaberDashers'

bound_drive_letter = 'K:'
deleted_nightly_dir=r'\\smu.edu\files\Guildhall$\Deleted Nightly'
executable_dir = bound_drive_letter + r'\C29\TGP2\HaberDashers\Executables'

smu_username= r'smu\spn02745'
smu_password= 'C@pst0n3Bu1ld'

if __name__ == '__main__':

    print( '----------------------------------------------------------------------------------------------------' )
    print( '{} - Step 4: Uploading the completed build to Deleted Nightly'.format( game_name ) )
    print( '----------------------------------------------------------------------------------------------------' )

    # Maps the network drive to 'K:'
    print(subprocess.run( ['net', 'use', bound_drive_letter, deleted_nightly_dir, '/user:' + smu_username, smu_password, '/persistent:no' ] ))


    # Removes the network drive 'K:'
    print( subprocess.run(['net', 'use', bound_drive_letter, '/d']))