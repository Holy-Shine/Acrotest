# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyPwd.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 282)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 30, 341, 181))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lb_name = QtWidgets.QLabel(self.groupBox_3)
        self.lb_name.setGeometry(QtCore.QRect(30, 20, 54, 12))
        self.lb_name.setObjectName("lb_name")
        self.et_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.et_name.setGeometry(QtCore.QRect(90, 20, 221, 20))
        self.et_name.setObjectName("et_name")
        self.lb_pwdc = QtWidgets.QLabel(self.groupBox_3)
        self.lb_pwdc.setGeometry(QtCore.QRect(30, 60, 54, 12))
        self.lb_pwdc.setObjectName("lb_pwdc")
        self.et_pwdc = QtWidgets.QLineEdit(self.groupBox_3)
        self.et_pwdc.setGeometry(QtCore.QRect(90, 60, 221, 20))
        self.et_pwdc.setObjectName("et_pwdc")
        self.lb_pwdn = QtWidgets.QLabel(self.groupBox_3)
        self.lb_pwdn.setGeometry(QtCore.QRect(30, 100, 54, 12))
        self.lb_pwdn.setObjectName("lb_pwdn")
        self.et_pwdn = QtWidgets.QLineEdit(self.groupBox_3)
        self.et_pwdn.setGeometry(QtCore.QRect(90, 100, 221, 20))
        self.et_pwdn.setObjectName("et_pwdn")
        self.lb_pwdnc = QtWidgets.QLabel(self.groupBox_3)
        self.lb_pwdnc.setGeometry(QtCore.QRect(30, 140, 54, 12))
        self.lb_pwdnc.setObjectName("lb_pwdnc")
        self.et_pwdnc = QtWidgets.QLineEdit(self.groupBox_3)
        self.et_pwdnc.setGeometry(QtCore.QRect(90, 140, 221, 20))
        self.et_pwdnc.setObjectName("et_pwdnc")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 220, 341, 51))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.bt_confrim = QtWidgets.QPushButton(self.groupBox_2)
        self.bt_confrim.setGeometry(QtCore.QRect(60, 10, 75, 31))
        self.bt_confrim.setObjectName("bt_confrim")
        self.bt_back = QtWidgets.QPushButton(self.groupBox_2)
        self.bt_back.setGeometry(QtCore.QRect(200, 10, 75, 31))
        self.bt_back.setObjectName("bt_back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户密码修改"))
        self.lb_name.setText(_translate("Form", "用户名"))
        self.lb_pwdc.setText(_translate("Form", "当前密码"))
        self.lb_pwdn.setText(_translate("Form", "修改密码"))
        self.lb_pwdnc.setText(_translate("Form", "确认修改"))
        self.bt_confrim.setText(_translate("Form", "确认"))
        self.bt_back.setText(_translate("Form", "返回"))

