# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime

class ActionManager :

    def __init__(self, cube, tagtype):
	self.cube = cube
	self.recordv = None
	self.recorda = None
	cube.register_tag_handler(tagtype,self.handle_action_tag)

    def handle_action_tag(self, ttype, data):
	logging.debug("Action : %s",data)
	if (data == 'STOP'):
	    # arrete les videos en lecture
	    command = 'killall /usr/bin/omxplayer.bin'
	    subprocess.call(command.split(),shell=False)
	    # arrete les enregistrements
	    if (self.recordv != None): 
	 	self.cube.tag_detection('CHATROOM','CHATROOM:Une nouvelle video tournee')
		self.recordv.kill()
		self.recorda.kill()
	if (data == 'PHOTO'):
	    ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
            # TODO : pas de chemin en dur
            # TODO : creer un repertoire par PROJET (par exemple)
	    filename = '/home/pi/images/'+ st +'.jpg'
            command = 'raspistill -hf -vf --width 400 --height 300 --timeout 1000 -awb auto -o '+filename
	    logging.debug(command)
	    subprocess.call(command.split(),shell=False)
	    self.cube.tag_detection('CHATROOM','CHATROOM:PHOTO:'+st)
            self.cube.tag_detection('TWITTER','TWITTER:PHOTO:'+filename)
	    logging.debug('CLIC !')
	if (data == 'RECORD'):
	    self.cube.tag_detection('CHATROOM','CHATROOM:Attention, ça tourne !')
	    ts = time.time()
	    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
	    st = 'last'
	    commandv = 'raspivid -t 300000 -w 1280 -h 720 -b 2000000 -fps 30 --vflip -awb fluorescent -sa -10 -br 60 -co 50 -o /home/pi/records/' + st + ".avi"
	    commanda = 'arecord -D plughw:0,0 -f cd -d 300 /home/pi/records/' + st + '.wav'
	    logging.debug(commandv)
	    logging.debug(commanda)
	    self.recordv = subprocess.Popen(commandv.split(),shell=False)
	    self.recorda = subprocess.Popen(commanda.split(),shell=False)
	if (data == 'HALT'):
	    self.cube.tag_detection('CHATROOM',"CHATROOM:Le Cube va s'arrêter, bye !")
	    command = 'sudo halt'
	    subprocess.call(command.split(),shell=False)

def init(cube, params):
    logging.info("Action management module initialization")
    tagtype = params.get("tagtype","act")
    cube.action_manager = ActionManager(cube, tagtype)

