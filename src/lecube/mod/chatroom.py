#-*- coding: utf-8 -*-

import logging
import thread
import traceback

import socket
import fcntl
import struct

import sleekxmpp


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
	s.fileno(),
	0x8915, # SIOCGIFADDR
	struct.pack('256s', ifname[:15])
    )[20:24])

# Un bot de chat pour gérer un salon commun ouvert à tous
# Il publie toutes les infos
class MUCBot(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password, room, nick):
	# enregistrement du bot
        sleekxmpp.ClientXMPP.__init__(self,jid, password)

	# sauvegarde des paramètres pour le salon commun
	self.room = room
	self.nick = nick

	# ce qui permet de faire du chat multi-utilisateur (muc)
	self.register_plugin('xep_0030')
        self.register_plugin('xep_0045')
	self.register_plugin('xep_0231')

	# démarrage de la session XMPP avec le serveur (donné par jid)
        self.add_event_handler('session_start', self.start)
	self.add_event_handler("groupchat_message", self.muc_message)
	self.add_event_handler("muc::%s::got_online" % self.room,
                               self.muc_online)


    def start_loop(self):
        if self.connect(use_tls=False):
            self.process(block=False)

    def start(self, event):
        self.get_roster()
        self.send_presence()
	self.plugin['xep_0045'].joinMUC(self.room,self.nick,wait=True)

	# signaler sa présence (et son IP)
	message = "Le Cube est démarré ! IP : %s, %s" % (get_ip_address('wlan1'),get_ip_address('eth0'))
	self.send_message(mto=self.room,mbody=message,mtype='groupchat')

    def muc_online(self, presence):
        if presence['muc']['nick'] != self.nick:
            self.send_message(mto=presence['from'].bare,
                              mbody="Salut %s !" % presence['muc']['nick'],mtype='groupchat')

    def muc_message(self, msg):
	if msg['mucnick'] != self.nick and self.nick in msg['body']:
	    m = self.Message()
	    m['to'] = msg['from'].bare
	    m['type'] = 'groupchat'
	    m['body'] = "Desole %s, je ne traite pas cette commande" % msg['mucnick']
	    m['html']['body'] = '<img src="%s" />' % 'http://www.google.com/images/errors/robot.png'
	    m.send()
	     

    def muc_photo(self, filename):
	m = self.Message()
	m['to'] = self.room
	m['type'] = 'groupchat'
	with open('/home/pi/images/'+filename+'.jpg','rb') as img_file:
	    img = img_file.read()
	if img:
	    cid = self['xep_0231'].set_bob(img, 'image/jpg')
	    m['body'] = "Nouvelle photo"
	    m['html']['body'] = '<img src="cid:%s" />' % cid
	    m.send()
    
    def traitement_message(self, data):
	action, value = data.split(':')
	if (value is not None) :
	    if (action == 'PHOTO'):
		self.muc_photo(value)
	else:
	    self.send_message(mto=self.room,mbody=data,mtype='groupchat')

class ChatroomManager :

    def __init__(self, cube, tagtype, user, password, room, nick):	
        self.cube=cube
	cube.register_tag_handler(tagtype,self.handle_chatroom_tag)
	try :
            user='%s/cube'%user
            self.active_muc = MUCBot(user,password,room,nick)
            self.disconnect_active()
            thread.start_new_thread(MUCBot.start_loop, (self.active_muc,))
        except :
            traceback.print_exc()

            
    def disconnect_active(self):
        if self.active_muc is not None :
            self.active_muc.disconnect(wait=True)


    def handle_chatroom_tag(self,ttype,data):
	# On demande de communiquer sur le chatroom
	# Traite le message
	self.active_muc.traitement_message(data)

def init(cube, params):
    logging.info("Cube chatroom module initialization")
    tagtype = params.get("tagtype","CHATROOM")
    user = params.get("user","no")
    pwd = params.get("password","no")
    room = params.get("room","no")
    nick = params.get("nick","no")
    cube.muc_manager = ChatroomManager(cube,tagtype,user,pwd,room,nick)
    
    
