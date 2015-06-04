# -*- coding: utf-8 -*-

import logging
import subprocess
import os
from os import listdir
from os.path import isfile, join

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class UpdriveManager :

	def __init__(self, cube, tagtype):
		self.cube = cube
		cube.register_tag_handler(tagtype,self.handle_action_tag)

	def handle_action_tag(self, ttype, data):
		logging.debug("Open : %s",data)
		gauth = GoogleAuth()
		drive = GoogleDrive(gauth)
		gauth.LoadCredentialsFile("mycreds.txt")
		check = os.stat("mod/hashtags").st_size

		######---find FOLDER ID
		#file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
		#for file1 in file_list:
		#	print 'title: %s, id: %s' % (file1['title'], file1['id'])
	
		######---authentication
		if gauth.credentials is None:
			gauth.LocalWebserverAuth()
		if gauth.access_token_expired:
			gauth.Refresh()
		else:
			gauth.Authorize()
		gauth.SaveCredentialsFile("mycreds.txt")

		if (data == 'DOCS'):
			
			### upload achat and depense 
			file1 = drive.CreateFile({'parents': [{"id": '0B8mDDuHeuNHDfmM0OXlWTndpdkczNHBBY3VJaXJ2ZlNqVVBoWWk3UDZnc0NvMS1Gd1JtWU0'}]})
			file1.SetContentFile('mod/achat.txt')
			file1.Upload()
				
			file2 = drive.CreateFile({'parents': [{"id": '0B8mDDuHeuNHDfmM0OXlWTndpdkczNHBBY3VJaXJ2ZlNqVVBoWWk3UDZnc0NvMS1Gd1JtWU0'}]})
			file2.SetContentFile('mod/depense.txt')
			file2.Upload()
			logging.debug("Upload done.")

		if (data == 'PICS'):
			file = open('mod/filepath', 'r')
			path = file.readlines()
			pic = path[0]

			if (check == 0):
			### list every photo
				onlyfiles = [f for f in listdir('/home/pi/images/') if isfile(join('/home/pi/images/',f))]

			### upload pic	
				file1 = drive.CreateFile({'parents': [{"id": '0B8mDDuHeuNHDfmM0OXlWTndpdkczNHBBY3VJaXJ2ZlNqVVBoWWk3UDZnc0NvMS1Gd1JtWU0'}]})
				file1.SetContentFile(pic)
				file1.Upload()
				logging.debug("Upload done.")

				file = open('mod/filepath', 'w').close()
			else:
				file = open('mod/hashtags', 'r')
				hash = file.readlines()	
				hashtag = hash[0]
				hashtag = hashtag[1:-1]
				

				file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
				for file1 in file_list:
					print 'title: %s, id: %s' % (file1['title'], file1['id'])
					print hashtag
					print file1['title']
					if (file1['title'] == hashtag):
						file1 = drive.CreateFile({'parents': [{"id": file1['id']}]})
						file1.SetContentFile(pic)
						file1.Upload()
						logging.debug("Upload done.")
					

				file = open('mod/filepath', 'w').close()
				file = open('mod/hashtags', 'w').close()


#0BzafXZYwn_6NbnBQN2VEejgzV1k    ('Guitare' Folder ID - test)
#0B8mDDuHeuNHDfmM0OXlWTndpdkczNHBBY3VJaXJ2ZlNqVVBoWWk3UDZnc0NvMS1Gd1JtWU0 ('Cube' folder ID)



def init(cube, params):
    logging.info("Updrive management module initialization")
    tagtype = params.get("tagtype","twt")
    cube.toshare_manager = UpdriveManager(cube, tagtype)
