from simulation import LotkaVoltera
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        title = "Lotka Voltera"
        top = 400
        left = 400
        width = 900
        height = 500


        self.h = 0.01
        self.a = 3
        self.b = 1
        self.c = 1
        self.d = 2
        self.x_herbivores = 100
        self.y_predators = 10
        self.steps = 50000

        self.a_slider = QSlider(Qt.Horizontal, self)
        self.a_slider.move(250, 400)
        self.a_slider.setMinimum(0)
        self.a_slider.setMaximum(30)
        self.a_slider.setSingleStep(0.1)
        self.a_slider.setTickInterval(1)
        self.a_slider.setValue(11)
        self.a_slider.setTickPosition(QSlider.TicksBelow)

        self.b_slider = QSlider(Qt.Horizontal, self)
        self.b_slider.move(400, 400)
        self.b_slider.setMinimum(0)
        self.b_slider.setMaximum(30)
        self.b_slider.setSingleStep(0.1)
        self.b_slider.setTickInterval(1)
        self.b_slider.setValue(4)
        self.b_slider.setTickPosition(QSlider.TicksBelow)

        self.c_slider = QSlider(Qt.Horizontal, self)
        self.c_slider.move(250, 450)
        self.c_slider.setMinimum(0)
        self.c_slider.setMaximum(10)
        self.c_slider.setSingleStep(0.1)
        self.c_slider.setTickInterval(1)
        self.c_slider.setValue(1)
        self.c_slider.setTickPosition(QSlider.TicksBelow)

        self.d_slider = QSlider(Qt.Horizontal, self)
        self.d_slider.move(400, 450)
        self.d_slider.setMinimum(0)
        self.d_slider.setMaximum(100)
        self.d_slider.setSingleStep(0.1)
        self.d_slider.setTickInterval(1)
        self.d_slider.setValue(4)
        self.d_slider.setTickPosition(QSlider.TicksBelow)

        self.x_slider = QSlider(Qt.Horizontal, self)
        self.x_slider.move(550, 400)
        self.x_slider.setMinimum(0)
        self.x_slider.setMaximum(100)
        self.x_slider.setSingleStep(0.1)
        self.x_slider.setTickInterval(1)
        self.x_slider.setValue(10)
        self.x_slider.setTickPosition(QSlider.TicksBelow)

        self.y_slider = QSlider(Qt.Horizontal, self)
        self.y_slider.move(550, 450)
        self.y_slider.setMinimum(0)
        self.y_slider.setMaximum(100)
        self.y_slider.setSingleStep(0.1)
        self.y_slider.setTickInterval(1)
        self.y_slider.setValue(10)
        self.y_slider.setTickPosition(QSlider.TicksBelow)

        self.steps_slider = QSlider(Qt.Horizontal, self)
        self.steps_slider.move(700, 400)
        self.steps_slider.setMinimum(0)
        self.steps_slider.setMaximum(1000)
        self.steps_slider.setSingleStep(0.1)
        self.steps_slider.setTickInterval(1)
        self.steps_slider.setValue(10)
        self.steps_slider.setTickPosition(QSlider.TicksBelow)


        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.button = QPushButton("plot", self)
        self.button.move(700, 460)
        self.button.clicked.connect(lambda: self.simulate(steps=self.steps))

        self.help_button = QPushButton("help", self)
        self.help_button.move(700, 420)
        self.help_button.clicked.connect(self.display_help)

        self.a = self.a_slider.value() / 10
        self.b = self.b_slider.value() / 10
        self.c = self.c_slider.value() / 10
        self.d = self.d_slider.value() / 10
        self.x_herbivores = self.x_slider.value()
        self.y_predators = self.y_slider.value()

        self.simulation = LotkaVoltera(self.h, self.a, self.b, self.c, self.d, self.x_herbivores, self.y_predators)
        self.canvas = Canvas(self, sim=self.simulation, width=9, height=4)
        self.canvas.move(0, 0)

        self.a_slider.valueChanged.connect(self.value_changed)
        self.b_slider.valueChanged.connect(self.value_changed)
        self.c_slider.valueChanged.connect(self.value_changed)
        self.d_slider.valueChanged.connect(self.value_changed)
        self.x_slider.valueChanged.connect(self.value_changed)
        self.y_slider.valueChanged.connect(self.value_changed)
        self.steps_slider.valueChanged.connect(self.change_steps)


        self.la = QLabel(self)
        self.lb = QLabel(self)
        self.lc = QLabel(self)
        self.ld = QLabel(self)
        self.l_steps = QLabel(self)

        self.la.move(50, 390)
        self.lb.move(50, 410)
        self.lc.move(50, 430)
        self.ld.move(50, 450)
        self.l_steps.move(50, 470)
        self.display_params()

    def change_steps(self):
        self.steps = self.steps_slider.value() * 1000
        self.display_params()

    def display_help(self):
        message = """a – herbivore growth rate,
                  b – herbivore death rate (predator caused)
                  c – predator growth rate,
                  d – predator death rate """
        QMessageBox.about(self, "help", message)

    def display_params(self):
        self.la.setText("A= " + str(self.a) + " B=" + str(self.b))
        self.lb.setText("C=" + str(self.c) + " D=" + str(self.d))
        self.lc.setText("herbivores= " + str(self.x_herbivores))
        self.ld.setText("predators=" + str(self.y_predators))
        self.l_steps.setText("steps= " + str(self.steps))


    def value_changed(self):
        self.a = self.a_slider.value()/10
        self.b = self.b_slider.value()/10
        self.c = self.c_slider.value()/10
        self.d = self.d_slider.value()/10
        self.x_herbivores = self.x_slider.value()
        self.y_predators = self.y_slider.value()
        self.display_params()
        self.simulate()

    def simulate(self, steps=50000):
        new_simulation = LotkaVoltera(self.h, self.a, self.b, self.c, self.d, self.x_herbivores, self.y_predators)
        self.canvas.replot(new_simulation, steps)


class Canvas(FigureCanvas):
    def __init__(self, parent=None, sim=LotkaVoltera(0.01, 0.3, 0.05, 0.1, 3, 100, 0), width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
#        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.simulation = sim
        # self.fig, self.ax = plt.subplots()
        self.ax = self.figure.add_subplot(111)
        self.plot()

    def plot(self):
        simulation = self.simulation
        simulation.simulate(120000)
        x_dim = [i for i in range(len(simulation.herbivores))]
        self.ax.plot(x_dim, simulation.herbivores, c='b')
        self.ax.plot(x_dim, simulation.predators, c='r')

    def replot(self, simulation, steps):
        simulation.simulate(steps)
        self.ax.cla()
        # self.ax.clear()
        x_dim = [i for i in range(len(simulation.herbivores))]
        self.ax.plot(x_dim, simulation.herbivores, c='b')
        self.ax.plot(x_dim, simulation.predators, c='r')
        self.ax.figure.canvas.draw()


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
