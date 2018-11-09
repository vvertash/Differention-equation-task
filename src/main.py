import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from func import *
from math import fabs
import numpy as np


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Differential equation -y-x'
        self.width = 720
        self.height = 640
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=6)
        m.move(0, 0)

        # first textbox with x0
        self.textbox_x0 = QLineEdit(self)
        self.textbox_x0.move(520, 0)
        self.textbox_x0.resize(120, 50)

        # first label with x0
        self.label_x0 = QLabel(self)
        self.label_x0.setText("x0")
        self.label_x0.move(660, 20)

        # second textbox with y0
        self.textbox_y0 = QLineEdit(self)
        self.textbox_y0.move(520, 80)
        self.textbox_y0.resize(120, 50)

        # second label with y0
        self.label_y0 = QLabel(self)
        self.label_y0.setText("y0")
        self.label_y0.move(660, 100)

        # third textbox with x
        self.textbox_x = QLineEdit(self)
        self.textbox_x.move(520, 170)
        self.textbox_x.resize(120, 50)

        # third label with x
        self.label_x = QLabel(self)
        self.label_x.setText("x")
        self.label_x.move(660, 190)

        button = QPushButton('Apply', self)
        button.move(520, 250)
        button.resize(120, 50)

        # connect button to function on_click
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        x0 = float(self.textbox_x0.text())
        y0 = float(self.textbox_y0.text())
        x_max = int(self.textbox_x.text())
        m = PlotCanvas(self, width=5, height=6, x_max=x_max, y0=y0, x0=x0)
        m.move(0, 0)
        m.show()

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, x_max=10, y0=1, x0=0):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(x_max=x_max, x0=x0, y0=y0)

    def plot(self, x_max=10, x0=0, y0=1):

        # steps
        steps = 3

        # calculating graphs
        x_euler, y_euler = euler(steps, x_max=x_max, x0=x0, y0=y0)
        x_ivp, y_ivp = IVP(steps, x_max=x_max, x0=x0, y0=y0)
        x_euler_improved, y_euler_improved = euler_improved(steps, x_max=x_max, x0=x0, y0=y0)
        x_runge_kutta, y_runge_kutta = runge_kutta(steps, x_max=x_max, x0=x0, y0=y0)

        # local error calculating
        euler_local_error = [0.0]
        euler_improved_local_error = [0.0]
        runge_kutta_local_error = [0.0]
        for i in range(steps):
            euler_local_error.append(fabs(y_ivp[i] - y_euler[i]))
            euler_improved_local_error.append(fabs(y_ivp[i] - y_euler_improved[i]))
            runge_kutta_local_error.append(fabs(y_ivp[i] - y_runge_kutta[i]))

        # first plot with graphs
        ax = self.figure.add_subplot(311)
        ax.plot(x_euler, y_euler, label="euler")
        ax.plot(x_ivp, y_ivp, label="IVP")
        ax.plot(x_euler_improved, y_euler_improved, label="improved euler")
        ax.plot(x_runge_kutta, y_runge_kutta, label="runge kutta")
        ax.legend()

        # second plot with local errors
        ax = self.figure.add_subplot(312)
        ax.plot(x_euler, euler_local_error, label="euler local error")
        ax.plot(x_euler_improved, euler_improved_local_error, label="improved euler local error")
        ax.plot(x_runge_kutta, runge_kutta_local_error, label="runge_kutta local error")
        ax.legend()

        # global error calculating

        # start and finish
        start = 20
        finish = 100

        # array for x axis in global error graph
        array = []

        # global error calculating
        euler_global_error = []
        euler_improved_global_error = []
        runge_kutta_global_error = []

        for i in range(start, finish):
            array.append(i)

            # calculating every graph with 'i' accuracy
            x_euler, y_euler = euler(i, x_max=10, x0=0, y0=1)
            x_ivp, y_ivp = IVP(i, x_max=10, x0=0, y0=1)
            x_euler_improved, y_euler_improved = euler_improved(i, x_max=10, x0=0, y0=1)
            x_runge_kutta, y_runge_kutta = runge_kutta(i, x_max=10, x0=0, y0=1)

            # calculating global error
            euler_max_error = 0
            euler_improved_max_error = 0
            runge_kutta_max_error = 0

            for j in range(i):
                if fabs(y_ivp[j] - y_ivp[j]) > euler_max_error:
                    euler_max_error = fabs(y_ivp[j] - y_ivp[j])

                if fabs(y_ivp[j] - y_euler_improved[j]) > euler_improved_max_error:
                    euler_improved_max_error = fabs(y_ivp[j] - y_euler_improved[j])

                if fabs(y_ivp[j] - y_runge_kutta[j]) > runge_kutta_max_error:
                    runge_kutta_max_error = fabs(y_ivp[j] - y_runge_kutta[j])

            euler_global_error.append(euler_max_error)
            euler_improved_global_error.append(euler_improved_max_error)
            runge_kutta_global_error.append(runge_kutta_max_error)

        # third plot with global errors
        ax = self.figure.add_subplot(313)
        ax.plot(array, euler_global_error, label="euler global error")
        ax.plot(array, euler_improved_global_error, label="improved euler global error")
        ax.plot(array, runge_kutta_global_error, label="runge kutta global error")
        ax.legend()

        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
