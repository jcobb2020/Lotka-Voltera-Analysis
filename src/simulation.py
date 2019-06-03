from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class LotkaVoltera:
    h = 0.01
    a = 3
    b = 1
    c = 1
    d = 2
    x_herbivores = 100
    y_predators = 10
    predators = []  # y
    herbivores = []

    def __init__(self, h, a, b, c, d, herbivores, predators):
        self.h = h
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x_herbivores = herbivores
        self.y_predators = predators
        self.predators = []
        self.herbivores = []

    def x_prim(self, x, y):
        return (self.a - self.b * y) * x

    def y_prim(self, x, y):
        return (self.c * x - self.d) * y

    def count_next_y(self, x, y):
        k1 = self.h * self.y_prim(x, y)
        k2 = self.h * self.y_prim(x + (self.h / 2), y + k1 / 2)
        k3 = self.h * self.y_prim(x + (self.h / 2), y + k2 / 2)
        k4 = self.h * self.y_prim(x + self.h, y + k3)
        return y + self.h * (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    def count_next_x(self, x, y):
        k1 = self.h * self.x_prim(x, y)
        k2 = self.h * self.x_prim(x + k1 / 2, y + (self.h / 2))
        k3 = self.h * self.x_prim(x + k2 / 2, y + (self.h / 2))
        k4 = self.h * self.x_prim(x + k3, y + self.h)
        return x + self.h * (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    # x

    def simulate(self, steps):
        for i in range(steps):
            predators = self.count_next_y(self.x_herbivores, self.y_predators)
            herbivores = self.count_next_x(self.x_herbivores, self.y_predators)
            self.y_predators = predators
            self.x_herbivores = herbivores
            if i % 100 == 0:
                self.predators.append(self.y_predators)
                self.herbivores.append(self.x_herbivores)



# def simulate():
#     l_v = LotkaVoltera(0.01, 1, 0.5, 0.2, 3, 10, 5)
#     l_v.simulate(40000)
#     x_dim = [i for i in range(len(l_v.herbivores))]
#
#     fig = plt.figure()
#     ax1 = fig.add_subplot(111)
#     ax1.plot(x_dim, l_v.herbivores, c='b')
#     ax1.plot(x_dim, l_v.predators, c='r')
#     plt.show()

