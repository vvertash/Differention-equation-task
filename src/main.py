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
        #self.initUI()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
