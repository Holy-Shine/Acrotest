# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyVerify.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 268)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 20, 351, 171))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lb_name = QtWidgets.QLabel(self.groupBox_3)
        self.lb_name.setGeometry(QtCore.QRect(30, 10, 54, 16))
        self.lb_name.setObjectName("lb_name")
        self.et_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.et_name.setGeometry(QtCore.QRect(110, 10, 221, 20))
        self.et_name.setObjectName("et_name")
        self.lb_vc = QtWidgets.QLabel(self.groupBox_3)
        self.lb_vc.setGeometry(QtCore.QRect(20, 50, 81, 20))
        self.lb_vc.setObjectName("lb_vc")
        self.et_vc = QtWidgets.QLineEdit(self.groupBox_3)
        self.et_vc.setGeometry(QtCore.QRect(110, 50, 221, 20))
        self.et_vc.setObjectName("et_vc")
        self.lb_vn = QtWidgets.QLabel(self.groupBox_3)
        self.lb_vn.setGeometry(QtCore.QRect(20, 90, 71, 20))
        self.lb_vn.setObjectName("lb_vn")
        self.et_vn = QtWidgets.QLineEdit(self.groupBox_3)
        self.et_vn.setGeometry(QtCore.QRect(110, 90, 221, 20))
        self.et_vn.setObjectName("et_vn")
        self.lb_vnc = QtWidgets.QLabel(self.groupBox_3)
        self.lb_vnc.setGeometry(QtCore.QRect(20, 130, 71, 20))
        self.lb_vnc.setObjectName("lb_vnc")
        self.et_vnc = QtWidgets.QLineEdit(self.groupBox_3)
        self.et_vnc.setGeometry(QtCore.QRect(110, 130, 221, 20))
        self.et_vnc.setObjectName("et_vnc")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 200, 351, 51))
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
        Form.setWindowTitle(_translate("Form", "二级密码修改"))
        self.lb_name.setText(_translate("Form", "用户名"))
        self.lb_vc.setText(_translate("Form", "当前二级密码"))
        self.lb_vn.setText(_translate("Form", "修改二级密码"))
        self.lb_vnc.setText(_translate("Form", "确认二级密码"))
        self.bt_confrim.setText(_translate("Form", "确认"))
        self.bt_back.setText(_translate("Form", "返回"))

