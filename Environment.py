from configparser import ConfigParser

config = ConfigParser()

def ParseEnvVariables():
    config.read('config.ini')

def GetEnvVariable( section, var_name ):
    if len( config.sections() ) == 0: 
        ParseEnvVariables()

    return config.get(section, var_name)    
