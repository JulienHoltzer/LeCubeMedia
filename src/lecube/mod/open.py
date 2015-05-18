# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime


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



def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
	auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
	return tweepy.API(auth)

def init(cube, params):
	logging.info("OPEN management module intialization")
	tagtype = params.get("tagtype","tst")
	cube.test_manager = TestManager(cube, tagtype)