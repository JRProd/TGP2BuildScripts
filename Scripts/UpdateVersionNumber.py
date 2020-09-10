import datetime
import json

from P4 import P4, P4Exception

from . import Environment as env

game_name = env.get_env_variable('Game','game_name')

def update_version_number( major, minor, hotfix ):
    print( '----------------------------------------------------------------------------------------------------' )
    print( '{} - Step 2: Update the version number'.format( game_name ) )
    print( '----------------------------------------------------------------------------------------------------' )

    uproject_file_name = env.get_env_variable('Game', 'uproject_file')
    # Load the uproject file
    with open( uproject_file_name, 'r') as file:
        uproject_json = json.load( file )

    # Update the version number
    if 'Version' in uproject_json:
        new_version = get_version_number(major, minor, hotfix, uproject_json['Version'])
        uproject_json['Version'] = new_version
    else:
        uproject_json['Version'] = {'Major':'0', 'Minor':'0', 'Hotfix':'1'}

    # Add a pretty version
    uproject_json['Version']['Pretty'] = str(uproject_json['Version']['Major']) + '.' + str(uproject_json['Version']['Minor']) + '.' + str(uproject_json['Version']['Hotfix'])

    # Check the file out from P4
    p4 = P4()
    p4.user = env.get_env_variable('Perforce', 'user_name')
    p4.password = env.get_env_variable('Perforce', 'user_password')
    p4.client = env.get_env_variable('Perforce', 'client')


    try:
        p4.connect()

        p4.run( 'edit', uproject_file_name )

        with open( uproject_file_name, 'w') as file:
            json.dump( uproject_json, file, indent = 4 )

        change = p4.fetch_change()
        change._description = '[Daily_Builds] Updated the version number to ' + uproject_json['Version']['Pretty']
        test = p4.run_submit( change ) 

        return True
    except P4Exception:
        for e in p4.errors:
            print(e)

        return False
    except Exception as e:
        print(e)
        return False

def get_version_number(major, minor, hotfix, version):
    if major:
        version['Major'] = int(version['Major']) + 1
        version['Minor'] = 0
        version['Hotfix'] = 0
        return version

    if minor:
        version['Minor'] = int(version['Minor']) + 1
        version['Hotfix'] = 0
        return version

    if hotfix:
        version['Hotfix'] = int(version['Hotfix']) + 1
        return version
 

if __name__ == '__main__':
    update_version_number(False, False, True)