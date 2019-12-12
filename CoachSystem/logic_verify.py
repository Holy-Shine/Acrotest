
from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtCore import Qt
from CoachSystem.Ui_verify import Ui_verify
import json

class logicVerify(Ui_verify, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  

        self.btn_confirm.clicked.connect(self.on_button_verify)
        self.btn_confirm.setShortcut(Qt.Key_Return)

        self.load_verify()

    def load_verify(self):
        try:
            f = open('./BasicInfos/Verify.json', encoding='utf-8')
            user_dic = json.load(f)
            self.verify = user_dic['Verify'][0]['pwd']
        except Exception as e:
            print(e)
    def myshow(self):
        self.le_pwd.setText('')

    def on_button_verify(self):
        pwd = self.le_pwd.text()
        if pwd == self.verify:
            self.accept()
        else:
            QMessageBox.warning(self, '提示','二级密码错误！', QMessageBox.Yes, QMessageBox.Yes)