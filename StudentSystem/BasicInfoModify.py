# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BasicInfoModify.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BasicInfoModify(object):
    def setupUi(self, BasicInfoModify):
        BasicInfoModify.setObjectName("BasicInfoModify")
        BasicInfoModify.resize(548, 576)
        BasicInfoModify.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.groupBox = QtWidgets.QGroupBox(BasicInfoModify)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 431, 461))
        self.groupBox.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(50, 20, 321, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lb_name = QtWidgets.QLabel(self.frame)
        self.lb_name.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.lb_name.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.lb_name.setObjectName("lb_name")
        self.et_name = QtWidgets.QLineEdit(self.frame)
        self.et_name.setGeometry(QtCore.QRect(100, 10, 201, 21))
        self.et_name.setStyleSheet("font: 10pt \"Adobe Arabic\";\n"
"background-color: rgb(255, 255, 255);")
        self.et_name.setText("")
        self.et_name.setObjectName("et_name")
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setGeometry(QtCore.QRect(50, 80, 321, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lb_age = QtWidgets.QLabel(self.frame_2)
        self.lb_age.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.lb_age.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.lb_age.setObjectName("lb_age")
        self.et_age = QtWidgets.QLineEdit(self.frame_2)
        self.et_age.setGeometry(QtCore.QRect(100, 10, 201, 21))
        self.et_age.setStyleSheet("font: 10pt \"Adobe Arabic\";\n"
"background-color: rgb(255, 255, 255);")
        self.et_age.setText("")
        self.et_age.setObjectName("et_age")
        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setGeometry(QtCore.QRect(50, 140, 321, 41))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lb_gender = QtWidgets.QLabel(self.frame_3)
        self.lb_gender.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.lb_gender.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.lb_gender.setObjectName("lb_gender")
        self.rb_man = QtWidgets.QRadioButton(self.frame_3)
        self.rb_man.setGeometry(QtCore.QRect(140, 10, 41, 21))
        self.rb_man.setStyleSheet("font: 10pt \"Adobe Arabic\";")
        self.rb_man.setObjectName("tb_man")
        self.rb_woman = QtWidgets.QRadioButton(self.frame_3)
        self.rb_woman.setGeometry(QtCore.QRect(190, 10, 51, 21))
        self.rb_woman.setStyleSheet("font: 10pt \"Adobe Arabic\";")
        self.rb_woman.setObjectName("rb_woman")
        self.frame_4 = QtWidgets.QFrame(self.groupBox)
        self.frame_4.setGeometry(QtCore.QRect(50, 200, 321, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lb_parent = QtWidgets.QLabel(self.frame_4)
        self.lb_parent.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.lb_parent.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.lb_parent.setObjectName("lb_parent")
        self.et_parent = QtWidgets.QLineEdit(self.frame_4)
        self.et_parent.setGeometry(QtCore.QRect(100, 10, 201, 21))
        self.et_parent.setStyleSheet("font: 10pt \"Adobe Arabic\";\n"
"background-color: rgb(255, 255, 255);")
        self.et_parent.setText("")
        self.et_parent.setObjectName("et_parent")
        self.frame_5 = QtWidgets.QFrame(self.groupBox)
        self.frame_5.setGeometry(QtCore.QRect(50, 270, 321, 41))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.lb_phone = QtWidgets.QLabel(self.frame_5)
        self.lb_phone.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.lb_phone.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.lb_phone.setObjectName("lb_phone")
        self.et_phone = QtWidgets.QLineEdit(self.frame_5)
        self.et_phone.setGeometry(QtCore.QRect(100, 10, 201, 21))
        self.et_phone.setStyleSheet("font: 10pt \"Adobe Arabic\";\n"
"background-color: rgb(255, 255, 255);")
        self.et_phone.setText("")
        self.et_phone.setObjectName("et_phone")
        self.frame_6 = QtWidgets.QFrame(self.groupBox)
        self.frame_6.setGeometry(QtCore.QRect(50, 390, 321, 41))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.lb_cishu = QtWidgets.QLabel(self.frame_6)
        self.lb_cishu.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.lb_cishu.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.lb_cishu.setObjectName("lb_cishu")
        self.et_cishu = QtWidgets.QLineEdit(self.frame_6)
        self.et_cishu.setGeometry(QtCore.QRect(100, 10, 201, 21))
        self.et_cishu.setStyleSheet("font: 10pt \"Adobe Arabic\";\n"
"background-color: rgb(255, 255, 255);")
        self.et_cishu.setText("")
        self.et_cishu.setObjectName("et_cishu")
        self.frame_7 = QtWidgets.QFrame(self.groupBox)
        self.frame_7.setGeometry(QtCore.QRect(50, 330, 321, 41))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.lb_classitem = QtWidgets.QLabel(self.frame_7)
        self.lb_classitem.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.lb_classitem.setStyleSheet("font: 12pt \"Adobe Arabic\";")
        self.lb_classitem.setObjectName("lb_classitem")
        self.cb_classitem = QtWidgets.QComboBox(self.frame_7)
        self.cb_classitem.setGeometry(QtCore.QRect(150, 10, 101, 22))
        self.cb_classitem.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_classitem.setObjectName("cb_classitem")
        self.frame_8 = QtWidgets.QFrame(BasicInfoModify)
        self.frame_8.setGeometry(QtCore.QRect(40, 490, 431, 71))
        self.frame_8.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.bt_confrim = QtWidgets.QPushButton(self.frame_8)
        self.bt_confrim.setGeometry(QtCore.QRect(70, 10, 111, 51))
        self.bt_confrim.setObjectName("bt_confrim")
        self.bt_back = QtWidgets.QPushButton(self.frame_8)
        self.bt_back.setGeometry(QtCore.QRect(250, 10, 111, 51))
        self.bt_back.setObjectName("bt_back")

        self.retranslateUi(BasicInfoModify)
        QtCore.QMetaObject.connectSlotsByName(BasicInfoModify)

    def retranslateUi(self, BasicInfoModify):
        _translate = QtCore.QCoreApplication.translate
        BasicInfoModify.setWindowTitle(_translate("BasicInfoModify", "学员基础信息修改"))
        self.groupBox.setTitle(_translate("BasicInfoModify", "修改信息"))
        self.lb_name.setText(_translate("BasicInfoModify", "学员姓名"))
        self.lb_age.setText(_translate("BasicInfoModify", "学员年龄"))
        self.lb_gender.setText(_translate("BasicInfoModify", "学员性别"))
        self.rb_man.setText(_translate("BasicInfoModify", "男"))
        self.rb_woman.setText(_translate("BasicInfoModify", "女"))
        self.lb_parent.setText(_translate("BasicInfoModify", "学员家长"))
        self.lb_phone.setText(_translate("BasicInfoModify", "联系方式"))
        self.lb_cishu.setText(_translate("BasicInfoModify", "剩余次数"))
        self.lb_classitem.setText(_translate("BasicInfoModify", "课程种类"))
        self.bt_confrim.setText(_translate("BasicInfoModify", "确认修改"))
        self.bt_back.setText(_translate("BasicInfoModify", "返回"))

