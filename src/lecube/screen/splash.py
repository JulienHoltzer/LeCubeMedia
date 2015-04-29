import thread
import logging
import socket
import fcntl
import struct
import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.camera import Camera
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.factory import Factory
from kivy.clock import Clock

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

class Logo(App):

    def build(self):
	layout = GridLayout(rows=3)
	layoutTop = FloatLayout(size=(100,300))
	layoutMid = FloatLayout(size=(100,300))
	layoutDown = FloatLayout(size=(100,300))
	
	logo = Image(source='images/logo.png',size_hint=(.45,.45),pos=(-50,400))
	
	carousel = Carousel(direction='right',loop=True,size_hint=(.9,.9),pos=(0,180),min_move=0.1)
        Clock.schedule_interval(carousel.load_next, 4)
	for i in range(1,6):
       		src = "images/nfc%s.png" % str(i)
        	image = Factory.AsyncImage(source=src, allow_stretch=True)
		carousel.add_widget(image)
		               
	blank = Label(text='', font_size = '25sp',pos=(-200,100))
	titre = Label(text='#LeCubeMedia',font_size='40sp',pos=(0,350))
	ip = Label(text=get_ip_address('wlan0'),font_size='25sp',pos=(250,350))
	console = Label(text='Forum SAME - Sophia Antipolis - 2 octobre 2014',font_size='25sp',pos=(0,0))

	layoutTop.add_widget(titre)
	layoutTop.add_widget(logo)
	layoutTop.add_widget(ip)
	layoutMid.add_widget(carousel)
	layoutMid.add_widget(blank)
	layoutDown.add_widget(console)

	layout.add_widget(layoutTop)
	layout.add_widget(layoutMid)
	layout.add_widget(layoutDown)
	
	return layout


def start_splash(title,cube) :
    logging.info(title)
    Logo().run()

def init(cube, params):
    thread.start_new_thread(start_splash,('LeCubeMedia Splash Screen', cube))
    #start_simulator()
