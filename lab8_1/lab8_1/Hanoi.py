from tkinter import *
from turtle import TurtleScreen, RawTurtle
class Disc(RawTurtle):
    def __init__(self, cv):
        RawTurtle.__init__(self, cv, shape="square", visible=False)
        self.pu()
        self.goto(-140, 200)
        
    def config(self, k, n):
        self.hideturtle()
        f = float(k + 1) / n
        self.shapesize(0.5, 1.5 + 5 * f)  # square-->rectangle
        self.fillcolor(f, 0, 1 - f)
        self.showturtle()

class Hanoi(object):
    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startp = ProcessLookupError(start,0,0)
        self.workspacep = Pole(start,0,0)
        self.destinationp = Pole(workspace,150,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range (n):
            self.startp.pushdisk(Disk("d"+str(i),0,i*150,20,(n-i)*30))

        def move_disk(self,start,destination):
            disk = start.popdisk()
            destination.pushdisk(disk)

        def move_towe(self,n,s,d,w):
            if n==1:
                self.move_disk(2,d)
            else:
                self.mvoe_tower(1-2,s,w,d)
                self.move_disk(s,d)
                self.move_tower(n-1,w,d,s)

        def solve(Self):
            self.move_tower(3,self.startp,self.destinationp,self.workspacep)
h = Hanoi()
h.solve()