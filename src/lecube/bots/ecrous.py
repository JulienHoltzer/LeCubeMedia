#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import getpass

import sleekxmpp

# Python versions before 3.0 do not use UTF-8 encoding
# by default. To ensure that Unicode is handled properly
# throughout SleekXMPP, we will set the default encoding
# ourselves to UTF-8.
if sys.version_info < (3, 0):
    reload(sys)
    sys.setdefaultencoding('utf8')
else:
    raw_input = input


class EcrousBot(sleekxmpp.ClientXMPP):

    """
	Un bot pour gérer les écrous du Lab Aix Bidouille
    """

    def __init__(self, jid, password):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        # The session_start event will be triggered when
        # the bot establishes its connection with the server
        # and the XML streams are ready for use. We want to
        # listen for this event so that we we can initialize
        # our roster.
        self.add_event_handler("session_start", self.start)

        # The message event is triggered whenever a message
        # stanza is received. Be aware that that includes
        # MUC messages and error messages.
        self.add_event_handler("message", self.message)


    def start(self, event):
        """
        Process the session_start event.

        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.

        Arguments:
            event -- An empty dictionary. The session_start
                     event does not provide any additional
                     data.
        """
        self.send_presence()
        self.get_roster()

    def message(self, msg):

        """
        Process incoming message stanzas. Be aware that this also
        includes MUC messages and error messages. It is usually
        a good idea to check the messages's type before processing
        or sending replies.

        Arguments:
            msg -- The received message stanza. See the documentation
                   for stanza objects and the Message stanza to see
                   how it may be used.
        """
        if msg['type'] in ('chat', 'normal'):
	    # détecter une commande connue
	    


	    # transmission au banquier
	    bmsg = "Reçu de "+msg['from'].bare+" : "+ msg['body']
	
	    #self.send_message(mto=self.params.get("banquier"), mbody=bmsg)	    
	    self.send_message(mto="julien@pobot.org", mbody=bmsg)	    

	    # répondre 
            rep = "Merci " + msg['from'].user + ", je transmets au banquier"

            msg.reply(rep).send()


def init(cube, params):

    # Le bot écrous n'utilise pas le cube (pour l'instant)

    xmpp = EcrousBot(params.get("jid","test@pobot.org"),params.get("pwd","test"))
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0004') # Data Forms
    xmpp.register_plugin('xep_0060') # PubSub
    xmpp.register_plugin('xep_0199') # XMPP Ping

    # Infos particulières passées dans le fichier de configuration
    xmpp.params = params


    # If you are working with an OpenFire server, you may need
    # to adjust the SSL version used:
    # xmpp.ssl_version = ssl.PROTOCOL_SSLv3

    # If you want to verify the SSL certificates offered by a server:
    # xmpp.ca_certs = "path/to/ca/cert"

    # Connect to the XMPP server and start processing XMPP stanzas.
    if xmpp.connect(use_tls=False):
        # If you do not have the dnspython library installed, you will need
        # to manually specify the name of the server if it does not match
        # the one in the JID. For example, to use Google Talk you would
        # need to use:
        #
        # if xmpp.connect(('talk.google.com', 5222)):
        #     ...
        xmpp.process(block=False)
        print("Ecrousbot : done")
    else:
        print("Ecrousbot : unable to connect.")
