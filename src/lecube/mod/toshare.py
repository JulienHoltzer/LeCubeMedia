# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime
import tweepy
import json

class ToshareManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)

	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')

		if (data == 'TWITTER'):

			filetimedur = open('mod/timedur', 'r')
			for line in iter(filetimedur):
				timedur = line
			logging.debug("Open : %s",timedur)
			filetimedur.close()

			filetoshare = open('mod/toshare', 'r')
			for line in iter(filetoshare):
				tweet = str.replace(line, " x ", " " + timedur + " ")
			logging.debug("Open : %s",tweet)
			filetoshare.close()

			###Twitter API
			file = open('mod/twitter.list')
			self.open_data = json.load(file)
			file.close()

			api = get_api(self.open_data)
			status = api.update_status(status=tweet)
			logging.debug('TWEET sent')



		#if (data == 'FACEBOOK'):




def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
    auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
    return tweepy.API(auth)

def init(cube, params):
    logging.info("Toshare management module initialization")
    tagtype = params.get("tagtype","twt")
    cube.toshare_manager = ToshareManager(cube, tagtype)