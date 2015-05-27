# -*- coding: utf-8 -*-

import logging
import subprocess
from os import listdir
from os.path import isfile, join

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class ToshareManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)

	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		gauth = GoogleAuth()
		drive = GoogleDrive(gauth)
		gauth.LoadCredentialsFile("mycreds.txt")
	
		#---find FOLDER ID
		#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
		#for file1 in file_list:
		#print 'title: %s, id: %s' % (file1['title'], file1['id'])
	

		if gauth.credentials is None:
			gauth.LocalWebserverAuth()
		elif gauth.access_token_expired:
			gauth.Refresh()
		else:
			gauth.Authorize()
		gauth.SaveCredentialsFile("mycreds.txt")

		drive = GoogleDrive(gauth)


		if (data == 'DOCS'):
			file1 = drive.CreateFile({'parents': [{"id": '0BzafXZYwn_6NbnBQN2VEejgzV1k'}]})
			file1.SetContentFile('mod/achat.txt')
			file1.Upload()

			file2 = drive.CreateFile({'parents': [{"id": '0BzafXZYwn_6NbnBQN2VEejgzV1k'}]})
			file2.SetContentFile('mod/depense.txt')
			file2.Upload()

		if (data == 'PICS'):
			onlyfiles = [f for f in listdir('/home/pi/images/') if isfile(join('/home/pi/images/',f))]

			for file in onlyfiles:
				file1 = drive.CreateFile({'parents': [{"id": '0BzafXZYwn_6NbnBQN2VEejgzV1k'}]})
				
				path = '/home/pi/images/' + file
				file1.SetContentFile(path)
				file1.Upload()
			
		logging.debug("Upload done.")
#0BzafXZYwn_6NbnBQN2VEejgzV1k    ('Guitare' Folder ID - test)
#0B8mDDuHeuNHDfmM0OXlWTndpdkczNHBBY3VJaXJ2ZlNqVVBoWWk3UDZnc0NvMS1Gd1JtWU0 ('Cube' folder ID)



def init(cube, params):
    logging.info("Toshare management module initialization")
    tagtype = params.get("tagtype","twt")
    cube.toshare_manager = ToshareManager(cube, tagtype)
