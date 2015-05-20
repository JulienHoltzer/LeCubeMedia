# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime
import tweepy
import json

class TwitterManager :



    def __init__(self, cube, tagtype):
	   self.cube = cube
	   cube.register_tag_handler(tagtype,self.handle_action_tag)

    def handle_action_tag(self, ttype, data):
	   logging.debug("Test : %s",data)
	   ts = time.time()
	   st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')

	   #TWITTER API
	   file = open('mod/twitter.list')
           self.twitter_data = json.load(file)
           file.close()


	#TWITTER API
	   file = open('mod/twitter.list')
	   self.twitter_data = json.load(file)
	   file.close()
	
	




	   api = get_api(self.twitter_data)
	   photo_path = data
	   tweet = "SoFAB: " + st
	   status = api.update_with_media(data, status=tweet)
	   logging.debug('SECOND CLIC !')

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
    auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
    return tweepy.API(auth)

def init(cube, params):
    logging.info("Twitter management module initialization")
    tagtype = params.get("tagtype","twt")
    cube.twitter_manager = TwitterManager(cube, tagtype)