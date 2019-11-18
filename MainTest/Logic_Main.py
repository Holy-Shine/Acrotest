from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from MainTest import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
import os,sys


class LogicMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LogicMain, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出本系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogicMain()
    window.show()
    sys.exit(app.exec_())
