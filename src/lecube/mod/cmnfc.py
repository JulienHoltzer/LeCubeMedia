# -*- coding: utf-8 -*-
import Tkinter as tk
import thread
import logging

class Application(tk.Frame):              
    def __init__(self, cube, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()
        self.cube = cube

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Tag Event',
            command=self.onTag)    
        self.quitButton.grid()            

        self.tagStr = tk.StringVar()
        self.userEntry = tk.Entry(self,textvariable=self.tagStr)
        self.tagStr.set('USER:giloux@localhost:giloux')
        self.userEntry.grid()

    def onTag(self):
        self.cube.tag_detection('NFC',self.userEntry.get())

def start_simulator(title,cube) :
    app = Application(cube)                       
    app.master.title(title)    
    app.mainloop()         

def init(cube, params):
    logging.info("Launching NFC simulator thread")
    thread.start_new_thread(start_simulator,('NFC Simulator', cube))
    #start_simulator()