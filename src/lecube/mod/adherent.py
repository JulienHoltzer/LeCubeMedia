# -*- coding: utf-8 -*-

import logging
import subprocess
import json

class AdherentManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		
		file = open('mod/adherents.list')
		self.adherent_data = json.load(file)
		file.close()
		name = self.adherent_data[data]
		print "Name: " + name

		file = open('mod/adherent', 'w')
		file.write(name)
		file.close()
		logging.debug("Name saved")

def init(cube, params):
	logging.info("Adherent management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.open_manager = AdherentManager(cube, tagtype)


