import random
import time

class W:
    def __init__(self,n):
        self.n=n
        self.P=P(1,1,n)
        self.ens=[EN(3,3,n),EN(4,4,n)]
    def step(self):
        for i in self.ens:
            i.move()
        self.P.move()
    def pr(self):
        print('\n'*100)
        px,py=self.P.getxy()
        self.wmap=list([[0 for i in range(self.n)] for j in range(self.n)])
        self.wmap[py][px]=1
        for i in self.ens:
            ex,ey=i.getxy()
            self.wmap[ey][ex]=2
        for i in self.wmap:
            print(i)
    def play(self):
        px,py=self.P.getxy()
        bl=True
        for i in self.ens:
            ex,ey=i.getxy()
            bl=bl and (px,py)!=(ex,ey)
        iter=0
        while bl:
            time.sleep(1)
            wr.pr()
            self.step()
            px,py=self.P.getxy()
            bl=True
            for i in self.ens:
                ex,ey=i.getxy()
                bl=bl and (px,py)!=(ex,ey)
                print((px,py),(ex,ey))
            print('___')
            iter=iter+1
        print(iter)

class un:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getxy(self):
        return self.x, self.y

class P(un):
    def __init__(self,x,y,n):
        self.n=n
        un.__init__(self,x,y)
    def strtg(self):
        return 0,0
    def move(self):
        dx,dy=self.strtg()
        a=self.x+dx
        b=self.y+dy
        expr=((0<=a<self.n) and (0<=b<self.n))
        if expr:
            self.x=a
            self.y=b
class EN(un):
    def __init__(self,x,y,n):
        self.n=n
        un.__init__(self,x,y)
    def move(self):
        expr=False
        while not expr:
            a=self.x+random.choice([-1,0,1])
            b=self.y+random.choice([-1,0,1])
            expr=((0<=a<self.n) and (0<=b<self.n))
            if expr:
                self.x=a
                self.y=b

if __name__=="__main__":
    wr=W(7)
    wr.play()
    wr.pr()