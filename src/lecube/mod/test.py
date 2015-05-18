# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime


class TestManager :

    def __init__(self, cube, tagtype):
	self.cube = cube
	self.recordv = None
	self.recorda = None
	cube.register_tag_handler(tagtype,self.handle_action_tag)

    def handle_action_tag(self, ttype, data):
	logging.debug("Test : %s",data)

	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')

	# TODO : pas de chemin en dur
	# TODO : creer un repertoire par PROJET (par exemple)
	filename = '/home/pi/images/'+ st +'.jpg'
	command = 'raspistill -hf -vf --width 1280 --height 720 --timeout 1000 -awb auto -o '+filename
	logging.debug(command)
	subprocess.call(command.split(),shell=False)

	#test to tweet string
	say = "CubeCubicCubicleTest"
	self.cube.tag_detection('TWITTER','TWITTER:'+filename)
	logging.debug('CLIC !')

def init(cube, params):
	logging.info("TEST management module initialization")
	tagtype = params.get("tagtype","tst")
	cube.test_manager = TestManager(cube, tagtype)