# -*- coding: utf-8 -*-

import os
import logging
import subprocess
import time
import datetime

class ActiviteManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		check1 = os.stat("mod/adherent").st_size
		check2 = os.stat("mod/tool").st_size
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
		file1 = open('mod/adherent', 'r')
		adh = file1.readlines()
		file1.close()
		file2 = open('mod/tool', 'r')
		too = file2.readlines()
		file2.close()
		file3 = open('mod/timedur', 'r')
		tim = file3.readlines()
		file3.close()

			

		if (data == 'DEPENSE'):
			if (check1 == 0 or check2 == 0 or tim[0] == '0'):
				print "Error: missing data"
				logging.debug("Error: missing data")	
			else:
				info = adh[0] + "," + too[0] + "," + tim[0] + "," + st	+ "\n"	
				file4 = open('mod/depense', 'a')
				file4.write(info)
				file4.close()

		if (data == 'ACHAT'):
			if (check1 == 0 or tim[0] == '0'):
				print "Error: missing data"
				logging.debug("Error: missing data")
			else:
				info = adh[0] + "," + tim[0] + "," + st + "\n"	
				file4 = open('mod/achat', 'a')
				file4.write(info)
				file4.close()

		file1 = open('mod/adherent', 'w').close()
		file2 = open('mod/tool', 'w').close()
		file3 = open('mod/timedur', 'w')
		file3.write('0')
		file3.close()
		print "Done."
		logging.debug("Data saved")


def init(cube, params):
	logging.info("Activite management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.open_manager = ActiviteManager(cube, tagtype)


