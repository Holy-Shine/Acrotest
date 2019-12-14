# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClassInfoCheck.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Qiandao.ComboChecBox import ComboCheckBox
class Ui_ClassInfoCheck(object):
    def setupUi(self, ClassInfoCheck):
        ClassInfoCheck.setObjectName("ClassInfoCheck")
        ClassInfoCheck.resize(845, 757)
        self.groupBox = QtWidgets.QGroupBox(ClassInfoCheck)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 811, 51))
        self.groupBox.setObjectName("groupBox")
        self.lb_year = QtWidgets.QLabel(self.groupBox)
        self.lb_year.setGeometry(QtCore.QRect(20, 20, 54, 21))
        self.lb_year.setObjectName("lb_year")
        self.cb_year = QtWidgets.QComboBox(self.groupBox)
        self.cb_year.setGeometry(QtCore.QRect(70, 20, 71, 22))
        self.cb_year.setObjectName("cb_year")
        self.lb_week = QtWidgets.QLabel(self.groupBox)
        self.lb_week.setGeometry(QtCore.QRect(150, 20, 54, 21))
        self.lb_week.setObjectName("lb_week")
        self.cb_week = QtWidgets.QComboBox(self.groupBox)
        self.cb_week.setGeometry(QtCore.QRect(200, 20, 91, 22))
        self.cb_week.setObjectName("cb_week")
        self.bt_search = QtWidgets.QPushButton(self.groupBox)
        self.bt_search.setGeometry(QtCore.QRect(450, 10, 71, 31))
        self.bt_search.setObjectName("bt_search")
        self.lb_weekday = QtWidgets.QLabel(self.groupBox)
        self.lb_weekday.setGeometry(QtCore.QRect(300, 20, 41, 21))
        self.lb_weekday.setObjectName("lb_weekday")
        self.weekday = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        self.cb_weekday = ComboCheckBox(self.weekday, self.groupBox)
        self.cb_weekday.setGeometry(QtCore.QRect(350, 20, 91, 22))
        self.cb_weekday.setObjectName("cb_weekday")
        self.lb_selectone = QtWidgets.QLabel(self.groupBox)
        self.lb_selectone.setGeometry(QtCore.QRect(530, 10, 271, 31))
        self.lb_selectone.setObjectName("lb_selectone")
        self.groupBox_2 = QtWidgets.QGroupBox(ClassInfoCheck)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 120, 811, 621))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tv_classlist = QtWidgets.QTableView(self.groupBox_2)
        self.tv_classlist.setGeometry(QtCore.QRect(10, 20, 801, 601))
        self.tv_classlist.setObjectName("tv_classlist")
        self.groupBox_3 = QtWidgets.QGroupBox(ClassInfoCheck)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 811, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lb_student = QtWidgets.QLabel(self.groupBox_3)
        self.lb_student.setGeometry(QtCore.QRect(370, 20, 421, 21))
        self.lb_student.setObjectName("lb_student")
        self.lb_time = QtWidgets.QLabel(self.groupBox_3)
        self.lb_time.setGeometry(QtCore.QRect(20, 20, 341, 21))
        self.lb_time.setObjectName("lb_time")

        self.retranslateUi(ClassInfoCheck)
        QtCore.QMetaObject.connectSlotsByName(ClassInfoCheck)

    def retranslateUi(self, ClassInfoCheck):
        _translate = QtCore.QCoreApplication.translate
        ClassInfoCheck.setWindowTitle(_translate("ClassInfoCheck", "Form"))
        self.groupBox.setTitle(_translate("ClassInfoCheck", "时间选择"))
        self.lb_year.setText(_translate("ClassInfoCheck", "选择年份"))
        self.lb_week.setText(_translate("ClassInfoCheck", "选择周"))
        self.bt_search.setText(_translate("ClassInfoCheck", "查询"))
        self.lb_weekday.setText(_translate("ClassInfoCheck", "周数"))
        self.lb_selectone.setText(_translate("ClassInfoCheck", "查询日期"))
        self.groupBox_2.setTitle(_translate("ClassInfoCheck", "排课信息"))
        self.groupBox_3.setTitle(_translate("ClassInfoCheck", "基础信息"))
        self.lb_student.setText(_translate("ClassInfoCheck", "当前学生"))
        self.lb_time.setText(_translate("ClassInfoCheck", "当前时间"))

