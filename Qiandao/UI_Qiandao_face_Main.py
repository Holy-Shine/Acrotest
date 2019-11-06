# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qiandao_face_Main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from UI_Qiandao_chaxun import UI_Qiandao_chaxun

class UI_Qiandao_face(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(567, 426)
        Form.setToolTipDuration(-1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 80, 231, 191))
        self.label.setText("")
        self.label.setObjectName("label")
        self.bt_qiandao_confrim = QtWidgets.QPushButton(Form)
        self.bt_qiandao_confrim.setGeometry(QtCore.QRect(130, 320, 101, 51))
        self.bt_qiandao_confrim.setObjectName("bt_qiandao_confrim")
        self.bt_trackback = QtWidgets.QPushButton(Form)
        self.bt_trackback.setGeometry(QtCore.QRect(330, 320, 101, 51))
        self.bt_trackback.setObjectName("bt_trackback")
        self.lb_name = QtWidgets.QLabel(Form)
        self.lb_name.setGeometry(QtCore.QRect(60, 80, 54, 12))
        self.lb_name.setObjectName("lb_name")
        self.lb_date = QtWidgets.QLabel(Form)
        self.lb_date.setGeometry(QtCore.QRect(60, 130, 54, 12))
        self.lb_date.setObjectName("lb_date")
        self.lb_coach = QtWidgets.QLabel(Form)
        self.lb_coach.setGeometry(QtCore.QRect(60, 180, 54, 12))
        self.lb_coach.setObjectName("lb_coach")
        self.lb_rest = QtWidgets.QLabel(Form)
        self.lb_rest.setGeometry(QtCore.QRect(60, 240, 54, 12))
        self.lb_rest.setObjectName("lb_rest")
        self.lb_nameinfo = QtWidgets.QLabel(Form)
        self.lb_nameinfo.setGeometry(QtCore.QRect(160, 80, 54, 12))
        self.lb_nameinfo.setObjectName("lb_nameinfo")
        self.lb_dateinfo = QtWidgets.QLabel(Form)
        self.lb_dateinfo.setGeometry(QtCore.QRect(160, 130, 54, 12))
        self.lb_dateinfo.setObjectName("lb_dateinfo")
        self.lb_coach_info = QtWidgets.QLabel(Form)
        self.lb_coach_info.setGeometry(QtCore.QRect(160, 180, 54, 12))
        self.lb_coach_info.setObjectName("lb_coach_info")
        self.lb_restinfo = QtWidgets.QLabel(Form)
        self.lb_restinfo.setGeometry(QtCore.QRect(160, 240, 54, 12))
        self.lb_restinfo.setObjectName("lb_restinfo")
        self.lb_toplabel = QtWidgets.QLabel(Form)
        self.lb_toplabel.setGeometry(QtCore.QRect(220, 30, 101, 16))
        self.lb_toplabel.setTextFormat(QtCore.Qt.AutoText)
        self.lb_toplabel.setObjectName("lb_toplabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bt_qiandao_confrim.setText(_translate("Form", "确认签到"))
        self.bt_trackback.setText(_translate("Form", "返回"))
        self.lb_name.setText(_translate("Form", "学生姓名"))
        self.lb_date.setText(_translate("Form", "上课时间"))
        self.lb_coach.setText(_translate("Form", "教练姓名"))
        self.lb_rest.setText(_translate("Form", "剩余次数"))
        self.lb_nameinfo.setText(_translate("Form", "l"))
        self.lb_dateinfo.setText(_translate("Form", "l"))
        self.lb_coach_info.setText(_translate("Form", "l"))
        self.lb_restinfo.setText(_translate("Form", "l"))
        self.lb_toplabel.setText(_translate("Form", "学 生 签 到 界 面"))

