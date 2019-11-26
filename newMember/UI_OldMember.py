# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OldMember.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from  MyQSS import myLabel

class Ui_OldMember(object):
    def setupUi(self, OldMember):
        OldMember.setObjectName("OldMember")
        OldMember.resize(1290, 652)
        OldMember.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.lb_head = QtWidgets.QLabel(OldMember)
        self.lb_head.setGeometry(QtCore.QRect(450, 20, 401, 41))
        self.lb_head.setStyleSheet("font: 75 28pt \"楷体\";")
        self.lb_head.setObjectName("lb_head")
        self.groupBox_BasicInfo = QtWidgets.QGroupBox(OldMember)
        self.groupBox_BasicInfo.setGeometry(QtCore.QRect(290, 70, 701, 541))
        self.groupBox_BasicInfo.setAutoFillBackground(False)
        self.groupBox_BasicInfo.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.groupBox_BasicInfo.setObjectName("groupBox_BasicInfo")
        self.lb_name = QtWidgets.QLabel(self.groupBox_BasicInfo)
        self.lb_name.setGeometry(QtCore.QRect(70, 60, 61, 21))
        self.lb_name.setStyleSheet("font: 10pt \"宋体\";")
        self.lb_name.setObjectName("lb_name")
        self.et_name = QtWidgets.QLineEdit(self.groupBox_BasicInfo)
        self.et_name.setGeometry(QtCore.QRect(140, 60, 121, 21))
        self.et_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_name.setObjectName("et_name")
        self.lb_age = QtWidgets.QLabel(self.groupBox_BasicInfo)
        self.lb_age.setGeometry(QtCore.QRect(50, 150, 81, 21))
        self.lb_age.setStyleSheet("font: 10pt \"宋体\";")
        self.lb_age.setObjectName("lb_age")
        self.et_age = QtWidgets.QLineEdit(self.groupBox_BasicInfo)
        self.et_age.setGeometry(QtCore.QRect(160, 150, 121, 21))
        self.et_age.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_age.setObjectName("et_age")
        self.lb_parent = QtWidgets.QLabel(self.groupBox_BasicInfo)
        self.lb_parent.setGeometry(QtCore.QRect(70, 210, 71, 21))
        self.lb_parent.setStyleSheet("font: 10pt \"宋体\";")
        self.lb_parent.setObjectName("lb_parent")
        self.et_parent = QtWidgets.QLineEdit(self.groupBox_BasicInfo)
        self.et_parent.setGeometry(QtCore.QRect(160, 210, 121, 21))
        self.et_parent.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_parent.setObjectName("et_parent")
        self.lb_phone = QtWidgets.QLabel(self.groupBox_BasicInfo)
        self.lb_phone.setGeometry(QtCore.QRect(300, 60, 61, 21))
        self.lb_phone.setStyleSheet("font: 10pt \"宋体\";")
        self.lb_phone.setObjectName("lb_phone")
        self.et_phone = QtWidgets.QLineEdit(self.groupBox_BasicInfo)
        self.et_phone.setGeometry(QtCore.QRect(360, 60, 121, 21))
        self.et_phone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_phone.setObjectName("et_phone")
        self.lb_card = QtWidgets.QLabel(self.groupBox_BasicInfo)
        self.lb_card.setGeometry(QtCore.QRect(70, 260, 81, 21))
        self.lb_card.setStyleSheet("font: 10pt \"宋体\";")
        self.lb_card.setObjectName("lb_card")
        self.cb_card = QtWidgets.QComboBox(self.groupBox_BasicInfo)
        self.cb_card.setGeometry(QtCore.QRect(180, 260, 81, 22))
        self.cb_card.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_card.setObjectName("cb_card")
        self.lb_cichu = QtWidgets.QLabel(self.groupBox_BasicInfo)
        self.lb_cichu.setGeometry(QtCore.QRect(50, 360, 91, 21))
        self.lb_cichu.setStyleSheet("font: 10pt \"宋体\";")
        self.lb_cichu.setObjectName("lb_cichu")
        self.et_cichu = QtWidgets.QLineEdit(self.groupBox_BasicInfo)
        self.et_cichu.setGeometry(QtCore.QRect(160, 360, 121, 21))
        self.et_cichu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_cichu.setObjectName("et_cichu")
        self.lb_money = QtWidgets.QLabel(self.groupBox_BasicInfo)
        self.lb_money.setGeometry(QtCore.QRect(50, 410, 91, 21))
        self.lb_money.setStyleSheet("font: 10pt \"宋体\";")
        self.lb_money.setObjectName("lb_money")
        self.et_money = QtWidgets.QLineEdit(self.groupBox_BasicInfo)
        self.et_money.setGeometry(QtCore.QRect(160, 410, 121, 21))
        self.et_money.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_money.setObjectName("et_money")
        self.pb_query = QtWidgets.QPushButton(self.groupBox_BasicInfo)
        self.pb_query.setGeometry(QtCore.QRect(510, 50, 61, 31))
        self.pb_query.setObjectName("pb_query")
        self.lb_cam = QtWidgets.QLabel(self.groupBox_BasicInfo)
        self.lb_cam.setGeometry(QtCore.QRect(340, 120, 260, 361))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 197, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 197, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 197, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 197, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 197, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 197, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 197, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 197, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 197, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lb_cam.setPalette(palette)
        self.lb_cam.setStyleSheet("background-color: rgb(200, 197, 198);")
        self.lb_cam.setText("")
        self.lb_cam.setObjectName("lb_cam")
        self.bt_confrim = QtWidgets.QPushButton(self.groupBox_BasicInfo)
        self.bt_confrim.setGeometry(QtCore.QRect(50, 470, 91, 41))
        self.bt_confrim.setObjectName("bt_confrim")
        self.bt_back = QtWidgets.QPushButton(self.groupBox_BasicInfo)
        self.bt_back.setGeometry(QtCore.QRect(180, 470, 81, 41))
        self.bt_back.setObjectName("bt_back")
        self.lb_toNew = myLabel(self.groupBox_BasicInfo)
        self.lb_toNew.setGeometry(QtCore.QRect(570, 510, 101, 21))
        self.lb_toNew.setObjectName("lb_toNew")
        self.cb_classitem = QtWidgets.QComboBox(self.groupBox_BasicInfo)
        self.cb_classitem.setGeometry(QtCore.QRect(180, 310, 81, 22))
        self.cb_classitem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_classitem.setObjectName("cb_classitem")
        self.lb_classitem = QtWidgets.QLabel(self.groupBox_BasicInfo)
        self.lb_classitem.setGeometry(QtCore.QRect(70, 310, 81, 21))
        self.lb_classitem.setStyleSheet("font: 10pt \"宋体\";")
        self.lb_classitem.setObjectName("lb_classitem")

        self.retranslateUi(OldMember)
        QtCore.QMetaObject.connectSlotsByName(OldMember)

    def retranslateUi(self, OldMember):
        _translate = QtCore.QCoreApplication.translate
        OldMember.setWindowTitle(_translate("OldMember", "Form"))
        self.lb_head.setText(_translate("OldMember", "学 员 续 卡 系 统"))
        self.groupBox_BasicInfo.setTitle(_translate("OldMember", "信息查询"))
        self.lb_name.setText(_translate("OldMember", "学员姓名"))
        self.lb_age.setText(_translate("OldMember", "学员年龄(岁)"))
        self.lb_parent.setText(_translate("OldMember", "学员家长"))
        self.lb_phone.setText(_translate("OldMember", "联系方式"))
        self.lb_card.setText(_translate("OldMember", "办卡模式"))
        self.lb_cichu.setText(_translate("OldMember", "添加次数(次)"))
        self.lb_money.setText(_translate("OldMember", "办卡金额(元)"))
        self.pb_query.setText(_translate("OldMember", "查询"))
        self.bt_confrim.setText(_translate("OldMember", "确认"))
        self.bt_back.setText(_translate("OldMember", "返回"))
        self.lb_toNew.setText(_translate("OldMember", "添加新学员"))
        self.lb_classitem.setText(_translate("OldMember", "课程种类"))

