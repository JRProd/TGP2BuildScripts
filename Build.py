from UpdateVersionNumber import update_version_number
from UpdateFromP4 import update_from_P4
from BuildGame import build_game
from UploadToDeletedNighly import upload_to_deleted_nightly
from UploadToSteam import upload_to_steam

if __name__ == '__main__':
    print( '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print( 'Initiating Build Sequence ')

    success = update_version_number()
    if success:
        update_from_P4()
        build_game()
        upload_to_steam()