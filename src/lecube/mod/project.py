import logging


def handle_project_tag(ttype,data):
    logging.info("Project %s tagged"%data)
  

def init(cube, params):
    logging.info("Project management module initialization")
    tagtype = params.get("tagtype","prj")
    cube.register_tag_handler(tagtype,handle_project_tag)

    