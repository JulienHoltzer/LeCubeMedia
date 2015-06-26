# -*- coding: utf-8 -*-

import logging
import subprocess
import speech_recognition as sr
import os
import time
import datetime
import tweepy
import json

class VoiceManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)
	
	def handle_action_tag(self, ttype, data):
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
		logging.debug("Open : %s",data)
		a = "true"
		
		 #TWITTER API
	   	file = open('mod/twitter.list')
           	self.twitter_data = json.load(file)
           	file.close()

		while (a != "fin"):
			os.system("arecord -D plughw:1,0 --duration=4 -f S16_LE -r44100 mod/speech.wav")

			r = sr.Recognizer("fr-FR")
			with sr.WavFile("mod/speech.wav") as source:
				audio = r.record(source)
				print audio
			try:
				print ("Transcription: " + r.recognize(audio))
				a = r.recognize(audio)

				if (a == "poste"):
					api = get_api(self.twitter_data)
					file = open('mod/filepath', 'r')
					path = file.readlines()
					pic = path[0]
					
					### tweet à modifier, peut contenir des hashtags ou la date/l'heure.
					#file = open('mod/hashtags', 'r')
					#hash = file.readlines()				
	   				#tweet = "SoFAB"
					logging.debug(tweet)
	   				status = api.update_with_media(pic, status=tweet)
					print "Photo published."
	   				logging.debug('PHOTO published')

					file = open('mod/filepath', 'w').close()
					file = open('mod/hashtags', 'w').close()
				
				if (a == "photos"):
					filename = '/home/pi/images/'+ st +'.jpg'
					command = 'raspistill -hf -vf --width 1280 --height 720 --timeout 2000 -awb auto -o '+filename
					file = open('mod/filepath', 'w')
					file.write(filename)
					file.close
					subprocess.call(command.split(),shell=False)

				if (a == "test"):
					os.system("arecord -D plughw:1,0 --duration=4 -f S16_LE -r48000 say.wav")

					r = sr.Recognizer("")
					with sr.WavFile("say.wav") as source:
						audio = r.record(source)

					try:
						print r.recognize(audio)
						saytext = r.recognize(audio)
						text = "espeak -v en \"" + r.recognize(audio) + "\""
						cmd = text
						logging.debug(cmd)
						print cmd
						os.system(cmd)
						file = open('mod/say', 'w')
						file.write(saytext)
						file.close()
					except LookupError:
						print "ATTENTION : Erreur de compréhension"
						logging.debug("ATTENTION : Erreur de compréhension")

				

				if (a == "publié"):
					api = get_api(self.twitter_data)
					file = open('mod/say', 'r')
					tweet = file.readlines()		
	   				status = api.update_status(status=tweet)
					print "Tweet sent."
	   				logging.debug('Tweet sent')

					file = open('mod/say', 'w').close()
				
				
			except LookupError:
				print("Speech intelligible. Please try again.")
		
		print "Stopped."
	
def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['CONSUMER_KEY'], cfg['CONSUMER_SECRET'])
    auth.set_access_token(cfg['OAUTH_TOKEN'], cfg['OAUTH_TOKEN_SECRET'])
    return tweepy.API(auth)
		

def init(cube, params):
	logging.info("Voice management module initialization")
	tagtype = params.get("tagtype","ope")
	cube.open_manager = VoiceManager(cube, tagtype)
