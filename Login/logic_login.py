from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit

from Login.ui_login import UI_login
import os, json

class logicLoginWin(UI_login,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.user_params = self.load_name_pwd()


        self.lineEdit_pwd.setEchoMode(QLineEdit.Password)
        self.lineEdit_name.setPlaceholderText('请输入用户名')
        self.lineEdit_pwd.setPlaceholderText('请输入密码')
        self.btn_yes.clicked.connect(self.on_pushButton_enter_clicked)
        
        

    # 加载保存的用户名密码
    def load_name_pwd(self):
        user_params = None
        if os.path.exists('user_params.json'):
            user_params = json.load(open('user_params.json'))
            save_code = user_params['save_code']
            name = user_params['name']
            pwd = user_params['pwd']

            if save_code == True:
                self.lineEdit_name.setText(name)
                self.lineEdit_pwd.setText(pwd)
                self.checkbox_save.setChecked(save_code)
        
        return user_params

                
    def on_pushButton_enter_clicked(self):
        # account judge
        name = self.lineEdit_name.text()
        pwd  = self.lineEdit_pwd.text()
        if  name== '':
            QMessageBox.warning(self, '提示','用户名不能为空！', QMessageBox.Yes, QMessageBox.Yes)
        elif pwd == '':
            QMessageBox.warning(self, '提示','密码不能为空！', QMessageBox.Yes, QMessageBox.Yes)

        elif name == 'admin' and pwd == '123':
            self.accept()

            # 更新user_params状态
            if self.user_params!=None:
                self.user_params['save_code'] = self.checkbox_save.isChecked()
                json.dump(self.user_params,open('user_params.json','w'))
        else:
            QMessageBox.warning(self, '提示', '用户名或密码错误！', QMessageBox.Yes, QMessageBox.Yes)