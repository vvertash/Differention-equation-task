import random

    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
    from matplotlib.figure import Figure

    from PyQt4 import QtGui, QtCore


    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            QToolTip.setFont(QFont('SansSerif', 10))

            self.setToolTip('This is a <b>QWidget</b> widget')

            btn = QPushButton('Button', self)
            btn.resize(btn.sizeHint())
            btn.move(50, 50)

            self.setGeometry(300, 300, 300, 200)
            self.setWindowTitle('Tooltips')
            self.show()


    class MatplotlibWidget(QtGui.QWidget):
        def __init__(self, parent=None):
            super(MatplotlibWidget, self).__init__(parent)

            self.figure = Figure()
            self.canvas = FigureCanvasQTAgg(self.figure)

            self.axis = self.figure.add_subplot(111)

            self.layoutVertical = QtGui.QVBoxLayout(self)
            self.layoutVertical.addWidget(self.canvas)


    class ThreadSample(QtCore.QThread):
        newSample = QtCore.pyqtSignal(list)

        def __init__(self, parent=None):
            super(ThreadSample, self).__init__(parent)

        def run(self):
            randomSample = random.sample(range(0, 10), 10)

            self.newSample.emit(randomSample)


    class MyWindow(QtGui.QWidget):
        def __init__(self, parent=None):
            super(MyWindow, self).__init__(parent)

            self.pushButtonPlot = QtGui.QPushButton(self)
            self.pushButtonPlot.setText("Plot")
            self.pushButtonPlot.clicked.connect(self.on_pushButtonPlot_clicked)

            self.matplotlibWidget = MatplotlibWidget(self)

            self.layoutVertical = QtGui.QVBoxLayout(self)
            self.layoutVertical.addWidget(self.pushButtonPlot)
            self.layoutVertical.addWidget(self.matplotlibWidget)

            self.threadSample = ThreadSample(self)
            self.threadSample.newSample.connect(self.on_threadSample_newSample)
            self.threadSample.finished.connect(self.on_threadSample_finished)

        @QtCore.pyqtSlot()
        def on_pushButtonPlot_clicked(self):
            self.samples = 0
            self.matplotlibWidget.axis.clear()
            self.threadSample.start()

        @QtCore.pyqtSlot(list)
        def on_threadSample_newSample(self, sample):
            self.matplotlibWidget.axis.plot(sample)
            self.matplotlibWidget.canvas.draw()

        @QtCore.pyqtSlot()
        def on_threadSample_finished(self):
            self.samples += 1
            if self.samples <= 2:
                self.threadSample.start()


    if __name__ == "__main__":
        import sys

        app = QtGui.QApplication(sys.argv)
        app.setApplicationName('MyWindow')

        main = MyWindow()
        main.resize(666, 333)
        main.show()

        sys.exit(app.exec_())

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(700, 400)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    app = QApplication(sys.argv)
    ex = Example()