import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from func import *


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

        self.textbox = QLineEdit(self)
        self.textbox.move(520, 0)
        self.textbox.resize(120, 50)

        self.label = QLabel(self)
        self.label.setText("x0")
        self.label.move(660, 20)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(520, 80)
        self.textbox1.resize(120, 50)

        self.label1 = QLabel(self)
        self.label1.setText("y0")
        self.label1.move(660, 100)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(520, 170)
        self.textbox2.resize(120, 50)

        self.label3 = QLabel(self)
        self.label3.setText("x")
        self.label3.move(660, 190)

        button = QPushButton('Apply', self)
        button.move(520, 250)
        button.resize(120, 50)

        # connect button to function on_click
        button.clicked.connect(self.on_click)

        self.show()

        @pyqtSlot()
        def on_click(self):
            x0 = float(self.textbox.text())
            y0 = float(self.textbox1.text())
            x_max = int(self.textbox2.text())
            #m = PlotCanvas(self, width=5, height=6, x_max=x_max, y0=y0, x0=x0)
            #m.move(0, 0)
            #m.show()

class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, x_max=10, y0=1, x0=0):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(x_max=x_max, x0=x0, y0=y0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
