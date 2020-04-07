from configparser import ConfigParser
from configparser import ExtendedInterpolation

config = ConfigParser( interpolation=ExtendedInterpolation() )

def ParseEnvVariables():
    config.read('config.ini')

def GetEnvVariable( section, var_name ):
    if len( config.sections() ) == 0: 
        ParseEnvVariables()

    return config.get(section, var_name)    
