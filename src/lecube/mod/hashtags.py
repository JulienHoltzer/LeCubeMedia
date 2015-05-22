# -*- coding: utf-8 -*-

import logging
import subprocess

class HashtagManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_hash_tag)

	def handle_hash_tag(self, ttype, data):
		logging.debug("Traitement du tag : %s",data)
		self.last_hashtag = data
		
		file = open('mod/hashtags', 'a')
		file.write('#'+ data + " ")
		file.close
		logging.debug("%s added",data)
		

def init(cube, params):
	logging.info("Hashtag management module initialization")
	tagtype = params.get("tagtype","act")
	cube.hashtag_manager = HashtagManager(cube, tagtype)
