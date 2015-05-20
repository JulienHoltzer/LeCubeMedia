# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime
import tweepy
import json

class TimedManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%H-%M-%S')
		#Twitter API
		file = open('mod/twitter.list')
		self.timed_data = json.load(file)
		file.close()

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
			file.write(state)
			file.close()
			

		
	    
def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
	auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
	return tweepy.API(auth)

def init(cube, params):
	logging.info("Time/Duration management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.action_manager = TimedManager(cube, tagtype)