# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qiandao_choose_info.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 304)
        self.lb_pic = QtWidgets.QLabel(Form)
        self.lb_pic.setGeometry(QtCore.QRect(240, 50, 111, 131))
        self.lb_pic.setText("")
        self.lb_pic.setObjectName("lb_pic")
        self.lb_name = QtWidgets.QLabel(Form)
        self.lb_name.setGeometry(QtCore.QRect(50, 50, 54, 12))
        self.lb_name.setObjectName("lb_name")
        self.lb_date = QtWidgets.QLabel(Form)
        self.lb_date.setGeometry(QtCore.QRect(50, 90, 54, 12))
        self.lb_date.setObjectName("lb_date")
        self.lb_jiaolian = QtWidgets.QLabel(Form)
        self.lb_jiaolian.setGeometry(QtCore.QRect(50, 130, 54, 12))
        self.lb_jiaolian.setObjectName("lb_jiaolian")
        self.lb_rest = QtWidgets.QLabel(Form)
        self.lb_rest.setGeometry(QtCore.QRect(50, 170, 54, 20))
        self.lb_rest.setObjectName("lb_rest")
        self.ib_nameinfo = QtWidgets.QLabel(Form)
        self.ib_nameinfo.setGeometry(QtCore.QRect(130, 50, 54, 12))
        self.ib_nameinfo.setObjectName("ib_nameinfo")
        self.lb_dateinfo = QtWidgets.QLabel(Form)
        self.lb_dateinfo.setGeometry(QtCore.QRect(130, 90, 54, 12))
        self.lb_dateinfo.setObjectName("lb_dateinfo")
        self.lb_coachinfo = QtWidgets.QLabel(Form)
        self.lb_coachinfo.setGeometry(QtCore.QRect(130, 130, 54, 12))
        self.lb_coachinfo.setObjectName("lb_coachinfo")
        self.lb_restinfo = QtWidgets.QLabel(Form)
        self.lb_restinfo.setGeometry(QtCore.QRect(130, 170, 54, 12))
        self.lb_restinfo.setObjectName("lb_restinfo")
        self.bt_confrim = QtWidgets.QPushButton(Form)
        self.bt_confrim.setGeometry(QtCore.QRect(70, 230, 75, 41))
        self.bt_confrim.setObjectName("bt_confrim")
        self.bt_back = QtWidgets.QPushButton(Form)
        self.bt_back.setGeometry(QtCore.QRect(230, 230, 75, 41))
        self.bt_back.setObjectName("bt_back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_name.setText(_translate("Form", "姓名"))
        self.lb_date.setText(_translate("Form", "上课日期"))
        self.lb_jiaolian.setText(_translate("Form", "教练"))
        self.lb_rest.setText(_translate("Form", "剩余次数"))
        self.ib_nameinfo.setText(_translate("Form", "l"))
        self.lb_dateinfo.setText(_translate("Form", "l"))
        self.lb_coachinfo.setText(_translate("Form", "l"))
        self.lb_restinfo.setText(_translate("Form", "l"))
        self.bt_confrim.setText(_translate("Form", "确认签到"))
        self.bt_back.setText(_translate("Form", "返回"))

