# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QMessageBox
import sys
class UI_login(object):
    def setupUi(self, Form):
        self.obj = Form
        Form.setObjectName("Form")
        Form.resize(300, 200)
        Form.setMinimumSize(QtCore.QSize(300, 200))
        Form.setMaximumSize(QtCore.QSize(300, 200))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 31, 16))
        self.label_2.setObjectName("label_2")
        self.checkbox_save = QtWidgets.QCheckBox(Form)
        self.checkbox_save.setGeometry(QtCore.QRect(60, 120, 141, 16))
        self.checkbox_save.setObjectName("checkbox_save")
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(60, 150, 75, 23))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_yes = QtWidgets.QPushButton(Form)
        self.btn_yes.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.btn_yes.setObjectName("btn_yes")
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_pwd = QtWidgets.QLineEdit(Form)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "员工登录"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_2.setText(_translate("Form", "密码："))
        self.checkbox_save.setText(_translate("Form", "记住用户名和密码"))
        self.btn_cancel.setText(_translate("Form", "清空"))
        self.btn_yes.setText(_translate("Form", "确定"))


