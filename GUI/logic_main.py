from PyQt5.QtWidgets import QMessageBox,QMainWindow

from ui_mainWin import Ui_MainWindow
from logic_schUpdate import logicSchUpdate

class logicMainWin(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(logicMainWin, self).__init__()
        self.setupUi(self)
        self.search_update = logicSchUpdate()

        self.btn_search_update.clicked.connect(self.search_update.show)


    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
                                     "确定退出本系统吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()