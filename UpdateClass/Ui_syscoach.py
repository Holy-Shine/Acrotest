# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\waibaoTest\GUI\syscoach.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sysCoach(object):
    def setupUi(self, sysCoach):
        sysCoach.setObjectName("sysCoach")
        sysCoach.resize(1291, 651)
        sysCoach.setMinimumSize(QtCore.QSize(1291, 651))
        sysCoach.setMaximumSize(QtCore.QSize(1291, 651))
        sysCoach.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.left_widget = QtWidgets.QWidget(sysCoach)
        self.left_widget.setGeometry(QtCore.QRect(-10, 0, 171, 661))
        self.left_widget.setStyleSheet("background:#DDDDDD")
        self.left_widget.setObjectName("left_widget")
        self.listFunc = QtWidgets.QListWidget(self.left_widget)
        self.listFunc.setGeometry(QtCore.QRect(20, 60, 131, 441))
        self.listFunc.setStyleSheet("QListWidget#listFunc{\n"
"    outline: 0px;\n"
"    border:0px;\n"
"    min-width: 120px;\n"
"    color: Black;\n"
"    background: #DDDDDD;\n"
"}\n"
"\n"
"QListWidget#listFunc::Item{\n"
"     height:30px;\n"
"}\n"
"QListWidget#listFunc::Item:selected {\n"
"    background: rgb(49, 194, 124);\n"
"    border-radius:1.5px;\n"
"   \n"
"}\n"
"")
        self.listFunc.setObjectName("listFunc")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/add_c.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon)
        self.listFunc.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resource/up_c.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        item.setIcon(icon1)
        self.listFunc.addItem(item)
        self.label = QtWidgets.QLabel(self.left_widget)
        self.label.setGeometry(QtCore.QRect(40, 20, 81, 21))
        self.label.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label.setObjectName("label")
        self.stackedWidget = QtWidgets.QStackedWidget(sysCoach)
        self.stackedWidget.setGeometry(QtCore.QRect(190, 50, 1061, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label_2.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 641, 501))
        self.groupBox.setObjectName("groupBox")
        self.te_cmsg = QtWidgets.QTextEdit(self.groupBox)
        self.te_cmsg.setGeometry(QtCore.QRect(40, 140, 561, 311))
        self.te_cmsg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.te_cmsg.setObjectName("te_cmsg")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(40, 110, 72, 15))
        self.label_14.setObjectName("label_14")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 41, 561, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.le_c_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_c_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_c_name.setObjectName("le_c_name")
        self.gridLayout.addWidget(self.le_c_name, 0, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.le_c_phone = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_c_phone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_c_phone.setObjectName("le_c_phone")
        self.gridLayout.addWidget(self.le_c_phone, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.cb_c_gender = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_c_gender.setObjectName("cb_c_gender")
        self.cb_c_gender.addItem("")
        self.cb_c_gender.addItem("")
        self.gridLayout.addWidget(self.cb_c_gender, 0, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 3, 1, 1)
        self.cb_a_type = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_a_type.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_a_type.setObjectName("cb_a_type")
        self.cb_a_type.addItem("")
        self.cb_a_type.addItem("")
        self.cb_a_type.addItem("")
        self.gridLayout.addWidget(self.cb_a_type, 1, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.cb_a_rank = QtWidgets.QComboBox(self.layoutWidget)
        self.cb_a_rank.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_a_rank.setObjectName("cb_a_rank")
        self.cb_a_rank.addItem("")
        self.cb_a_rank.addItem("")
        self.cb_a_rank.addItem("")
        self.cb_a_rank.addItem("")
        self.gridLayout.addWidget(self.cb_a_rank, 1, 1, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(680, 50, 351, 501))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_confirm = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_confirm.setGeometry(QtCore.QRect(70, 60, 221, 61))
        self.btn_confirm.setObjectName("btn_confirm")
        self.btn_clear = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_clear.setGeometry(QtCore.QRect(70, 160, 221, 61))
        self.btn_clear.setObjectName("btn_clear")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label_3.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_4.setGeometry(QtCore.QRect(680, 50, 351, 481))
        self.groupBox_4.setToolTip("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.btn_confirm_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_confirm_2.setGeometry(QtCore.QRect(20, 300, 311, 61))
        self.btn_confirm_2.setObjectName("btn_confirm_2")
        self.btn_remove = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_remove.setGeometry(QtCore.QRect(20, 390, 311, 61))
        self.btn_remove.setObjectName("btn_remove")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(21, 71, 75, 16))
        self.label_22.setObjectName("label_22")
        self.lb_result = QtWidgets.QLabel(self.groupBox_4)
        self.lb_result.setGeometry(QtCore.QRect(103, 71, 221, 16))
        self.lb_result.setText("")
        self.lb_result.setObjectName("lb_result")
        self.tv_search_coach = QtWidgets.QTableView(self.groupBox_4)
        self.tv_search_coach.setGeometry(QtCore.QRect(20, 90, 311, 192))
        self.tv_search_coach.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tv_search_coach.setObjectName("tv_search_coach")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 311, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_search = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_search.setObjectName("btn_search")
        self.gridLayout_3.addWidget(self.btn_search, 0, 2, 1, 1)
        self.le_search_term = QtWidgets.QLineEdit(self.layoutWidget1)
        self.le_search_term.setToolTip("")
        self.le_search_term.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_search_term.setObjectName("le_search_term")
        self.gridLayout_3.addWidget(self.le_search_term, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 50, 641, 481))
        self.groupBox_3.setObjectName("groupBox_3")
        self.te_cmsg_2 = QtWidgets.QTextEdit(self.groupBox_3)
        self.te_cmsg_2.setEnabled(True)
        self.te_cmsg_2.setGeometry(QtCore.QRect(40, 140, 561, 311))
        self.te_cmsg_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.te_cmsg_2.setObjectName("te_cmsg_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(40, 110, 72, 15))
        self.label_15.setObjectName("label_15")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 41, 561, 54))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)
        self.le_c_name_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.le_c_name_3.setEnabled(True)
        self.le_c_name_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_c_name_3.setObjectName("le_c_name_3")
        self.gridLayout_4.addWidget(self.le_c_name_3, 0, 1, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 0, 3, 1, 1)
        self.le_c_phone_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.le_c_phone_3.setEnabled(True)
        self.le_c_phone_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_c_phone_3.setObjectName("le_c_phone_3")
        self.gridLayout_4.addWidget(self.le_c_phone_3, 0, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 0, 5, 1, 1)
        self.cb_c_gender_3 = QtWidgets.QComboBox(self.layoutWidget2)
        self.cb_c_gender_3.setEnabled(True)
        self.cb_c_gender_3.setObjectName("cb_c_gender_3")
        self.cb_c_gender_3.addItem("")
        self.cb_c_gender_3.addItem("")
        self.gridLayout_4.addWidget(self.cb_c_gender_3, 0, 6, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 1, 3, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_3.setEnabled(True)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_3, 1, 4, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_4.setEnabled(True)
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_4, 1, 1, 1, 2)
        self.stackedWidget.addWidget(self.page_2)
        self.lb_head = QtWidgets.QLabel(sysCoach)
        self.lb_head.setGeometry(QtCore.QRect(550, 10, 281, 41))
        self.lb_head.setStyleSheet("font: 75 28pt \"楷体\";")
        self.lb_head.setObjectName("lb_head")

        self.retranslateUi(sysCoach)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(sysCoach)

    def retranslateUi(self, sysCoach):
        _translate = QtCore.QCoreApplication.translate
        sysCoach.setWindowTitle(_translate("sysCoach", "教练系统"))
        __sortingEnabled = self.listFunc.isSortingEnabled()
        self.listFunc.setSortingEnabled(False)
        item = self.listFunc.item(0)
        item.setText(_translate("sysCoach", "添加教练人员"))
        item = self.listFunc.item(1)
        item.setText(_translate("sysCoach", "更改教练信息"))
        self.listFunc.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("sysCoach", "菜 单 栏"))
        self.label_2.setText(_translate("sysCoach", "添加教练人员"))
        self.groupBox.setTitle(_translate("sysCoach", "教练信息"))
        self.label_14.setText(_translate("sysCoach", "简单介绍："))
        self.label_4.setText(_translate("sysCoach", "姓名："))
        self.label_5.setText(_translate("sysCoach", "联系方式："))
        self.label_6.setText(_translate("sysCoach", "性别："))
        self.cb_c_gender.setItemText(0, _translate("sysCoach", "男"))
        self.cb_c_gender.setItemText(1, _translate("sysCoach", "女"))
        self.label_13.setText(_translate("sysCoach", "类别："))
        self.cb_a_type.setItemText(0, _translate("sysCoach", "轮滑"))
        self.cb_a_type.setItemText(1, _translate("sysCoach", "平衡车"))
        self.cb_a_type.setItemText(2, _translate("sysCoach", "均可"))
        self.label_7.setText(_translate("sysCoach", "职级："))
        self.cb_a_rank.setItemText(0, _translate("sysCoach", "助教"))
        self.cb_a_rank.setItemText(1, _translate("sysCoach", "初级"))
        self.cb_a_rank.setItemText(2, _translate("sysCoach", "中级"))
        self.cb_a_rank.setItemText(3, _translate("sysCoach", "高级"))
        self.groupBox_2.setTitle(_translate("sysCoach", "操作栏"))
        self.btn_confirm.setText(_translate("sysCoach", "确认录入"))
        self.btn_clear.setText(_translate("sysCoach", "清空输入"))
        self.label_3.setText(_translate("sysCoach", "更改教练信息"))
        self.groupBox_4.setTitle(_translate("sysCoach", "操作栏"))
        self.btn_confirm_2.setText(_translate("sysCoach", "确认修改"))
        self.btn_remove.setText(_translate("sysCoach", "删除教练"))
        self.label_22.setText(_translate("sysCoach", "搜索状态："))
        self.btn_search.setText(_translate("sysCoach", "搜索"))
        self.le_search_term.setPlaceholderText(_translate("sysCoach", "输入\"*\"查询全部"))
        self.label_12.setText(_translate("sysCoach", "关键字："))
        self.groupBox_3.setTitle(_translate("sysCoach", "教练信息"))
        self.label_15.setText(_translate("sysCoach", "简单介绍："))
        self.label_16.setText(_translate("sysCoach", "姓名："))
        self.label_17.setText(_translate("sysCoach", "联系方式："))
        self.label_18.setText(_translate("sysCoach", "性别："))
        self.cb_c_gender_3.setItemText(0, _translate("sysCoach", "男"))
        self.cb_c_gender_3.setItemText(1, _translate("sysCoach", "女"))
        self.label_19.setText(_translate("sysCoach", "类别："))
        self.comboBox_3.setItemText(0, _translate("sysCoach", "轮滑"))
        self.comboBox_3.setItemText(1, _translate("sysCoach", "平衡车"))
        self.comboBox_3.setItemText(2, _translate("sysCoach", "均可"))
        self.label_20.setText(_translate("sysCoach", "职级："))
        self.comboBox_4.setItemText(0, _translate("sysCoach", "助教"))
        self.comboBox_4.setItemText(1, _translate("sysCoach", "初级"))
        self.comboBox_4.setItemText(2, _translate("sysCoach", "中级"))
        self.comboBox_4.setItemText(3, _translate("sysCoach", "高级"))
        self.lb_head.setText(_translate("sysCoach", "教 练 系 统"))
