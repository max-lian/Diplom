import random
import time

class W:
    def __init__(self,n, map):
        self.n=n
        self.P=P(4,2)
        self.map = map

class un:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getxy(self):
        return self.x, self.y

class sensor():
    def __init__(self, lenght):
        self.lenght = lenght

class P(un):
    def __init__(self, x, y):
        un.__init__(self, x, y)

    def strtg(self):
        return 0, 0

    def move(self):
        dx, dy = self.strtg()
        a = self.x + dx
        b = self.y + dy
        expr = ((0 <= a < self.n) and (0 <= b < self.n))
        if expr:
            self.x = a
            self.y = b

if __name__=="__main__":
    map = []
    with open('map.txt') as file:
        file = file.read()
        q = file.replace(' ', '')
        for i in range(0, 10):
            map.append([])
            for j in range(0, 10):
                map[i].append(q[j + i * 10])
    for i in range(0, 10):
        for j in range(0, 10):
            print(map[i][j], end=''),