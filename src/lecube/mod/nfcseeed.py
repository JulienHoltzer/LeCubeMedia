import logging
import json

class NfcManager :

    def __init__(self,cube, tagtype):
        self.cube = cube
        self.last_id = None
        self.load_data()
	cube.register_tag_handler(tagtype,self.handle_nfc_tag)

    def handle_nfc_tag(self, ttype,data):
        logging.debug("Traitement du tag ID %s",data)
        if data in self.tags_data:
	    self.last_id = data
	    self.last_command = self.tags_data[data]['type']+":"+self.tags_data[data]['detail']
	    logging.debug("Tag : %s", self.last_command)
	    self.cube.tag_detection('VIDEO',self.last_command)
	else:
	    logging.info("ID inconnu : %s",data)

    def load_data(self):
        file = open('/home/pi/lecubemedia/src/protoxmpp/server/mod/tags.list')
        self.tags_data = json.load(file)
        logging.debug("Charge : %s",self.tags_data)
        file.close()


            
def init(cube, params):
    logging.info("NFC ID dispatching module initialization")
    tagtype = params.get("tagtype","NFC")
    cube.nfc_manager = NfcManager(cube,tagtype)
