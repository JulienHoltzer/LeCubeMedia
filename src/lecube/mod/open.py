# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime
import tweepy
import json

class OpenManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%H-%M-%S')
		if (data == 'DEF'):

			###check current state 
			filestate = open('mod/state', 'r')
			for line in iter(filestate):
				state = line
			logging.debug("Open : %s",state)
			filestate.close()

			###Twitter API
			file = open('mod/twitter.list')
			self.open_data = json.load(file)
			file.close()
			
	
			###if SoFAB is opening
			if(state == 'CLOSED'):

				file = open('mod/state', 'w')
				file.write('OPEN')
				file.close()
				api = get_api(self.open_data)
				tweet = st + ". SoFAB est maintenant ouvert!"
				status = api.update_status(status=tweet)
				logging.debug('TWEET sent')

	    		###if SoFAB is closing
			if(state == 'OPEN'):
				
				file = open('mod/state', 'w')
				file.write('CLOSED')
				file.close()
				api = get_api(self.open_data)
				tweet = st + ". SoFAB est maintenant fermé!"
				status = api.update_status(status=tweet)
				logging.debug('TWEET sent')

			
	
		### ---- if SoFAB is closing temporarily
		if (data == 'CLOSETEMP'):
			
				###check current state 
				filestate = open('mod/state', 'r')
				for line in iter(filestate):
					state = line
				logging.debug("Current state : %s",state)
				filestate.close()

				###Twitter API
				file = open('mod/twitter.list')
				self.open_data = json.load(file)
				file.close()

				###Set counter to zero
				file = open('mod/timedur', 'w')
				file.write('0')
				file.close()
				
				if(state == 'CLOSED'):
					logging.debug('Attention : SoFAB est deja fermé!')

				###if SoFAB is closing
				if(state == 'OPEN'):
					file = open('mod/state', 'w')
					file.write('CLOSED')
					file.close()

					file = open('mod/toshare', 'w')
					tweet = "Fermeture du SoFAB pour x minutes."
					file.write(tweet)
					file.close()
					logging.debug('SoFAB is closing; TWEET on-hold')

   
def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
	auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
	return tweepy.API(auth)

def init(cube, params):
	logging.info("SoFABOpen management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.open_manager = OpenManager(cube, tagtype)
