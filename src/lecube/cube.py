import logging
import time
from Queue import Queue
import traceback

def  cube_exe_in_main(f):
    "Function decorator to ensure the execution of the function call into the main loop of the cube" 
    def g(*args, **kwargs):
        self = args[0]
        self.loop_tasks.put( (f,args,kwargs) )
    return g


class Cube :
    
    TAGSEP = ':'
    
    def __init__(self):
        logging.info("Cube instance is ready")
        self.tag_handler = {}
        self.tag_handler_unknown = self. __tag_handler_unknown
        self.loop_tasks = Queue()
        self.active_rid = ''

    def loop(self):
        "Main loop"

        cont = True
        while cont :
            cont = self.step()

    def step(self):
        func,p,k = self.loop_tasks.get()
        try :
            func(*p,**k)
        except:
            logging.exception('Failed to run task') # TBD : better error management
	    traceback.print_exc()
        self.loop_tasks.task_done()
        return True

    def register_tag_handler(self,tagtype,handler):
        self.tag_handler[tagtype] = handler
        
    def set_active_user(self,uid):
        # ensure client for uid/cube is running
        pass
        
    def set_active_remote(self,rid):
        self.active_rid=rid
        
# ###### Tags Management

    @cube_exe_in_main
    def tag_detection(self,device,data):
        """Called by the HWD when a new tag is detected.
        Expected format is TAGTYPE:TAGDATA
        Calls the TAGTYPE handler"""
    
        stag = data.split(Cube.TAGSEP,1)
        if len(stag)==2 :
            ttype,tdata = stag 
            th = self.tag_handler.get(ttype, self.tag_handler_unknown)
            th(ttype,tdata)

    def register_tag_handler(self,ttype,cb) : 
        self.tag_handler[ttype]=cb
            
# ###### internal methods 
    
    def __tag_handler_unknown(self,ttype, tdata):
        logging.info('Do  not know how to handle tag type %s - data = "%s"',
            ttype, tdata)
        

        

