dbg = None

def  exe_in_main(f):
    def g(*args, **kwargs):
        global dbg
        self = args[0]
        self.q.append( (f,args,kwargs) )
    return g

class cube :
   
    def __init__(self):
        self.q=[]

    def popone(self):
        s,a,k = self.q.pop()
        s(*a,**k)

    def toto(self,a):
        print "toto ",a

    @exe_in_main
    def tutu(self,a):
        print "tutu ",a

c = cube()
c.toto(1)
c.tutu(2)
c.popone()
