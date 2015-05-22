# -*- coding: utf-8 -*-

import logging
import subprocess
import json

class ToolManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)

		file = open('mod/tools.list')
		self.adherent_data = json.load(file)
		file.close()
		name = self.adherent_data[data]
		print "Tool: " + name

		file = open('mod/tool', 'w')
		file.write(name)
		file.close()
		logging.debug("Item saved")

def init(cube, params):
	logging.info("Tool management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.open_manager = ToolManager(cube, tagtype)
