import logging
import json

def handle_nfc_tag(ttype,data):
    logging.debug("Traitement du tag ID %s",data)

def load_data(cube):
    file = open('/home/pi/lecubemedia/src/protoxmpp/server/mod/tags.list')
    cube.tags_data = json.load(file)
    logging.debug(cube.tags_data)
    file.close()

            
def init(cube, params):
    logging.info("NFC ID dispatching module initialization")
    tagtype = params.get("tagtype","nfc")
    cube.register_tag_handler(tagtype,handle_nfc_tag)
    
    
