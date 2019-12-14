from MainTest.Logic_Main import LogicMain
from PyQt5 import QtWidgets
import sys
from Login.logic_login import logicLoginWin



def LoadLogin():
    app = QtWidgets.QApplication(sys.argv)
    window = logicLoginWin()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    LoadLogin()