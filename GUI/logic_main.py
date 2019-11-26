from PyQt5.QtWidgets import QMessageBox,QMainWindow
from PyQt5.QtCore import Qt

from ui_mainWin import Ui_mainWin
from logic_updateClass import logicUpdateClass
from logic_newUser import logicNewUser
from logic_sysCoach import logicSysCoach

class logicMainWin(Ui_mainWin, QMainWindow):
    def __init__(self):
        super(logicMainWin, self).__init__()
        self.setupUi(self)

        self.new_user = logicNewUser()
        self.new_user.setWindowModality(Qt.ApplicationModal)

        self.class_update = logicUpdateClass()
        self.sys_coach = logicSysCoach()
        self.class_update.setWindowModality(Qt.ApplicationModal)
        #self.btn_search_update.clicked.connect(self.search_update.show)
        self.btn_class_update.clicked.connect(self.class_update.myshow)

        self.btn_add_user.clicked.connect(self.new_user.show)
        self.btn_syscoach.clicked.connect(self.sys_coach.myshow)
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出本系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()