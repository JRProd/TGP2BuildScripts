import subprocess

game_name = 'HaberDashers'

network_dir=r'smu.edu\files\Guildhall$\Deleted Nightly\TGP2\HaberDasher'
smu_username= 'SMU\\spn02745'
smu_password= 'C@pst0n3Bu1ld'

if __name__ == '__main__':

    print( '----------------------------------------------------------------------------------------------------' )
    print( '{} - Step 4: Uploading the completed build to Deleted Nightly'.format( game_name ) )
    print( '----------------------------------------------------------------------------------------------------' )

    # proc = subprocess.Popen( ['net','use K:', '\\' + network_dir, '/user:' + smu_username, smu_password, '/persistent:no', '/savecred'] )
    print(subprocess.run( ['net', 'use', 'k:', r'\\smu.edu\files\Guildhall$', '/user:' + smu_username , smu_password] ))
    # print (subprocess.run(['net use Z:', '\\' + network_dir ]))