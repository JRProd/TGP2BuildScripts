from configparser import ConfigParser
from configparser import ExtendedInterpolation

config = ConfigParser( interpolation=ExtendedInterpolation() )

def parse_env_variables():
    config.read('config.ini')

def get_env_variable( section, var_name ):
    if len( config.sections() ) == 0: 
        parse_env_variables()

    return config.get(section, var_name)    
