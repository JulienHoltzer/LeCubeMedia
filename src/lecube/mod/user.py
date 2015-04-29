import logging
import thread
import traceback

import sleekxmpp


class CubeUserClient(sleekxmpp.ClientXMPP) :
    def __init__(self, jid, password):
        super(CubeUserClient, self).__init__(jid, password)
        logging.info("User client launched:%s"%jid)
        #self.register_plugin('xep_0030')
        #self.register_plugin('xep_0059')
        #self.register_plugin('xep_0060')
        self.add_event_handler('session_start', self.start)
        #self.add_event_handler('presence', self.cb_presence)
        #self.add_event_handler('message', self.cb_message)

    def start_loop(self):
        if self.connect(use_tls=False):
            self.process(block=False)

    def start(self, event):
        logging.info("XMPP : session started")
        self.get_roster()
        self.send_presence()

    def xmpp_setpresence(self,status):
        logging.info("XMPP : setting presence to - %s"%status)
        self.send_presence(pfrom=self.boundjid, pshow='chat',pstatus=status)


class UserManager :

    def __init__(self, cube, tagtype):
        self.cube=cube
        self.active_user = None
        cube.register_tag_handler(tagtype,self.handle_user_tag)

    def handle_user_tag(self,ttype,data):
        try :
            user,pwd = data.split(':')
            logging.info("User %s tagged"%user)
            user='%s/cube'%user
            self.active_user = CubeUserClient(user,pwd)
            self.disconnect_active()
            thread.start_new_thread(CubeUserClient.start_loop, (self.active_user,))
        except :
            traceback.print_exc()

            
    def disconnect_active(self):
        if self.active_user is not None :
            self.active_user.disconnect(wait=True)

def init(cube, params):
    logging.info("User management module initialization")
    tagtype = params.get("tagtype","usr")
    cube.user_manager = UserManager(cube,tagtype)
    
    
