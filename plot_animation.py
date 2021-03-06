import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import copy
import MyBasicModel
Writer = animation.writers['ffmpeg']
writer = Writer(fps=5, metadata=dict(artist='M.Yakovlev'), bitrate=1800)
class moveAnimation:
    def makeMoveAnimation(self, map, QM):
        wr = MyBasicModel.W(map, QM, 0)
        anim = wr.play(True)
        self.animate(map, anim)

    def animate(self, map, ANIM):
        print("anim begin")
        range1 = min(1000, len(ANIM))
        DOWN= []
        UP = []
        RIGHT = []
        LEFT = []
        for i in range (range1):
            x = ANIM[i][0]
            y = ANIM[i][1]
            DOWN.append(ANIM[i][2])
            UP.append(ANIM[i][3])
            RIGHT.append(ANIM[i][4])
            LEFT.append(ANIM[i][5])
            ANIM[i] = copy.deepcopy(map)
            ANIM[i][x][y] = 3
#        print(down[0])

        def update(i):
            matrice.set_array(ANIM[i])
            down.set_text('DOWN = %f' % DOWN[i])
            up.set_text('UP = %f' % UP[i])
            right.set_text('RIGHT = %f' % RIGHT[i])
            left.set_text('LEFT = %f' % LEFT[i])
        fig, ax = plt.subplots()
        down = ax.text(0.4, -0.1, '', transform=ax.transAxes)
        up = ax.text(0.4, 1.1, '', transform=ax.transAxes)
        right = ax.text(1.02, 0.5, '', transform=ax.transAxes)
        left = ax.text(-0.4, 0.5, '', transform=ax.transAxes)
        matrice = ax.matshow(ANIM[0])
        ani = animation.FuncAnimation(fig, update, frames=range1, interval=1000)
        ani.save('map5(extrahard)sensors.mp4', writer=writer)
        plt.show()
        plt.show(block=True)