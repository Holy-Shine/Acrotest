from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import  QMessageBox, QLineEdit
from PyQt5 import QtWidgets
from MainTest.ModifyVerify import Ui_Form

import Login.CheckUserName as modify

class LogicModifyVerify(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self,username):
        super(LogicModifyVerify, self).__init__()
        self.setupUi(self)
        self.username = username

        self.init()
        self.slot_init()


    def init(self):
        self.et_name.setEnabled(False)
        self.et_name.setText(self.username)
        self.et_vc.setEchoMode(QLineEdit.Password)
        self.et_vn.setEchoMode(QLineEdit.Password)
        self.et_vnc.setEchoMode(QLineEdit.Password)


    def slot_init(self):
        self.bt_back.clicked.connect(self.close)
        self.bt_confrim.clicked.connect(self.modify_verify)
        self.bt_confrim.setShortcut(Qt.Key_Return)

    def modify_verify(self):
        if (self.et_vc.text() == '' or self.et_vn.text() == '' or self.et_vnc.text() == ''):
            QMessageBox.information(self, '提示', '请输入密码！', QMessageBox.Ok, QMessageBox.Ok)
        elif not (self.et_vn.text() == self.et_vnc.text()):
            QMessageBox.information(self, '提示', '两次新密码不一致！', QMessageBox.Ok, QMessageBox.Ok)
        else:
            flag = modify.ChangVerify(newve=self.et_vnc.text(),
                                      oldve=self.et_vc.text())
            if (flag):
                QMessageBox.information(self, '提示', '修改成功！', QMessageBox.Ok, QMessageBox.Ok)
                self.close()
            else:
                QMessageBox.information(self, '提示', '修改失败！', QMessageBox.Ok, QMessageBox.Ok)