from MainTest.Logic_Main import LogicMain
from PyQt5 import QtWidgets
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogicMain()
    window.show()
    sys.exit(app.exec_())