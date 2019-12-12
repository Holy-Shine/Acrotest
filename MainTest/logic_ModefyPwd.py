
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QStackedWidget, QWidget
from PyQt5 import QtCore,QtGui,QtWidgets
from MainTest.ModifyPwd import Ui_Form

import Login.CheckUserName as modify

class LogicModifyPwd(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self,username):
        super(LogicModifyPwd, self).__init__()
        self.setupUi(self)
        self.username = username

        self.init()
        self.slot_init()

    def init(self):
        self.et_name.setEnabled(False)
        self.et_name.setText(self.username)
        self.et_pwdc.setEchoMode(QLineEdit.Password)
        self.et_pwdn.setEchoMode(QLineEdit.Password)
        self.et_pwdnc.setEchoMode(QLineEdit.Password)

    def slot_init(self):
        self.bt_back.clicked.connect(self.close)
        self.bt_confrim.clicked.connect(self.modify_pwd)
        self.bt_confrim.setShortcut(Qt.Key_Return)


    def modify_pwd(self):
        if(self.et_pwdn.text() == '' or self.et_pwdnc.text()=='' or self.et_pwdc.text()==''):
            QMessageBox.information(self, '提示', '请输入密码！', QMessageBox.Ok, QMessageBox.Ok)
        elif not(self.et_pwdnc.text() == self.et_pwdn.text()):
            QMessageBox.information(self, '提示', '两次新密码不一致！', QMessageBox.Ok, QMessageBox.Ok)
        else:
            flag = modify.Changpwd(newpwd=self.et_pwdnc.text(),
                                   oldpwd=self.et_pwdc.text(),
                                   username=self.username)
            if (flag):
                QMessageBox.information(self, '提示', '修改成功！', QMessageBox.Ok, QMessageBox.Ok)
                self.close()
            else:
                QMessageBox.information(self, '提示', '修改失败！', QMessageBox.Ok, QMessageBox.Ok)