from PyQt5.QtWidgets import QMessageBox,QMainWindow,QDialog

from ui_mainWin import Ui_MainWindow
from ui_daytime import Ui_classTime

class logicClassTime(Ui_classTime, QDialog):

    def __init__(self):
        super(logicClassTime, self).__init__()
        self.setupUi(self)
        self.btn_ok.clicked.connect(self.close)


    def on_button_time_selected_exit():
        pass