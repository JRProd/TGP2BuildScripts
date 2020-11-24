import subprocess

from . import Environment as env

game_name = env.get_env_variable('Game', 'game_name')

def build_installer():
    exe_build_script = env.get_env_variable( 'Local', "exe_build_script" )
    inno_setup_exe = env.get_env_variable( 'Local', "inno_setup_exe" )

    # Yay, the build was a success!
    # Step 3 Time to make an installer using the created archive
    # I don't believe this step can fail, as I never had it fail, but you could check this return code too
    print( '----------------------------------------------------------------------' )
    print( '{} - Step 3: Building installer executable'.format( game_name ) )
    print( '----------------------------------------------------------------------' )
    print(subprocess.run( [ inno_setup_exe, exe_build_script ] ))


if __name__ == '__main__':
    build_installer()