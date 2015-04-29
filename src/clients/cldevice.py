# -*- coding: utf-8 -*-
import logging
import thread
from optparse import OptionParser

import sleekxmpp


class DeviceClient(sleekxmpp.ClientXMPP) :

    def __init__(self, jid, password):
        print "User : %s"%jid
        super(DeviceClient, self).__init__(jid, password)
        logging.info("XMPP client launched : %s"%jid)
        #self.register_plugin('xep_0030')
        #self.register_plugin('xep_0059')
        #self.register_plugin('xep_0060')
        self.add_event_handler('session_start', self.start)
        #self.add_event_handler('presence', self.cb_presence)
        #self.add_event_handler('message', self.cb_message)

    def start(self, event):
        logging.info("XMPP : session started")
        self.get_roster()
        self.send_presence()

    def xmpp_setpresence(self,status):
        logging.info("XMPP : setting presence to - %s"%status)
        self.send_presence(pfrom=self.boundjid, pshow='chat',pstatus=status)


print "Device : Client XMPP connecte au Cube"
logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')

parser = OptionParser()
parser.add_option('-c', action="store", dest='cube_jid', default='cube@localhost')
parser.add_option('-j', action="store", dest='self_jid', default='device@localhost')
parser.add_option('-k', action="store", dest='self_pwd', default='device')
options, args = parser.parse_args()

print options.self_jid, options.self_pwd
client = DeviceClient(options.self_jid, options.self_pwd)
#thread.start_new_thread(client.start_loop, ())
print "hola"

if client.connect(use_tls=False):
    client.process(block=False)
    onemore = True
    while onemore :
        raw = raw_input('> ')
        if raw=='q' :
            break
        else :
            client.send_message(mto=options.cube_jid, mbody=raw)
    client.disconnect()
else:
    logging.info("Unable to connect.")

