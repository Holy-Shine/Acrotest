from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Evaluation(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1292, 648)
        Form.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.left_widget = QtWidgets.QWidget(Form)
        self.left_widget.setGeometry(QtCore.QRect(0, 0, 161, 661))
        self.left_widget.setStyleSheet("background:#DDDDDD")
        self.left_widget.setObjectName("left_widget")
        self.listFunc = QtWidgets.QListWidget(self.left_widget)
        self.listFunc.setGeometry(QtCore.QRect(10, 60, 141, 511))
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
        icon.addPixmap(QtGui.QPixmap("SummarySystem/resource/card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listFunc.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listFunc.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("SummarySystem/resource/money.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listFunc.addItem(item)
        self.label_13 = QtWidgets.QLabel(self.left_widget)
        self.label_13.setGeometry(QtCore.QRect(40, 20, 81, 21))
        self.label_13.setStyleSheet("font: 75 14pt \"黑体\";")
        self.label_13.setObjectName("label_13")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(170, 10, 1111, 621))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 261, 631))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 241, 51))
        self.groupBox.setObjectName("groupBox")
        self.et_search_stu = QtWidgets.QLineEdit(self.groupBox)
        self.et_search_stu.setGeometry(QtCore.QRect(10, 20, 151, 20))
        self.et_search_stu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_search_stu.setObjectName("et_search_stu")
        self.bt_search_stu = QtWidgets.QPushButton(self.groupBox)
        self.bt_search_stu.setGeometry(QtCore.QRect(170, 20, 61, 23))
        self.bt_search_stu.setObjectName("bt_search_stu")
        self.tv_list_stu = QtWidgets.QTableView(self.groupBox_2)
        self.tv_list_stu.setGeometry(QtCore.QRect(10, 80, 241, 541))
        self.tv_list_stu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tv_list_stu.setObjectName("tv_list_stu")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 0, 541, 631))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tv_eval_stu = QtWidgets.QTreeWidget(self.groupBox_3)
        self.tv_eval_stu.setGeometry(QtCore.QRect(0, 40, 531, 581))
        self.tv_eval_stu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tv_eval_stu.setObjectName("tv_eval_stu")
        self.lb_stu_eval_num = QtWidgets.QLabel(self.groupBox_3)
        self.lb_stu_eval_num.setGeometry(QtCore.QRect(20, 20, 391, 16))
        self.lb_stu_eval_num.setObjectName("lb_stu_eval_num")
        self.check_stu_openall = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_stu_openall.setGeometry(QtCore.QRect(440, 20, 91, 19))
        self.check_stu_openall.setObjectName("check_stu_openall")
        self.groupBox_4 = QtWidgets.QGroupBox(self.page)
        self.groupBox_4.setGeometry(QtCore.QRect(830, 0, 271, 631))
        self.groupBox_4.setObjectName("groupBox_4")
        self.te_eval_stu = QtWidgets.QTextEdit(self.groupBox_4)
        self.te_eval_stu.setGeometry(QtCore.QRect(0, 20, 261, 601))
        self.te_eval_stu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.te_eval_stu.setObjectName("te_eval_stu")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 261, 631))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 20, 241, 51))
        self.groupBox_6.setObjectName("groupBox_6")
        self.et_search_coa = QtWidgets.QLineEdit(self.groupBox_6)
        self.et_search_coa.setGeometry(QtCore.QRect(10, 20, 151, 20))
        self.et_search_coa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_search_coa.setObjectName("et_search_coa")
        self.bt_search_coa = QtWidgets.QPushButton(self.groupBox_6)
        self.bt_search_coa.setGeometry(QtCore.QRect(170, 20, 61, 23))
        self.bt_search_coa.setObjectName("bt_search_coa")
        self.tv_list_coa = QtWidgets.QTableView(self.groupBox_5)
        self.tv_list_coa.setGeometry(QtCore.QRect(10, 80, 241, 541))
        self.tv_list_coa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tv_list_coa.setObjectName("tv_list_coa")
        self.groupBox_13 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_13.setGeometry(QtCore.QRect(270, 0, 541, 631))
        self.groupBox_13.setObjectName("groupBox_13")
        self.tv_eval_coa = QtWidgets.QTreeWidget(self.groupBox_13)
        self.tv_eval_coa.setGeometry(QtCore.QRect(0, 40, 531, 581))
        self.tv_eval_coa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tv_eval_coa.setObjectName("tv_eval_coa")
        self.check_coa_openall = QtWidgets.QCheckBox(self.groupBox_13)
        self.check_coa_openall.setGeometry(QtCore.QRect(430, 20, 91, 19))
        self.check_coa_openall.setObjectName("check_coa_openall")
        self.lb_coa_eval_num_2 = QtWidgets.QLabel(self.groupBox_13)
        self.lb_coa_eval_num_2.setGeometry(QtCore.QRect(20, 20, 391, 16))
        self.lb_coa_eval_num_2.setObjectName("lb_coa_eval_num_2")
        self.groupBox_14 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_14.setGeometry(QtCore.QRect(820, 0, 281, 631))
        self.groupBox_14.setObjectName("groupBox_14")
        self.te_eval_coa = QtWidgets.QTextEdit(self.groupBox_14)
        self.te_eval_coa.setGeometry(QtCore.QRect(0, 20, 271, 601))
        self.te_eval_coa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.te_eval_coa.setObjectName("te_eval_coa")
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.groupBox_15 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_15.setGeometry(QtCore.QRect(0, 0, 371, 561))
        self.groupBox_15.setObjectName("groupBox_15")
        self.groupBox_16 = QtWidgets.QGroupBox(self.groupBox_15)
        self.groupBox_16.setGeometry(QtCore.QRect(10, 20, 351, 91))
        self.groupBox_16.setObjectName("groupBox_16")
        self.frame = QtWidgets.QFrame(self.groupBox_16)
        self.frame.setGeometry(QtCore.QRect(180, 20, 141, 21))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lb_year = QtWidgets.QLabel(self.frame)
        self.lb_year.setGeometry(QtCore.QRect(0, 0, 51, 21))
        self.lb_year.setObjectName("lb_year")
        self.cb_year = QtWidgets.QComboBox(self.frame)
        self.cb_year.setGeometry(QtCore.QRect(60, -2, 81, 21))
        self.cb_year.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_year.setObjectName("cb_year")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_16)
        self.frame_2.setGeometry(QtCore.QRect(10, 99, 120, 31))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_16)
        self.frame_3.setGeometry(QtCore.QRect(10, 60, 141, 21))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lb_week = QtWidgets.QLabel(self.frame_3)
        self.lb_week.setGeometry(QtCore.QRect(0, 0, 51, 19))
        self.lb_week.setObjectName("lb_week")
        self.cb_weekj = QtWidgets.QComboBox(self.frame_3)
        self.cb_weekj.setGeometry(QtCore.QRect(60, 0, 81, 21))
        self.cb_weekj.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.cb_weekj.setObjectName("cb_weekj")
        self.frame_4 = QtWidgets.QFrame(self.groupBox_16)
        self.frame_4.setGeometry(QtCore.QRect(170, 60, 151, 21))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lb_weekday = QtWidgets.QLabel(self.frame_4)
        self.lb_weekday.setGeometry(QtCore.QRect(10, 0, 41, 19))
        self.lb_weekday.setObjectName("lb_weekday")
        self.cb_weekday = QtWidgets.QComboBox(self.frame_4)
        self.cb_weekday.setGeometry(QtCore.QRect(70, -2, 81, 21))
        self.cb_weekday.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.cb_weekday.setObjectName("cb_weekday")
        self.lb_date = QtWidgets.QLabel(self.groupBox_16)
        self.lb_date.setGeometry(QtCore.QRect(20, 30, 161, 16))
        self.lb_date.setObjectName("lb_date")
        self.tv_classlist = QtWidgets.QTableView(self.groupBox_15)
        self.tv_classlist.setGeometry(QtCore.QRect(10, 120, 351, 431))
        self.tv_classlist.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tv_classlist.setObjectName("tv_classlist")
        self.groupBox_17 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_17.setGeometry(QtCore.QRect(380, 10, 711, 51))
        self.groupBox_17.setObjectName("groupBox_17")
        self.formLayoutWidget_6 = QtWidgets.QWidget(self.groupBox_17)
        self.formLayoutWidget_6.setGeometry(QtCore.QRect(20, 20, 201, 26))
        self.formLayoutWidget_6.setObjectName("formLayoutWidget_6")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_6)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.lb_stuname = QtWidgets.QLabel(self.formLayoutWidget_6)
        self.lb_stuname.setObjectName("lb_stuname")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_stuname)
        self.et_stuname = QtWidgets.QLineEdit(self.formLayoutWidget_6)
        self.et_stuname.setObjectName("et_stuname")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.et_stuname)
        self.formLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_17)
        self.formLayoutWidget_7.setGeometry(QtCore.QRect(260, 20, 201, 26))
        self.formLayoutWidget_7.setObjectName("formLayoutWidget_7")
        self.formLayout_7 = QtWidgets.QFormLayout(self.formLayoutWidget_7)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")
        self.lb_stuphone = QtWidgets.QLabel(self.formLayoutWidget_7)
        self.lb_stuphone.setObjectName("lb_stuphone")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_stuphone)
        self.et_stuphone = QtWidgets.QLineEdit(self.formLayoutWidget_7)
        self.et_stuphone.setObjectName("et_stuphone")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.et_stuphone)
        self.formLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_17)
        self.formLayoutWidget_8.setGeometry(QtCore.QRect(490, 20, 211, 26))
        self.formLayoutWidget_8.setObjectName("formLayoutWidget_8")
        self.formLayout_8 = QtWidgets.QFormLayout(self.formLayoutWidget_8)
        self.formLayout_8.setContentsMargins(0, 0, 0, 0)
        self.formLayout_8.setObjectName("formLayout_8")
        self.llv_stuclasstype = QtWidgets.QLabel(self.formLayoutWidget_8)
        self.llv_stuclasstype.setObjectName("llv_stuclasstype")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.llv_stuclasstype)
        self.et_stuclasstype = QtWidgets.QLineEdit(self.formLayoutWidget_8)
        self.et_stuclasstype.setObjectName("et_stuclasstype")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.et_stuclasstype)
        self.groupBox_18 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_18.setGeometry(QtCore.QRect(380, 70, 721, 51))
        self.groupBox_18.setObjectName("groupBox_18")
        self.formLayoutWidget_9 = QtWidgets.QWidget(self.groupBox_18)
        self.formLayoutWidget_9.setGeometry(QtCore.QRect(20, 20, 201, 26))
        self.formLayoutWidget_9.setObjectName("formLayoutWidget_9")
        self.formLayout_9 = QtWidgets.QFormLayout(self.formLayoutWidget_9)
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9.setObjectName("formLayout_9")
        self.lb_classdate = QtWidgets.QLabel(self.formLayoutWidget_9)
        self.lb_classdate.setObjectName("lb_classdate")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_classdate)
        self.et_classdate = QtWidgets.QLineEdit(self.formLayoutWidget_9)
        self.et_classdate.setObjectName("et_classdate")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.et_classdate)
        self.formLayoutWidget_10 = QtWidgets.QWidget(self.groupBox_18)
        self.formLayoutWidget_10.setGeometry(QtCore.QRect(260, 20, 201, 26))
        self.formLayoutWidget_10.setObjectName("formLayoutWidget_10")
        self.formLayout_10 = QtWidgets.QFormLayout(self.formLayoutWidget_10)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout_10.setObjectName("formLayout_10")
        self.lb_calsstime = QtWidgets.QLabel(self.formLayoutWidget_10)
        self.lb_calsstime.setObjectName("lb_calsstime")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_calsstime)
        self.et_classtime = QtWidgets.QLineEdit(self.formLayoutWidget_10)
        self.et_classtime.setObjectName("et_classtime")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.et_classtime)
        self.formLayoutWidget_11 = QtWidgets.QWidget(self.groupBox_18)
        self.formLayoutWidget_11.setGeometry(QtCore.QRect(490, 20, 211, 26))
        self.formLayoutWidget_11.setObjectName("formLayoutWidget_11")
        self.formLayout_11 = QtWidgets.QFormLayout(self.formLayoutWidget_11)
        self.formLayout_11.setContentsMargins(0, 0, 0, 0)
        self.formLayout_11.setObjectName("formLayout_11")
        self.lb_coaname = QtWidgets.QLabel(self.formLayoutWidget_11)
        self.lb_coaname.setObjectName("lb_coaname")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_coaname)
        self.et_coaname = QtWidgets.QLineEdit(self.formLayoutWidget_11)
        self.et_coaname.setObjectName("et_coaname")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.et_coaname)
        self.groupBox_19 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_19.setGeometry(QtCore.QRect(380, 120, 721, 501))
        self.groupBox_19.setObjectName("groupBox_19")
        self.et_eval_insert = QtWidgets.QTextEdit(self.groupBox_19)
        self.et_eval_insert.setGeometry(QtCore.QRect(10, 20, 701, 471))
        self.et_eval_insert.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.et_eval_insert.setObjectName("et_eval_insert")
        self.groupBox_20 = QtWidgets.QGroupBox(self.page_5)
        self.groupBox_20.setGeometry(QtCore.QRect(0, 570, 371, 51))
        self.groupBox_20.setTitle("")
        self.groupBox_20.setObjectName("groupBox_20")
        self.bt_confrim = QtWidgets.QPushButton(self.groupBox_20)
        self.bt_confrim.setGeometry(QtCore.QRect(40, 0, 101, 41))
        self.bt_confrim.setObjectName("bt_confrim")
        self.bt_clear = QtWidgets.QPushButton(self.groupBox_20)
        self.bt_clear.setGeometry(QtCore.QRect(200, 0, 111, 41))
        self.bt_clear.setObjectName("bt_clear")
        self.stackedWidget.addWidget(self.page_5)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listFunc.isSortingEnabled()
        self.listFunc.setSortingEnabled(False)
        item = self.listFunc.item(0)
        item.setText(_translate("Form", "评价展示和查询(学生)"))
        item = self.listFunc.item(1)
        item.setText(_translate("Form", "评价展示和查询(教练)"))
        item = self.listFunc.item(2)
        item.setText(_translate("Form", "评价录入和修改"))
        self.listFunc.setSortingEnabled(__sortingEnabled)
        self.label_13.setText(_translate("Form", "菜单栏"))
        self.groupBox_2.setTitle(_translate("Form", "学生列表"))
        self.groupBox.setTitle(_translate("Form", "功能菜单"))
        self.bt_search_stu.setText(_translate("Form", "查询"))
        self.groupBox_3.setTitle(_translate("Form", "评价列表"))
        self.lb_stu_eval_num.setText(_translate("Form", "没有评价信息！"))
        self.check_stu_openall.setText(_translate("Form", "全部展开"))
        self.groupBox_4.setTitle(_translate("Form", "评价内容"))
        self.groupBox_5.setTitle(_translate("Form", "教练列表"))
        self.groupBox_6.setTitle(_translate("Form", "功能菜单"))
        self.bt_search_coa.setText(_translate("Form", "查询"))
        self.groupBox_13.setTitle(_translate("Form", "评价列表"))
        self.check_coa_openall.setText(_translate("Form", "全部展开"))
        self.lb_coa_eval_num_2.setText(_translate("Form", "没有评价信息！"))
        self.groupBox_14.setTitle(_translate("Form", "评价内容"))
        self.groupBox_15.setTitle(_translate("Form", "课程选择"))
        self.groupBox_16.setTitle(_translate("Form", "日期"))
        self.lb_year.setText(_translate("Form", "  年份  "))
        self.lb_week.setText(_translate("Form", "  周次"))
        self.lb_weekday.setText(_translate("Form", " 周内  "))
        self.lb_date.setText(_translate("Form", "日期"))
        self.groupBox_17.setTitle(_translate("Form", "学生信息"))
        self.lb_stuname.setText(_translate("Form", "  学生姓名 "))
        self.lb_stuphone.setText(_translate("Form", "  联系方式 "))
        self.llv_stuclasstype.setText(_translate("Form", "  课程种类 "))
        self.groupBox_18.setTitle(_translate("Form", "课程信息"))
        self.lb_classdate.setText(_translate("Form", "  上课日期 "))
        self.lb_calsstime.setText(_translate("Form", "  上课时间 "))
        self.lb_coaname.setText(_translate("Form", "  教练姓名 "))
        self.groupBox_19.setTitle(_translate("Form", "评价录入"))
        self.bt_confrim.setText(_translate("Form", "确认录入"))
        self.bt_clear.setText(_translate("Form", "清空"))