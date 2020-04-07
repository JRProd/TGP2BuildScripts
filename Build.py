import Update_Version_Number
import Update_From_P4

if __name__ == '__main__':
    print( '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print( 'Initiating Build Sequence ')

    success = Update_Version_Number.UpdateVersionNumber()
    if success:
        Update_From_P4.UpdateFromP4()