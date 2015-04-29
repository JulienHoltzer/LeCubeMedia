import logging


def handle_video_tag(ttype,data):
    logging.info("Vidéo à lancer : %s",data)
    

def init(cube, params):
    logging.info("Video launcher module initialization")
    tagtype = params.get("tagtype","vid")
    cube.register_tag_handler(tagtype,handle_video_tag)
    
