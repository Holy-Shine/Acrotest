from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog,QMessageBox
from PyQt5.QtCore import Qt

from logic_qiandao_chose import LogicQiandaoChose


import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LogicQiandaoChose()
    login.show()
    sys.exit(app.exec_())