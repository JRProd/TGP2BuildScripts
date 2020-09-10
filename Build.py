from Scripts.UpdateVersionNumber import update_version_number
from Scripts.UpdateVersionNumber import update_version_number
from Scripts.UpdateFromP4 import update_from_P4
from Scripts.BuildGame import build_game
from Scripts.UploadToDeletedNighly import upload_to_deleted_nightly
from Scripts.UploadToSteam import upload_to_steam


if __name__ == '__main__':
    print( '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print( 'Initiating Build Sequence ')

    success = update_from_P4()
    if success:
        success = True #update_version_number( False, False, True)
        pass
    else:
        print("[FAILED] Failed to update from perforce")

    if success:
        success = build_game()
        pass
    else:
        print("[FAILED]: Failed to update version number")

    if success:
        # success = upload_to_steam()
        pass
    else:
        print("[FAILED]: FAiled to build and package the project")

    if not success:
        print("[FAILED]: Failed to upload the package")