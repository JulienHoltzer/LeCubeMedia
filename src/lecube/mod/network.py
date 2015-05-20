# -*- coding: utf-8 -*-

import logging
import subprocess
import os
import json

class NetworkManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		os.system('sudo cp /etc/wpa_supplicant/wpa-roam.conf mod/wpa-roam.conf')

		f = open('mod/wpa-roam.conf', "r")
		w = open('mod/listssidfromfile', "w")

		for line in iter(f):
			target = "ssid"
			words = line.split("=")
			prevline = ""

			for line in words:
				if 'ssid' in prevline:
					ssid = line[1:-1].rstrip('"')
					w.write(ssid + "\n")
				prevline = line

		w.close()
		f.close()
		logging.debug("SSID from file listed")

		os.system('sudo iwlist wlan1 scan | grep ESSID > mod/scanresults')
		f = open ('mod/scanresults', "r")
		w = open('mod/listssidfromscan', "w")

		for line in iter(f):
	
			prevline = ""
			words = line.split(":")
			for i in words:
				if 'ESSID' in prevline:
					ssid = i[1:-1].rstrip('"')
					if ssid != "":
						w.write(ssid + "\n")
				prevline = i

		w.close()
		f.close()

		seenlines = set()
		outfile = open('mod/listssidfromscanfin', "w")
		r = open('mod/listssidfromscan', "r")
		for line in r:
			if line not in seenlines:
				outfile.write(line)
				seenlines.add(line)

		outfile.close()
		logging.debug("SSID from scan listed")

def init(cube, params):
	logging.info("Network management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.open_manager = NetworkManager(cube, tagtype)
