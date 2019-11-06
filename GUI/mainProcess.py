

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog,QMessageBox
from PyQt5.QtCore import Qt

from logic_login import logicLoginWin
from logic_main import logicMainWin
from logic_newUser import logicNewUser

import sys





if __name__ == '__main__':
    app = QApplication(sys.argv)

    login = logicLoginWin()
    login.show()

    if login.exec_()==QDialog.Accepted:
        mainWin = logicMainWin()
        win_newuser  = logicNewUser()
        win_newuser.setWindowModality(Qt.ApplicationModal)
        btn = mainWin.btn_add_user
        btn.clicked.connect(win_newuser.show)

        mainWin.show()
        sys.exit(app.exec_())