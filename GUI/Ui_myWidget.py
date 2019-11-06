# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\waibao\myWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(462, 105)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 40, 331, 49))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cb_daytime = QtWidgets.QComboBox(self.widget)
        self.cb_daytime.setObjectName("cb_daytime")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.cb_daytime.addItem("")
        self.gridLayout_2.addWidget(self.cb_daytime, 0, 1, 1, 1)
        self.ck_day = QtWidgets.QCheckBox(self.widget)
        self.ck_day.setObjectName("ck_day")
        self.gridLayout_2.addWidget(self.ck_day, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cb_daytime.setItemText(0, _translate("Form", "10:00"))
        self.cb_daytime.setItemText(1, _translate("Form", "11:00"))
        self.cb_daytime.setItemText(2, _translate("Form", "12:00"))
        self.cb_daytime.setItemText(3, _translate("Form", "13:00"))
        self.cb_daytime.setItemText(4, _translate("Form", "14:00"))
        self.cb_daytime.setItemText(5, _translate("Form", "15:00"))
        self.cb_daytime.setItemText(6, _translate("Form", "16:00"))
        self.cb_daytime.setItemText(7, _translate("Form", "17:00"))
        self.cb_daytime.setItemText(8, _translate("Form", "18:00"))
        self.cb_daytime.setItemText(9, _translate("Form", "19:00"))
        self.cb_daytime.setItemText(10, _translate("Form", "20:00"))
        self.cb_daytime.setItemText(11, _translate("Form", "21:00"))
        self.ck_day.setText(_translate("Form", "CheckBox"))
