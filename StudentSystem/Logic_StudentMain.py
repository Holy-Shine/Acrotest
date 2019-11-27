from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from StudentSystem.StudentMain import Ui_StudentMain


class LogicStudentMain(Ui_StudentMain,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)