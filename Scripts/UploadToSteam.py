import subprocess

from . import Environment as env

game_name = env.get_env_variable('Game', 'game_name')

def upload_to_steam():

    print( '----------------------------------------------------------------------------------------------------' )
    print( '{} - Step 3: Starting Upload to Steam'.format( game_name ) )
    print( '----------------------------------------------------------------------------------------------------' )

    user_name = env.get_env_variable( "Steam", "user_name" )
    user_password = env.get_env_variable( "Steam", "user_password" )
    steam_dir = env.get_env_variable( "Steam", "steam_dir" )
    steam_cmd = env.get_env_variable( "Steam", "steam_cmd" )
    app_build = env.get_env_variable( "Steam", "app_build" )

    print(subprocess.run( [steam_dir + steam_cmd, "+login", user_name, user_password, "+run_app_build_http", steam_dir + app_build, "+quit"] ))

    return True

if __name__ == '__main__':
    upload_to_steam()



