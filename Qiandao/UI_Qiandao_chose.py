# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qiandao_chose.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiQiandaoChose(object):
    def setupUi(self, UiQiandaoChose):
        UiQiandaoChose.setObjectName("UiQiandaoChose")
        UiQiandaoChose.resize(413, 151)
        UiQiandaoChose.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.bt_back = QtWidgets.QPushButton(UiQiandaoChose)
        self.bt_back.setGeometry(QtCore.QRect(230, 100, 81, 41))
        self.bt_back.setObjectName("bt_back")
        self.bt_confrim = QtWidgets.QPushButton(UiQiandaoChose)
        self.bt_confrim.setGeometry(QtCore.QRect(90, 100, 81, 41))
        self.bt_confrim.setObjectName("bt_confrim")
        self.frame = QtWidgets.QFrame(UiQiandaoChose)
        self.frame.setGeometry(QtCore.QRect(20, 10, 361, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cb_year = QtWidgets.QComboBox(self.frame)
        self.cb_year.setGeometry(QtCore.QRect(80, 20, 71, 22))
        self.cb_year.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_year.setObjectName("cb_year")
        self.cb_day = QtWidgets.QComboBox(self.frame)
        self.cb_day.setGeometry(QtCore.QRect(80, 50, 71, 22))
        self.cb_day.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_day.setObjectName("cb_day")
        self.lb_year = QtWidgets.QLabel(self.frame)
        self.lb_year.setGeometry(QtCore.QRect(30, 20, 31, 16))
        self.lb_year.setObjectName("lb_year")
        self.lb_day = QtWidgets.QLabel(self.frame)
        self.lb_day.setGeometry(QtCore.QRect(30, 50, 31, 16))
        self.lb_day.setObjectName("lb_day")
        self.lb_cam = QtWidgets.QLabel(self.frame)
        self.lb_cam.setGeometry(QtCore.QRect(190, 50, 41, 16))
        self.lb_cam.setObjectName("lb_cam")
        self.cb_week = QtWidgets.QComboBox(self.frame)
        self.cb_week.setGeometry(QtCore.QRect(250, 20, 71, 22))
        self.cb_week.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_week.setObjectName("cb_week")
        self.lb_week = QtWidgets.QLabel(self.frame)
        self.lb_week.setGeometry(QtCore.QRect(190, 20, 31, 16))
        self.lb_week.setObjectName("lb_week")
        self.cb_cam = QtWidgets.QComboBox(self.frame)
        self.cb_cam.setGeometry(QtCore.QRect(250, 50, 71, 22))
        self.cb_cam.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_cam.setObjectName("cb_cam")

        self.retranslateUi(UiQiandaoChose)
        QtCore.QMetaObject.connectSlotsByName(UiQiandaoChose)

    def retranslateUi(self, UiQiandaoChose):
        _translate = QtCore.QCoreApplication.translate
        UiQiandaoChose.setWindowTitle(_translate("UiQiandaoChose", "Form"))
        self.bt_back.setText(_translate("UiQiandaoChose", "返回"))
        self.bt_confrim.setText(_translate("UiQiandaoChose", "确认"))
        self.lb_year.setText(_translate("UiQiandaoChose", "年份"))
        self.lb_day.setText(_translate("UiQiandaoChose", "周内"))
        self.lb_cam.setText(_translate("UiQiandaoChose", "摄像头"))
        self.lb_week.setText(_translate("UiQiandaoChose", "周次"))

