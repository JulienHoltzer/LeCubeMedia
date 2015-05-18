#!/usr/bin/env python
# -*- coding: utf-8 -*-

#std libs
import logging
from logging.handlers import RotatingFileHandler
from optparse import OptionParser

#app includes
from cube import Cube
import cubeconf

if __name__ == "__main__":
    
    # Basic setup
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

# création d'un formateur qui va ajouter le temps, le niveau
    # de chaque message quand on écrira un message dans le log
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    # création d'un handler qui va rediriger une écriture du log vers
    # un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
    file_handler = RotatingFileHandler('/home/pi/LeCubeMedia/log/activity.log','a', 1000000,2)
    # on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
    # créé précédement et on ajoute ce handler au logger
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("Starting the cube")

    # Basic configuration and cmd line args
    parser = OptionParser()
    parser.add_option('-c', action="append", dest='cfglist', default=[])

    options, args = parser.parse_args()
    if len(options.cfglist)==0 : options.cfglist.append('cube.cfg')

    # Core object initialization
    zecube = Cube()
    zecube.logger = logger
    
    # Configuration files handling
    logger.info("Reading configuration files")
    logger.debug(' - '.join(options.cfglist))    

    cubeconf.process_config_files(zecube,options.cfglist)

    # Launching the main thread loop 
    zecube.loop()
