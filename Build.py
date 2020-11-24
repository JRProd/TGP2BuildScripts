import argparse
import sys

from Scripts.UpdateVersionNumber import update_version_number
from Scripts.UpdateFromP4 import update_from_P4
from Scripts.BuildLighting import build_lighting
from Scripts.BuildGame import build_game
from Scripts.UploadToDeletedNighly import upload_to_deleted_nightly
from Scripts.UploadToSteam import upload_to_steam
from Scripts.BuildInstaller import build_installer

from Scripts import Environment as env

# Create and setup the argument parser for the user scripts
parser = argparse.ArgumentParser(description='Python based UE4 Versioning, Building, Packaging, and Uploading suite')
parser.add_argument('-m', '--minor', action='store_true', default=False, help='Increment the minor version of the project. Will be overriden by the major argument')
parser.add_argument('-M', '--major', action='store_true', default=False, help='Increment the major version of the project. Will override the minor argument')
parser.add_argument('-n', '--no-lighting', action='store_true', default=False, help='Skip the lighting build')
parser.add_argument('-a', '--all', action='store_true', default=False, help='Run the full script suite. This is purely for verbosity. Giving no individual script arguments has the same effect')
parser.add_argument('-p4', '--perforce', action='store_true', default=False, help='Update from P4V')
parser.add_argument('-uv', '--version', action='store_true', default=False, help='Update the version number')
parser.add_argument('-bl', '--lighting', action='store_true', default=False, help='Build the lighting')
parser.add_argument('-bg', '--build', action='store_true', default=False, help='Build the game')
parser.add_argument('-us', '--steam', action='store_true', default=False, help='Upload to steam')
parser.add_argument('--output', action='store', nargs='?', default='log.txt', help='Set the output files name that is generated in the environments build location')

def script_error( log_file, error_message ):
    log_file.write("ERROR: " + error_message)
    log_file.close()
    quit(1)

if __name__ == '__main__':
    args = parser.parse_args()

    build_dir = env.get_env_variable('Game', 'builds_dir')
    log_file = open( build_dir + args.output, 'w')
    sys.stderr = log_file

    log_file.write( '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n' )
    log_file.write( 'Initiating Build Sequence\n' )


    # If no commands are give, assume the user wants to run the full suite of scripts
    args.all = True if not (args.perforce or args.version or args.lighting or args.build or args.steam) else args.all

    # Defines the success of the previous operation
    success = True
    if args.all or args.perforce:
        success = update_from_P4(log_file)
    if not success:
        script_error(log_file, 'Failed to update from P4V')

    if success and (args.all or args.version):
        success = update_version_number( log_file, args.major, args.minor)
    if not success:
        script_error(log_file, 'Failed to update the version number')

    if success and not args.no_lighting and (args.all or args.lighting):
        success = build_lighting( log_file )
    if not success:
        script_error(log_file, 'Failed to build the lighting')

    if success and (args.all or args.build):
        success = build_game( log_file )
    if not success:
        script_error( log_file, 'Failed to build and package the game')

    if success and (args.all or args.steam):
        success = upload_to_steam( log_file )
    if not success:
        script_error( log_file, 'Failed to upload to steam')

    log_file.write('Sequence finished without error.\n')
    log_file.write('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    log_file.close()

    quit(0)