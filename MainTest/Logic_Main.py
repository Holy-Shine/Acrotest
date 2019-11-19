from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication,QStackedWidget

from MainTest import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets

from newMember.logic_Newmember import LogicNewMember
from GUI.logic_updateClass import logicUpdateClass
from newMember.logic_OldMember import LogicOldMember

import os,sys


class LogicMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LogicMain, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.init()
        self.slot_init()

    def init(self):
        self.stackedWidget = QStackedWidget()
        self.Layout.addWidget(self.stackedWidget)

        #子界面
        self.FormNewMember = LogicNewMember()
        self.FormLesson = logicUpdateClass()
        self.FormOldMember = LogicOldMember()

        self.stackedWidget.addWidget(self.FormNewMember)
        self.stackedWidget.addWidget(self.FormLesson)
        self.stackedWidget.addWidget(self.FormOldMember)

    def slot_init(self):
        #新学员录入系统嵌入
        self.pb_main_NewMemberSystem.clicked.connect(self.on_pb_main_NewMemberSystem_clicked)
        self.FormNewMember.lb_toOld.clicked.connect(self.on_pb_main_toOldMemberSystem_clicked)
        self.FormOldMember.lb_toNew.clicked.connect(self.on_pb_main_toNewMemberSystem_clicked)

        #排课系统嵌入
        self.pb_main_LessonSystem.clicked.connect(self.on_pb_main_LessonSystem_clicked)




    def on_pb_main_NewMemberSystem_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    def on_pb_main_LessonSystem_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def on_pb_main_toOldMemberSystem_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def on_pb_main_toNewMemberSystem_clicked(self):
        self.stackedWidget.setCurrentIndex(0)


    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出本系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LogicMain()
    window.show()
    sys.exit(app.exec_())
