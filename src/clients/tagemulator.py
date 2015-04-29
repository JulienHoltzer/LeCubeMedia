# -*- coding: utf-8 -*-
import Tkinter as tk
import logging
import thread

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Tag Event',
            command=self.onTag)    
        self.quitButton.grid()            

        self.tagStr = tk.StringVar()
        self.userEntry = tk.Entry(self,textvariable=self.tagStr)
        self.tagStr.set('USER:giloux@localhost:giloux')
        self.userEntry.grid()

    def onTag(self):
        logging.info(self.userEntry.get())
        print "yay"
        #TBD

def start_simulator(a) :
    app = Application()                       
    app.master.title('Simple Tag Device Emulator')    
    app.mainloop()         

logging.basicConfig(level=logging.DEBUG)
logging.info("Tag device emulator launched")
thread.start_new_thread(start_simulator,('a', ))
s = raw_input('[Return] to stop emulator')
#start_simulator()
