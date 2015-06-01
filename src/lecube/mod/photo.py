# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime


class PhotoManager :

    def __init__(self, cube, tagtype):
	self.cube = cube
	cube.register_tag_handler(tagtype,self.handle_action_tag)

    def handle_action_tag(self, ttype, data):
	logging.debug("Open : %s",data)

	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')

	# TODO : pas de chemin en dur
	# TODO : creer un repertoire par PROJET (par exemple)
	filename = '/home/pi/images/'+ st +'.jpg'
	command = 'raspistill -hf -vf --width 1280 --height 720 --timeout 3000 -awb auto -o '+filename
	file = open('mod/filepath', 'w')
	file.write(filename)
	file.close
	logging.debug(command)
	subprocess.call(command.split(),shell=False)

	### --- automatic post to Twitter
	#self.cube.tag_detection('TWITTER','TWITTER:'+filename)
	#logging.debug('CLIC !')

def init(cube, params):
	logging.info("PHOTO management module initialization")
	tagtype = params.get("tagtype","tst")
	cube.photo_manager = PhotoManager(cube, tagtype)
