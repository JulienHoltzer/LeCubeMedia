# -*- coding: utf-8 -*-

import logging
import subprocess
import time
import datetime


def handle_project_tag(ttype, data):
	logging.info("Jadi woh benda ni tengok : %s !" %data)

def init(cube, params):
	logging.info("Mulakan process")
	tagtype = params.get("tagtype","prj")
	cube.register_tag_handler(tagtype, handle_project_tag)