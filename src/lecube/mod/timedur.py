# -*- coding: utf-8 -*-

import logging
import subprocess

class TimedManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)

		if (data == '30'):
			filestate = open('mod/timedur', 'r')
			for line in iter(filestate):
				state = line
			logging.debug("Previously : %s",state)
			filestate.close()
			state = 30 + int(state)

			file = open('mod/timedur', 'w')
			state = str(state)
			logging.debug("Currently : %s",state)
			print "Counter: " + state
			file.write(state)
			file.close()

		if (data == '10'):
			filestate = open('mod/timedur', 'r')
			for line in iter(filestate):
				state = line
			logging.debug("Previously : %s",state)
			filestate.close()
			state = 10 + int(state)

			file = open('mod/timedur', 'w')
			state = str(state)
			logging.debug("Currently : %s",state)
			print "Counter: " + state
			file.write(state)
			file.close()

			

		if (data == '5'):
			filestate = open('mod/timedur', 'r')
			for line in iter(filestate):
				state = line
			logging.debug("Previously : %s",state)
			filestate.close()
			state = 5 + int(state)

			file = open('mod/timedur', 'w')
			state = str(state)
			logging.debug("Currently : %s",state)
			print "Counter: " + state
			file.write(state)
			file.close()
			

		
	

def init(cube, params):
	logging.info("Time/Duration management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.action_manager = TimedManager(cube, tagtype)