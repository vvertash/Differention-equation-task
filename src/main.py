import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QVBoxLayout, QLabel)
from PyQt5.QtGui import QFont
#from PyQt5 import Qt
import pyqtgraph as pg
import numpy as np
import func

steps = 3

# calculating graphs
x_euler, y_euler = func.euler(steps)
x_exact, y_exact = func.IVP(steps)
x_euler_improved, y_euler_improved = func.euler_improved(steps)
x_runge_kutta, y_runge_kutta = func.runge_kutta(steps)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Apply', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(500, 300)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Tooltips')
        self.show()

class Window(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.view = view = pg.PlotWidget()
        self.curve = view.plot(name="Line")

        self.btn = QPushButton("Apply")
        self.btn.clicked.connect(self.random_plot)

        layout.addWidget(QLabel("Graphics"))
        layout.addWidget(self.view)
        layout.addWidget(self.btn)

    def random_plot(self):
        random_array = np.random.random_sample(20)
        self.curve.setData(random_array)


if __name__ == '__main__':
    #app = QApplication(sys.argv)
    #ex = Example()
    #sys.exit(app.exec_())
    app = QApplication([])
    w = Window()
    w.show()
    app.exec()