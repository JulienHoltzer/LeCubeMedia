# -*- coding: utf-8 -*-

import logging
import subprocess


class ResetManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		
		file = open('mod/toshare', 'w').close
		file = open('mod/tool', 'w').close
		file = open('mod/filepath', 'w').close
		file = open('mod/adherent', 'w').close
		file = open('mod/hashtags', 'w').close
		file = open('mod/timedur', 'w')
		file.write('0')
		file.close()
		
		logging.debug("Data cleared.")

def init(cube, params):
	logging.info("Reset management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.open_manager = ResetManager(cube, tagtype)