from MainTest.Logic_Main import LogicMain
import os,sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogicMain()
    window.show()
    sys.exit(app.exec_())