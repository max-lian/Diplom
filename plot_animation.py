import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy
import MyBasicModel
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='M.Yakovlev'), bitrate=1800)
class moveAnimation:
    def makeMoveAnimation(self, map, QM):
        wr = MyBasicModel.W(map, QM, 0)
        anim = wr.play(True)
        self.animate(map, anim)

    def animate(self, map, ANIM):
        print("anim begin")
        range1 = min(300, len(ANIM))
        for i in range (range1):
            x = ANIM[i][0]
            y = ANIM[i][1]
            ANIM[i] = copy.deepcopy(map)
            ANIM[i][x][y] = 3

        def update(i):
            matrice.set_array(ANIM[i])
        fig, ax = plt.subplots(1, 1)
        matrice = ax.matshow(ANIM[0])
        ani = animation.FuncAnimation(fig, update, frames=range1, interval=100)
        ani.save('test.mp4', writer=writer)
        plt.show()
        plt.show(block=True)