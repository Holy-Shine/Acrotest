from ui_newUser import Ui_newUser

from PyQt5.QtWidgets import QDialog, QMessageBox
from ui_newUser import Ui_newUser
import os,json
import pymysql,sqlite3


class logicNewUser(Ui_newUser, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.ctimes = ['1','2','3','4','5','6','7','8','9','10','11','12']
        # self.days = ['1','2','3','4','5','6','7']
        
        # self.cb_days = self.cb_time.qCheckBox
        # self.cb_ttimes = self.cb_time.qComboBox

        self.btn_insert.clicked.connect(self.on_pushButton_insert_clicked)
        self.btn_clear.clicked.connect(self.on_pushButton_clear_clicked)
        self.btn_newadd.clicked.connect(self.on_pushButton_clear_clicked)

    def on_pushButton_clear_clicked(self):
        self.edit_phone.clear()
        self.edit_name.clear()
        self.edit_parent.clear()    

    def on_pushButton_insert_clicked(self):

        # 检查完整性
        if self.edit_name.text() == '':
            QMessageBox.warning(self, '提示','新员工名字不能为空！', QMessageBox.Yes, QMessageBox.Yes)
        elif self.edit_phone.text() == '':
            QMessageBox.warning(self, '提示','新员工联系方式不能为空！', QMessageBox.Yes,QMessageBox.Yes)
        else:
            if self.cb_mem_type.currentText() == '学生':
                sql = 'INSERT INTO mem_info (mem_name, mem_gender, mem_parent, mem_phone, mem_type) VALUES(\'{}\',\'{}\',\'{}\',{},{})'.format(
                                        self.edit_name.text(), 
                                        self.cb_gender.currentText(), 
                                        self.edit_parent.text(), 
                                        self.edit_phone.text(),
                                        self.cb_type.currentText(),
                                    )


                
                hint = '学员姓名：{}\n性别：{}\n家长：{}\n联系方式：{}\n办卡类型：{}'.format(
                                        self.edit_name.text(), 
                                        self.cb_gender.currentText(), 
                                        self.edit_parent.text(), 
                                        self.edit_phone.text(),
                                        self.cb_type.currentText()
                                    )
            else:
                sql = 'INSERT INTO coach(coa_name, coa_phone) VALUES(\'{}\',{})'.format(
                                        self.edit_name.text(), 
                                        self.edit_phone.text(),
                                    )   
                hint = '教练姓名：{}\n联系方式：{}'.format(
                                        self.edit_name.text(), 
                                        self.edit_phone.text()
                                    )             
            reply = QMessageBox.warning(self, '确认信息',hint, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            print(sql)
            if reply == QMessageBox.Yes:
                try:
                    conn = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='1230456',
                        database = 'meminfo',
                        charset='utf8'
                    )
                    cursor = conn.cursor()
                    cursor.execute(sql)
                    conn.commit()
                    QMessageBox.information(self, '提示', '录入成功！',QMessageBox.Ok,QMessageBox.Ok)

                    conn.close()
                    # conn = sqlite3.connect('meminfo.db')
                    # c = conn.cursor()   
                    # c.execute(sql)
                    # conn.commit()
                    # conn.close()
                    # QMessageBox.information(self, '提示', '录入成功！',QMessageBox.Ok,QMessageBox.Ok)
                except:
                    QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)
            else:
                pass
            

    def closeEvent(self, event):

        # 清空
        self.edit_phone.setText('')
        self.edit_name.setText('')
        self.edit_parent.setText('')

            