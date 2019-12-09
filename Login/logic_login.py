from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit

from Login.ui_login import UI_login
import os, json
import Login.CheckUserName as ckpwd

import Login.CheckDBandFace as ckdf
from  MainTest.Logic_Main import LogicMain

class logicLoginWin(UI_login,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



        self.lineEdit_pwd.setEchoMode(QLineEdit.Password)
        self.lineEdit_name.setPlaceholderText('请输入用户名')
        self.lineEdit_pwd.setPlaceholderText('请输入密码')
        self.btn_yes.clicked.connect(self.on_pushButton_enter_clicked)
        self.btn_yes.setDefault(True)
        self.btn_cancel.clicked.connect(self.on_pushButton_clear_clicked)
        
    def on_pushButton_clear_clicked(self):
        self.lineEdit_name.clear()
        self.lineEdit_pwd.clear()
                
    def on_pushButton_enter_clicked(self):
        try:
        # account judge
            name = self.lineEdit_name.text()
            pwd  = self.lineEdit_pwd.text()
            if  name== '':
                QMessageBox.warning(self, '提示','用户名不能为空！', QMessageBox.Yes, QMessageBox.Yes)
            elif pwd == '':
                QMessageBox.warning(self, '提示','密码不能为空！', QMessageBox.Yes, QMessageBox.Yes)

            elif ckpwd.login(password=pwd,username=name):
                self.accept()
                # print('登陆成功，当前用户名{}'.format(name))
                #检查数据库的连接情况
                flag,MySQL = ckdf.CheckDB()
                if not flag:
                    QMessageBox.warning(self, '提示', '数据库连接失败，请检查数据库！', QMessageBox.Yes, QMessageBox.Yes)
                flag,facefunction = ckdf.CheckFace()
                if not flag:
                    QMessageBox.warning(self, '提示', '人脸识别SDK错误，请检查！', QMessageBox.Yes, QMessageBox.Yes)
                self.LogicMain = LogicMain(MySQL= MySQL, facefunction= facefunction,user = name)
                self.LogicMain.show()



            else:
                QMessageBox.warning(self, '提示', '用户名或密码错误！', QMessageBox.Yes, QMessageBox.Yes)
        except Exception as e:
            print(e)