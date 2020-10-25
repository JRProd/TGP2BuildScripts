import subprocess

from . import Environment as env

game_name = env.get_env_variable('Game', 'game_name')

def upload_to_steam( log_file ):

    log_file.write( '----------------------------------------------------------------------------------------------------\n' )
    log_file.write( '{} - Step 5: Starting Upload to Steam\n'.format( game_name ) )
    log_file.write( '----------------------------------------------------------------------------------------------------\n' )
    log_file.flush()

    user_name = env.get_env_variable( "Steam", "user_name" )
    user_password = env.get_env_variable( "Steam", "user_password" )
    steam_dir = env.get_env_variable( "Steam", "steam_dir" )
    steam_cmd = env.get_env_variable( "Steam", "steam_cmd" )
    app_build = env.get_env_variable( "Steam", "app_build" )

    result = subprocess.run( [steam_dir + steam_cmd, "+login", user_name, user_password, "+run_app_build_http", steam_dir + app_build, "+quit"], stdout=log_file )

    log_file.flush()
    return result.returncode == 0

if __name__ == '__main__':
    upload_to_steam()



