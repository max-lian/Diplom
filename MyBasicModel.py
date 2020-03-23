import enum
import random
import time
from abc import abstractmethod
import plot_epoch

#Параметры
leftSensorLenght = 1
leftMiddleSensorLenght = 3
middleSensorLenght = 4
rightMiddleSensorLenght = 3
rightSensorLenght = 1
N = 10

class Q:
    def __init__(self):
        self.gamma = 0.95
        self.alpha = 0.05
        self.state = {}

    def get_wp(self, plr):
        self.plr = plr

    def run_model(self, silent=1):
        self.plr.prev_state = self.plr.curr_state[:-2] + (self.plr.dx, self.plr.dy)
        self.plr.curr_state = tuple(self.plr.get_features()) + (self.plr.dx, self.plr.dy)

        r = self.plr.reward
        #print(r)
        if self.plr.prev_state not in self.state:
            self.state[self.plr.prev_state] = 0

        nvec = []
        for i in self.plr.actions:
            cstate = self.plr.curr_state[:-2] + (i[0], i[1])
            if cstate not in self.state:
                self.state[cstate] = 0
            nvec.append(self.state[cstate])
        nvec = max(nvec)
        self.state[self.plr.prev_state] = self.state[self.plr.prev_state] + self.alpha * (
                -self.state[self.plr.prev_state] + r + self.gamma * nvec)
        #print(self.state[self.plr.prev_state])
        #time.sleep(1)

class W:
    def __init__(self, map, QModel, eps):
        self.P=P(7,4,QModel, eps, map)
        self.map = map
        self.QM = QModel
        self.QM.get_wp(self.P)

    def step(self):
        self.P.move()

    def is_finished(self):
        px, py = self.P.getxy()
        end_bool = 0
        if map[px][py] == 1:
            end_bool = 1
        if map[px][py] == 2:
            end_bool = 2
        return end_bool

    def get_reward(self, end_bool):
        if end_bool == 0:
            self.P.reward = -0.5
        if end_bool == 1:
            self.P.reward = -1000
        if end_bool == 2:
            self.P.reward = 1000

    def play(self, silent=1, silent_run=1):
        end_bool = self.is_finished()
        iter = 0
        while end_bool == 0:
            try:
                self.P.sensorController.collectData(self.P)
            except IndexError:
                print("ERROR: ", self.P.getxy())
            if iter > 3000:
                print("iterations:", iter, end_bool, "sensors:", self.P.get_features(), "dx,dy", self.P.dx, self.P.dy,
                      "coords:", self.P.getxy())
                time.sleep(1)
            self.step()
            end_bool = self.is_finished()
            self.get_reward(end_bool)
            if silent_run:
                self.QM.run_model(silent)
            iter = iter + 1
            #if(iter % 100 == 0):
        if(self.P.eps == 0):
            print("end coords:", self.P.getxy())
        return iter

class un:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.actions = [(0, -1), (-1, 0),
                        (1, 0), (0, 1)]
    def getxy(self):
        return self.x, self.y

class P(un):
    def __init__(self, x, y, QM, eps, map):
        self.sensorController = sensorsController()
        self.QM = QM
        self.dx = 0
        self.dy = 0
        self.eps = eps
        self.map = map
        self.targetX = 0
        self.targetY = 0
        self.setTarget()
        un.__init__(self, x, y)
        self.prev_state = tuple(self.get_features()) + (self.dx, self.dy)
        self.curr_state = tuple(self.get_features()) + (self.dx, self.dy)

    def setTarget(self):
        for i in range(0, N):
            for j in range(0, N):
                if self.map[i][j] == 2:
                    self.targetX = i
                    self.targetY = j


    def get_dxdy(self):
        return self.dx, self.dy
    def get_features(self):
        features = []
        features.append(self.sensorController.leftSensor.distance)
        features.append(self.sensorController.leftMiddleSensor.distance)
        features.append(self.sensorController.middleSensor.distance)
        features.append(self.sensorController.rightMiddleSensor.distance)
        features.append(self.sensorController.rightSensor.distance)
        features.append(self.targetX - self.x)
        features.append(self.targetY - self.y)
        return features

    def strtg(self):
        randomnum = random.random()
        if  randomnum < self.eps:
            act = random.choice(self.actions)
            #print("random", randomnum, self.eps)
        else:
            name1 = tuple(self.get_features())
            best = [(0, 0), float('-inf')]
            for i in self.actions:
                namea = name1 + (i[0], i[1])
                if namea not in self.QM.state:
                    self.QM.state[namea] = 0
                if best[1] < self.QM.state[namea]:
                    best = [i, self.QM.state[namea]]
            act = best[0]
            #print("not random", randomnum, self.eps)
        return act

    def move(self):
        self.dx, self.dy = self.strtg()
        a = self.x + self.dx
        b = self.y + self.dy
        expr = ((0 <= a < N) and (0 <= b < N))
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
        x, y = player.getxy()
        dx, dy = player.get_dxdy()
        i = 1
        while i <= leftSensorLenght and map[x - dy*i][y + dx*i] != 1:
            self.leftSensor.distance += 1
            i += 1
        i = 1
        while i <= leftMiddleSensorLenght and map[x + (dx - dy) * i][y + (dx + dy) * i] != 1:
            self.leftMiddleSensor.distance += 1
            i += 1
        i = 1
        while i <= middleSensorLenght and map[x + dx * i][y + dy * i] != 1:
            self.middleSensor.distance += 1
            i += 1
        i = 1
        while i <= rightMiddleSensorLenght and map[x + (dx + dy) * i][y + (-dx + dy) * i] != 1:
            self.rightMiddleSensor.distance += 1
            i += 1
        i = 1
        while i <= rightSensorLenght and map[x + dy * i][y - dx * i] != 1:
            self.rightSensor.distance += 1
            i += 1

if __name__=="__main__":
    map = []
    with open('C:/Users/Max/Desktop/Materiali s uchebi/Diplom/map2.txt') as file:
        file = file.read()
        q = file.replace(' ', '')
        q = q.replace('\n', '')
        for i in range(0, N):
            map.append([])
            for j in range(0, N):
                map[i].append(int(q[j + i * N]))
                #print(j + i * 10, q[j + i * 10])
    for i in range(0, N):
        print(' ')
        for j in range(0, N):
            print(map[i][j], end=''),
    QModel = Q()
    plot = plot_epoch.epoch_graph()

    for i in range(30000):
        wr = W(map, QModel, 0.9)
        iter = wr.play(1)
        if i % 100 == 0:
            print(i, iter)
        #plot.plt_virt_game(W, QModel)
        plot.plt_append(iter)


    for i in range(100000):
        wr = W(map, QModel, 0.2)
        iter = wr.play(1)
        if i % 100 == 0:
            print(i, iter)
        #plot.plt_virt_game(W, QModel)
        plot.plt_append(iter)

    for i in QModel.state:
        print(i, QModel.state[i])

    for i in range(1000):
        wr = W(map, QModel, 0)
        iter = wr.play(1)
        print(i, iter)
        #plot.plt_virt_game(W, QModel)
        plot.plt_append(iter)

    plot.plot_graph()