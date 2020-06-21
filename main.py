import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget, QToolTip, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from MainWindow import Ui_MainWindow


class canvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=20, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(canvas, self).__init__(fig)




class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)







def main():
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
