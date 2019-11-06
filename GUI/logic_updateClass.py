

from Ui_updateClass import Ui_updateClass
from PyQt5.QtWidgets import QDialog,QMessageBox,QTableWidgetItem
import sqlite3

class logicUpdateClass(Ui_updateClass, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.btn_flush.clicked.connect(self.on_button_flush)

    
    def on_button_flush(self):
        if self.cb_year.currentText()=='未选择' or self.comboBox.currentText()=='未选择':
            QMessageBox.warning(self, '提示','年和周未选!', QMessageBox.Yes, QMessageBox.Yes)
        else:
            sql = '''
                    SELECT mem_phone, mem_name FROM mem_info mi WHERE NOT EXISTS(
                SELECT * FROM mem_class  mc WHERE week=9
            )'''
            try:
                conn = sqlite3.connect('meminfo.db')
                c = conn.cursor()   
                c.execute(sql)
                
                rst = c.fetchall()
                for i,(mem_phone, mem_name) in enumerate(rst):
                    phone = QTableWidgetItem(str(mem_phone))
                    name = QTableWidgetItem(mem_name)
                    self.cb_mem_table.setItem(i,0,phone)
                    self.cb_mem_table.setItem(i,1,name)

                conn.commit()
                conn.close()
            except:
                QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)
                

        