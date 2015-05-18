# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime
<<<<<<< HEAD
import tweepy
import json

class OpenManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		self.recordv = None
		self.recorda = None
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%H-%M-%S')
		if (data == 'DEF'):

			#check current state 
			filestate = open('mod/state', 'r')
			for line in iter(filestate):
				state = line
			logging.debug("Open : %s",state)
			filestate.close()

			#Twitter API
			file = open('mod/twitter.list')
			self.open_data = json.load(file)
			file.close()
			
	
			#if SoFAB is opening
			if(state == 'CLOSED'):

				file = open('mod/state', 'w')
				file.write('OPEN')
				file.close()
				api = get_api(self.open_data)
				tweet = st + ". SoFAB est maintenant ouvert!"
				status = api.update_status(status=tweet)
				logging.debug('TWEET sent')

	    		#if SoFAB is closing
			if(state == 'OPEN'):
				
				file = open('mod/state', 'w')
				file.write('CLOSED')
				file.close()
				api = get_api(self.open_data)
				tweet = st + ". SoFAB est maintenant fermé!"
				status = api.update_status(status=tweet)
				logging.debug('TWEET sent')

			
	
		# ---- if SoFAB is closing temporarily
		if (data == 'CLOSETEMP'):
			
				file = open('mod/state', 'w')
				file.write('CLOSED')
				file.close()
				api = get_api(self.open_data)
				tweet = st + ". SoFAB est maintenant fermé pour " + x = " minutes."
				status = api.update_status(status=tweet)
				logging.debug('TWEET sent')

		
	    
=======


class OpenManager :

    def __init__(self, cube, tagtype):
	   self.cube = cube
	   self.recordv = None
	   self.recorda = None
	   cube.register_tag_handler(tagtype,self.handle_action_tag)

    def handle_action_tag(self, ttype, data):
        logging.debug("Action : %s",data)
        ts = time.time()
        if (data == 'DEF'):

            # check current state
            file = open('mod/state.conf')
            self.open_data = json.load(file)
            file.close()

            # if SoFAB is opening...
            if(self.open_data == 'CLOSE'):
                say = 'Il est' + ts + '. SoFab est maintenant ouvert!'
                file = open('mod/state.conf', 'w')
                file.write('OPEN')
                file.close()

            # if SoFAB is closing...
            if(self.open_data == 'OPEN'):
                say = 'Il est' + ts + '. SoFab est maintenant fermé!'
                file = open('mod/state.conf', 'w')
                file.write('CLOSE')
                file.close()

        # --- if SoFAB is closing temporarily...
        #if (data == 'CLOSETEMP'):

        #TWITTER API
        file = open('mod/twitter.list')
        self.twitter_data = json.load(file)
        file.close()


        api = get_api(self.twitter_data)
        tweet = "ATTENTION : " + say
        status = api.update_status(status=tweet)
        logging.debug('TWEET SENT!')



>>>>>>> d0d323f5426a76fb98c950a736b0165320396a87
def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
	auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
	return tweepy.API(auth)

def init(cube, params):
<<<<<<< HEAD
	logging.info("SoFABOpen management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.action_manager = OpenManager(cube, tagtype)
=======
	logging.info("OPEN management module intialization")
	tagtype = params.get("tagtype","tst")
	cube.test_manager = TestManager(cube, tagtype)
>>>>>>> d0d323f5426a76fb98c950a736b0165320396a87
