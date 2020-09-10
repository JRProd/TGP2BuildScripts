import os
import zipfile

def zip_file_directory( directory_path, zip_file_path ):
    zip_file = zipfile.ZipFile( zip_file_path, 'w', zipfile.ZIP_STORED )

    for root, dirs, files in os.walk( directory_path ):
        for file in files:
            relative_path = os.path.relpath( root, directory_path )

            zip_file.write( os.path.join( root, file ), relative_path + '\\' + file )

    zip_file.close()
    