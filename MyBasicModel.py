import enum
import random
import time
from abc import abstractmethod
leftSensorLenght = 1
leftMiddleSensorLenght = 3
middleSensorLenght = 4
rightMiddleSensorLenght = 3
rightSensorLenght = 1

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

class P(un):
    def __init__(self, x, y):
        self.motionVector = "up"
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

class sensor():
    def __init__(self, lenght):
        self.lenght = lenght
        #self.data = [0 for i in range(lenght)]
        self.distance = 1
    '''
    def getDistance(self):
        dist = 1
        while dist  <= self.lenght and self.data[dist - 1] == 0:
            dist += 1
        return dist
    '''
class sensorsController():
    def __init__(self):
        self.leftSensor = sensor(leftSensorLenght)
        self.leftMiddleSensor = sensor(leftMiddleSensorLenght)
        self.middleSensor = sensor(middleSensorLenght)
        self.rightMiddleSensor = sensor(rightMiddleSensorLenght)
        self.rightSensor = sensor(rightSensorLenght)
    def collectData(self, player : P):
        self.leftSensor.distance = 1
        self.leftMiddleSensor.distance = 1
        self.middleSensor.distance = 1
        self.rightMiddleSensor.distance = 1
        self.rightSensor.distance = 1
        for i in range(0, max(leftMiddleSensorLenght, leftSensorLenght, middleSensorLenght,
                             rightSensorLenght, rightMiddleSensorLenght)):
            if player.motionVector == "up":
                        if i < leftSensorLenght and map[i][j - 1] == 0:
                            self.leftSensor.distance += 1
                        if i < leftMiddleSensorLenght and map[i - 1][j - 1] == 0:
                            self.leftMiddleSensor.distance += 1
                        if i < middleSensorLenght and map[i - 1][j] == 0:
                            self.middleSensor.distance += 1
                        if i < rightMiddleSensorLenght and map[i - 1][j + 1] == 0:
                            self.rightMiddleSensor.distance += 1
                        if i < rightSensorLenght and map[i][j + 1] == 0:
                            self.rightSensor.distance += 1
            if player.motionVector == "down":
                        if i < leftSensorLenght and map[i][j + 1] == 0:
                            self.leftSensor.distance += 1
                        if i < leftMiddleSensorLenght and map[i + 1][j + 1] == 0:
                            self.leftMiddleSensor.distance += 1
                        if i < middleSensorLenght and map[i + 1][j] == 0:
                            self.middleSensor.distance += 1
                        if i < rightMiddleSensorLenght and map[i + 1][j - 1] == 0:
                            self.rightMiddleSensor.distance += 1
                        if i < rightSensorLenght and map[i][j - 1] == 0:
                            self.rightSensor.distance += 1
            if player.motionVector == "left":
                        if i < leftSensorLenght and map[i + 1][j] == 0:
                            self.leftSensor.distance += 1
                        if i < leftMiddleSensorLenght and map[i + 1][j - 1] == 0:
                            self.leftMiddleSensor.distance += 1
                        if i < middleSensorLenght and map[i][j - 1] == 0:
                            self.middleSensor.distance += 1
                        if i < rightMiddleSensorLenght and map[i - 1][j - 1] == 0:
                            self.rightMiddleSensor.distance += 1
                        if i < rightSensorLenght and map[i - 1][j] == 0:
                            self.rightSensor.distance += 1
            if player.motionVector == "right":
                if i < leftSensorLenght and map[i - 1][j] == 0:
                    self.leftSensor.distance += 1
                if i < leftMiddleSensorLenght and map[i - 1][j + 1] == 0:
                    self.leftMiddleSensor.distance += 1
                if i < middleSensorLenght and map[i][j + 1] == 0:
                    self.middleSensor.distance += 1
                if i < rightMiddleSensorLenght and map[i + 1][j + 1] == 0:
                    self.rightMiddleSensor.distance += 1
                if i < rightSensorLenght and map[i + 1][j] == 0:
                    self.rightSensor.distance += 1
if __name__=="__main__":
    map = []
    with open('map.txt') as file:
        file = file.read()
        q = file.replace(' ', '')
        q = q.replace('\n', '')
        for i in range(0, 10):
            map.append([])
            for j in range(0, 10):
                map[i].append(q[j + i * 10])
                #print(j + i * 10, q[j + i * 10])
    for i in range(0, 10):
        print(' ')
        for j in range(0, 10):
            print(map[i][j], end=''),