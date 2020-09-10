import subprocess
from datetime import datetime

from . import FileUtils as file_utils
from . import Environment as env

game_name = env.get_env_variable('Game', 'game_name')
builds_dir = env.get_env_variable( "Game", "builds_dir" )

def build_game():

    print( '----------------------------------------------------------------------------------------------------' )
    print( '{} - Step 3: Starting BuildCookRun'.format( game_name ) )
    print( '----------------------------------------------------------------------------------------------------' )

    uproject_file = env.get_env_variable( "Game", "uproject_file" )
    build_maps = env.get_env_variable( "Game", "build_maps" )

    ue4_batchfiles_dir = env.get_env_variable( 'Local', "ue4_batchfiles_dir" )
    ue4_binaries_dir = env.get_env_variable( 'Local', "ue4_binaries_dir" )

    print(subprocess.run( [ ue4_batchfiles_dir + 'RunUAT.bat', "BuildCookRun", "-project=" + uproject_file, "-noP4", "-nocompile", "-nocompileeditor", "-installed", "-cook", "-stage", "-archive", "-archivedirectory=" + builds_dir, "-package", "-clientconfig=Development", "-ue4exe=" + ue4_binaries_dir + "UE4Editor-Cmd.exe", "-pak", "-prereqs", "-nodebuginfo", "-targetplatform=Win64", "-build", "-CrashReporter", "-utf8output" ] ))

    return True

def zip_build():
    latest_build_dir = env.get_env_variable( "Game", "latest_build_dir" )

    now = datetime.now()
    now_str = now.strftime( "%m_%d_%H_%M" )

    file_utils.zip_file_directory( latest_build_dir, builds_dir + game_name + "_" + now_str + ".zip" )


if __name__ == '__main__':
    build_game()
    zip_build()