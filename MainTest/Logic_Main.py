from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from MainTest import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
import os,sys


class LogicMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LogicMain, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogicMain()
    window.show()
    sys.exit(app.exec_())
