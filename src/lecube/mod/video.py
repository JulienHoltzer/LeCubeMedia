# -*- coding: utf-8 -*-
import logging
import subprocess

class VideoManager : 

    def __init__(self,cube,tagtype):
	self.cube = cube
	self.playing = True
	cube.register_tag_handler(tagtype,self.handle_video_tag)

    def handle_video_tag(self,ttype,data):
	logging.debug("Traitement video %s",data)
    	if self.playing:
            command = 'killall /usr/bin/omxplayer.bin'
	    subprocess.call(command.split(), shell=False)
	    logging.debug("Arret de la lecture en cours")

#        command = 'omxplayer -b -w /home/pi/videos/{0} --loop'.format(data)
	command = 'omxplayer -b -w /home/pi/records/last.avi --loop'
        logging.debug("Lancement : %s",command)
        subprocess.Popen(command.split(), shell=False)
        self.playing=True

    def addHashtag(self, data):
	logging.debug("Ajout d'un tag")

def init(cube, params):
    logging.info("Video launcher module initialization")
    tagtype = params.get("tagtype","vid")
    cube.video_manager = VideoManager(cube,tagtype)
    
