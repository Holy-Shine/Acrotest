# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentMain.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StudentMain(object):
    def setupUi(self, StudentMain):
        StudentMain.setObjectName("StudentMain")
        StudentMain.resize(1290, 651)
        StudentMain.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.groupBox = QtWidgets.QGroupBox(StudentMain)
        self.groupBox.setGeometry(QtCore.QRect(30, 40, 821, 591))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.table_studentList = QtWidgets.QTableView(self.groupBox)
        self.table_studentList.setGeometry(QtCore.QRect(10, 20, 801, 561))
        self.table_studentList.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.table_studentList.setObjectName("table_studentList")
        self.groupBox_2 = QtWidgets.QGroupBox(StudentMain)
        self.groupBox_2.setGeometry(QtCore.QRect(870, 140, 351, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.et_search = QtWidgets.QLineEdit(self.groupBox_2)
        self.et_search.setGeometry(QtCore.QRect(90, 30, 151, 31))
        self.et_search.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_search.setObjectName("et_search")
        self.bt_search = QtWidgets.QPushButton(self.groupBox_2)
        self.bt_search.setGeometry(QtCore.QRect(260, 30, 71, 31))
        self.bt_search.setObjectName("bt_search")
        self.lb_phone = QtWidgets.QLabel(self.groupBox_2)
        self.lb_phone.setGeometry(QtCore.QRect(20, 30, 54, 31))
        self.lb_phone.setObjectName("lb_phone")
        self.groupBox_3 = QtWidgets.QGroupBox(StudentMain)
        self.groupBox_3.setGeometry(QtCore.QRect(870, 240, 361, 371))
        self.groupBox_3.setObjectName("groupBox_3")
        self.bt_modifyinfo = QtWidgets.QPushButton(self.groupBox_3)
        self.bt_modifyinfo.setGeometry(QtCore.QRect(20, 120, 331, 61))
        self.bt_modifyinfo.setObjectName("bt_modifyinfo")
        self.bt_checkclass = QtWidgets.QPushButton(self.groupBox_3)
        self.bt_checkclass.setGeometry(QtCore.QRect(20, 200, 331, 61))
        self.bt_checkclass.setObjectName("bt_checkclass")
        self.bt_flash = QtWidgets.QPushButton(self.groupBox_3)
        self.bt_flash.setGeometry(QtCore.QRect(20, 40, 331, 61))
        self.bt_flash.setObjectName("bt_flash")
        self.bt_delete = QtWidgets.QPushButton(self.groupBox_3)
        self.bt_delete.setGeometry(QtCore.QRect(20, 290, 331, 61))
        self.bt_delete.setObjectName("bt_quit")
        self.lb_toplabel = QtWidgets.QLabel(StudentMain)
        self.lb_toplabel.setGeometry(QtCore.QRect(930, 60, 261, 51))
        self.lb_toplabel.setStyleSheet("font: 75 28pt \"楷体\";")
        self.lb_toplabel.setTextFormat(QtCore.Qt.AutoText)
        self.lb_toplabel.setObjectName("lb_toplabel")

        self.retranslateUi(StudentMain)
        QtCore.QMetaObject.connectSlotsByName(StudentMain)

    def retranslateUi(self, StudentMain):
        _translate = QtCore.QCoreApplication.translate
        StudentMain.setWindowTitle(_translate("StudentMain", "Form"))
        self.groupBox_2.setTitle(_translate("StudentMain", "查询"))
        self.bt_search.setText(_translate("StudentMain", "查询"))
        self.lb_phone.setText(_translate("StudentMain", "查询学生"))
        self.groupBox_3.setTitle(_translate("StudentMain", "功能菜单"))
        self.bt_modifyinfo.setText(_translate("StudentMain", "学生信息修改"))
        self.bt_checkclass.setText(_translate("StudentMain", "排课信息查看(一周内）"))
        self.bt_flash.setText(_translate("StudentMain", "刷新学生表格"))
        self.bt_delete.setText(_translate("StudentMain", "删除学员"))
        self.lb_toplabel.setText(_translate("StudentMain", "学 生 系 统 "))

