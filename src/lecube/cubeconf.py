#std libs
import logging
from ConfigParser import ConfigParser
from importlib import import_module

def process_config_files(cube,cfnamelist):
    """
    This function read a list of configuration files.
    Format : INI
    - Each section represents a software module to set up
    - It expects a key called 'module' in each section, 
    - The module defined in each section is imported
    - The function init is called on each module with the following parameters (in this order):
    - cube : the instance of the Cube class
    - params : a dict that contains all the key/value pairs defined in 
    the current INI file section
    """

    #Read and parse the configuration files
    logging.info("Reading configuration files")
    configuration = ConfigParser()
    configuration.read(cfnamelist)
    
    # Dynamic plug-ins management
    for plugin in configuration.sections():
        logging.info("Initializing module: %s"%plugin)
        params = dict(configuration.items(plugin))
        modname = params.get('module')
        if modname is not None:
            try:
                mod = import_module(modname)
                mod.init(cube, params)
            except:
                logging.exception("Error during module %s initialization"%plugin)
        else:
            logging.info("No python module specified for %s"%plugin)
