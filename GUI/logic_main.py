from PyQt5.QtWidgets import QMessageBox,QMainWindow
from PyQt5.QtCore import Qt

from ui_mainWin import Ui_MainWindow
from logic_schUpdate import logicSchUpdate
from logic_updateClass import logicUpdateClass
from logic_newUser import logicNewUser


class logicMainWin(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(logicMainWin, self).__init__()
        self.setupUi(self)

        self.new_user = logicNewUser()
        self.new_user.setWindowModality(Qt.ApplicationModal)

        self.search_update = logicSchUpdate()
        self.class_update = logicUpdateClass()
        self.class_update.setWindowModality(Qt.ApplicationModal)
        #self.btn_search_update.clicked.connect(self.search_update.show)
        self.btn_class_update.clicked.connect(self.class_update.myshow)

        self.btn_add_user.clicked.connect(self.new_user.show)
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出本系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()