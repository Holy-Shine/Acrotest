from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox, QLineEdit, QApplication, QTableView, QHeaderView
from qtpy import QtCore


from EvaluationSystem.EvaluationMain import Ui_Evaluation
import sys

class LogicEvaluationMain(Ui_Evaluation,QDialog):
    def __init__(self,MySQL):
        super().__init__()
        self.setupUi(self)
        self.MySQL = MySQL
        self.init()

    def init(self):
        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)


if __name__ == '__main__':
    import Login.CheckDBandFace as ckdf
    f1, MySQL = ckdf.CheckDB()
    MySQL.ConnectMySQL()
    app = QApplication(sys.argv)
    login = LogicEvaluationMain(MySQL=MySQL)
    login.show()
    sys.exit(app.exec_())