

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog,QMessageBox
from PyQt5.QtCore import Qt

from GUI.logic_login import logicLoginWin
from GUI.logic_main import logicMainWin
from GUI.logic_newUser import logicNewUser

import sys





if __name__ == '__main__':
    app = QApplication(sys.argv)

    login = logicLoginWin()
    login.show()

    if login.exec_()==QDialog.Accepted:
        
        mainWin = logicMainWin()
        mainWin.show()
        sys.exit(app.exec_())