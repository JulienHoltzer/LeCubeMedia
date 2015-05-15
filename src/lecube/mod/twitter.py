# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime
import tweepy

class TwitterManager :
	


    def __init__(self, cube, tagtype):
	self.cube = cube
	self.recordv = None
	self.recorda = None
	cube.register_tag_handler(tagtype,self.handle_action_tag)

    def handle_action_tag(self, ttype, data):
	logging.debug("Test : %s",data)
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')

	#TWITTER API
	cfg = {
		"CONSUMER_KEY": "value",
		"CONSUMER_SECRET": "valuee",
		"OAUTH_TOKEN": "valueee",
		"OAUTH_TOKEN_SECRET": "valueeee"
	}

	api = get_api(cfg)
	photo_path = data
	tweet = "SoFAB: " + st
	status = api.update_with_media(data, status=tweet)
	logging.debug('SECOND CLIC !')

def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
	auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
	return tweepy.API(auth)

def init(cube, params):
	logging.info("Project Twitter")
	tagtype = params.get("tagtype","twt")
	cube.twitter_manager = TwitterManager(cube, tagtype)