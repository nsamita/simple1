from tkinter import *
from turtle import TurtleScreen, RawTurtle
class Disc(RawTurtle):
    def __init__(self, cv):
        RawTurtle.__init__(self, cv, shape="square", visible=False)
        self.pu()
        self.goto(-140, 200) #gotoja
        
    def config(self, k, n):
        self.hideturtle()
        f = float(k + 1) / n
        self.shapesize(0.5, 1.5 + 5 * f)  # square-->rectangle
        self.fillcolor(f, 0, 1 - f)
        self.showturtle()

class Pole(list): # pole here ######
    def __init__(self, x):
        self.x = x

    def push(self, d):
        d.setx(self.x)
        d.sety(-70 + 10 * len(self))
        self.append(d)

    def pop(self, y=90):
        d = list.pop(self)
        d.sety(y)
        return d


class HanoiEngine:
    def __init__(self, canvas, nrOfDiscs, speed, moveCntDisplay=None):
        self.ts = canvas
        self.ts.tracer(False)
        # setup scene
        self.designer = RawTurtle(canvas, shape="square")
        self.designer.penup()
        self.designer.shapesize(0.5, 21)
        self.designer.goto(0, -80);
        self.designer.stamp()
        self.designer.shapesize(7, 0.5)
        self.designer.fillcolor('yellow')
        for x in -140, 0, 140:
            self.designer.goto(x, -5);
            self.designer.stamp()

        self.nrOfDiscs = nrOfDiscs
        self.speed = speed
        self.moveDisplay = moveCntDisplay
        self.running = False
        self.moveCnt = 0
        self.discs = [Disc(canvas) for i in range(10)]
        self.towerA = Pole(-140)
        self.towerB = Pole(0)
        self.towerC = Pole(140)
        self.ts.tracer(True)

    def setspeed(self):
        for disc in self.discs: disc.speed(self.speed)

    def hanoi(self, n, src, dest, temp):
        if n > 0:
            for x in self.hanoi(n - 1, src, temp, dest): yield None
            yield self.move(src, dest)
            for x in self.hanoi(n - 1, temp, dest, src): yield None

    def move(self, src_tower, dest_tower):
        dest_tower.push(src_tower.pop())
        self.moveCnt += 1
        self.moveDisplay(self.moveCnt)

    def reset(self):
        self.ts.tracer(False)
        self.moveCnt = 0
        self.moveDisplay(0)
        for t in self.towerA, self.towerB, self.towerC:
            while t != []: t.pop(200)
        for k in range(self.nrOfDiscs - 1, -1, -1):
            self.discs[k].config(k, self.nrOfDiscs)
            self.towerA.push(self.discs[k])
        self.ts.tracer(True)
        self.HG = self.hanoi(self.nrOfDiscs,
                             self.towerA, self.towerC, self.towerB)

    def run(self):
        self.running = True
        try:
            while self.running:
                result = self.step()
            return result  # True iff done
        except StopIteration:  # game over
            return True

    def step(self):
        try:
            next(self.HG)
            return 2 ** self.nrOfDiscs - 1 == self.moveCnt
        except TclError:
            return False

    def stop(self):
        self.running = False

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