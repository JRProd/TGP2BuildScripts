import os

from configparser import ConfigParser
from configparser import ExtendedInterpolation

config = ConfigParser( interpolation=ExtendedInterpolation() )

def parse_env_variables( configParser, file ):
    if os.path.exists( file ):
        config.read( file )
        return True
    else:
        return False
        

def get_env_variable( section, var_name ):
    if len( config.sections() ) == 0: 
        success = parse_env_variables(config, 'config.ini')
        if not success:
            raise Exception("Failed to find file 'config.ini'")

    return config.get(section, var_name) 
