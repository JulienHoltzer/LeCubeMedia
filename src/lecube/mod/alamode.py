# -*- coding: utf-8 -*-
import thread
import subprocess
import logging

import serial
import json
import time

def listen(cube,params):
    # commencer par relancer l'Arduino
    try:
        logging.debug("Transmission du programme de lecture à la carte alamode")
        subprocess.call('avrdude -c alamode -b 115200 -P /dev/ttyS0 -p m328p -U flash:w:firmware.hex', shell=True)
        # ouverture de la liaison série
        logging.debug("Ouverture de la liaison série")
	ser = serial.Serial(0,timeout=4)
    except:
	logging.error("Erreur a l'ouverture de la liaison série : %s", sys.exc_info()[0])
    # les dernières valeurs reçues
    lastID = None
    lasttime = 0
    # boucle de lecture de la liaison série
    while True:
#	logging.debug("En attente d'un message")
	line = ser.readline()
	# on ne traite pas les chaines vides (timeout)
	if len(line) == 0:
	    continue
        elif line in "Read":
	    logging.error("ALERTE : la carte Alamode s'est bloquée")
	    ser.close()
	    subprocess.call('avrdude -c alamode -b 115200 -P /dev/ttyS0 -p m328p -U flash:w:firmware.hex', shell=True)
	    ser = serial.Serial(0,timeout=4)
	# sinon, on essaie de lire le JSON
	#logging.debug("Reçu : %s",line)
	try: 
	    data = json.loads(line)
	    # tester si la reception du meme tag n'est pas deja ancienne
	    if data['ID'] == lastID and (time.time() - lasttime) > 5:
		logging.debug("Relecture du meme tag autorisee")
            	lastID = None
	    # tester si le message contient un ID et qu'il n'est pas déjà 
	    
	    if len(data['ID']) != 0 and data['ID'] != lastID:
		logging.info("Nouveau tag : %s",data['ID'])
                lastID = data['ID']
		lasttime = time.time()
		cube.tag_detection('NFC','NFC:'+lastID)
            # TODO les autres valeurs (capteurs, ...)
	except ValueError:
            #logging.debug("Erreur, ce n'est pas du JSON %s",line)
	    pass

def init(cube, params):
    logging.info("Launching Alamode serial reader thread")
    thread.start_new_thread(listen, (cube,params))
