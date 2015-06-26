#-*- coding: utf-8 -*-

import logging
import subprocess
import speech_recognition as sr
import os

os.system("arecord -D plughw:1,0 --duration=4 -f S16_LE -r48000 say.wav")

r = sr.Recognizer("fr-FR")
with sr.WavFile("say.wav") as source:
	audio = r.record(source)

try:
	print r.recognize(audio)
except LookupError:
	print "ATTENTION : Erreur de compréhension"
	logging.debug("ATTENTION : Erreur de compréhension")

text1 = "espeak -v en \"" + r.recognize(audio) + "\""
cmd = text1
logging.debug(cmd)
print cmd
os.system(cmd)

### arecord -D plughw:1,0 -f S16_LE -c1 -r48000 tset.wav