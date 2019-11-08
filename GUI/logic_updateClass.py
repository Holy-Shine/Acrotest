

from Ui_updateClass import Ui_updateClass
from PyQt5.QtWidgets import QDialog,QMessageBox,QTableView,QHeaderView
from PyQt5.QtGui import QStandardItemModel,QStandardItem

import sqlite3

class logicUpdateClass(Ui_updateClass, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setupItem()
        self.current_row = -1
        self.cb_coach.setCurrentIndex(0)
        self.tv_show_mem.setEditTriggers(QTableView.NoEditTriggers) # 不可编辑
        self.tv_show_mem.setSelectionBehavior(QTableView.SelectRows) # 选中行
        

        self.headers = ['联系方式','姓名']
        self.data_model = QStandardItemModel()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        self.data = []
        self.tv_show_mem.setModel(self.data_model)
        self.tv_show_mem.selectionModel().selectionChanged.connect(self.row_sel_change) # 选中事件

        self.tv_show_mem.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        
        self.btn_flush.clicked.connect(self.on_button_flush)
        self.btn_confirm.clicked.connect(self.on_button_confirm)

    def on_button_confirm(self):
        if self.le_choose_phone.text()=='':
            QMessageBox.warning(self, '提示','未选择待排课学生!', QMessageBox.Yes, QMessageBox.Yes)
        else:
            # 检查是否未选择排课日期
            flag = True
            for cb in self.cb_day.qCheckBox:
                flag = flag and (not cb.isChecked())
            if flag:
                QMessageBox.warning(self, '提示','未选择排课日期!', QMessageBox.Yes, QMessageBox.Yes)
            
            else:
                sql_T = []
                str_confirm = '姓名：{}\n联系方式：{}\n教练：{}\n排课时间：\n   '.format(
                    self.le_choose_name.text(),
                    self.le_choose_phone.text(),
                    self.cb_coach.currentText()
                    )

                for i, cb in enumerate(self.cb_day.qCheckBox):
                    if cb.isChecked():
                        str_confirm+=(cb.text()+': '+self.cb_day.qComboBox[i].currentText()+'\n   ')
                        sql_T.append('T'+str(i+1)+self.cb_day.qComboBox[i].currentText()[:2])

                reply = QMessageBox.warning(self, '确认信息',str_confirm, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

                # 插入数据库
                if reply == QMessageBox.Yes:
                    try:
                        sql = '''
                        INSERT INTO mem_class (mem_phone, mem_name, mem_coa_name, year, week, ctime) VALUES(
                            {},'{}','{}',{},{},'{}'
                        )
                        '''.format(
                            self.le_choose_phone.text(),
                            self.le_choose_name.text(),
                            self.cb_coach.currentText(),
                            self.cb_year.currentText(),
                            self.cb_week.currentText(),
                            ','.join(sql_T)
                        )
                        conn = sqlite3.connect('meminfo.db')
                        c = conn.cursor()   
                        c.execute(sql)
                        conn.commit()
                        conn.close()
                        QMessageBox.information(self, '提示', '排课成功！',QMessageBox.Ok,QMessageBox.Ok)
                        
                        #删除选中行
                        # self.tv_show_mem.clearSelection()
                        # self.data_model.removeRow(self.current_row)
                    except:
                        QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)
                else:
                    pass                
            


    def row_sel_change(self):
        idxs = self.tv_show_mem.selectionModel().selection().indexes()
        selected_phone = str(self.data[idxs[0].row()][0])
        selected_name = self.data[idxs[0].row()][1]
        self.le_choose_name.setText(selected_name)
        self.le_choose_phone.setText(selected_phone)
        self.current_row = self.tv_show_mem.currentIndex().row()
        
        

    def setupItem(self):
        sql = 'SELECT coa_name FROM coach'
        try:
            conn = sqlite3.connect('meminfo.db')
            c = conn.cursor()   
            c.execute(sql)
            
            coanames = c.fetchall()
            for coa_name in (coanames):
                self.cb_coach.addItem(coa_name[0])

            conn.commit()
            conn.close()
        except:
            QMessageBox.critical(self,'错误','数据库异常！无法连接到教练数据库',QMessageBox.Ok,QMessageBox.Ok)       


    def on_button_flush(self):
        # 清空表
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        if self.cb_year.currentText()=='未选择' or self.cb_week.currentText()=='未选择':
            QMessageBox.warning(self, '提示','年和周未选!', QMessageBox.Yes, QMessageBox.Yes)
        else:
            week = self.cb_week.currentText()
            sql = '''SELECT mi.mem_phone, mi.mem_name FROM mem_info mi WHERE NOT EXISTS(
                SELECT mc.mem_phone, mc.mem_name FROM mem_class mc WHERE mi.mem_phone=mc.mem_phone and mi.mem_name=mc.mem_name and week={})'''.format(week)
            print(sql)
            try:
                conn = sqlite3.connect('meminfo.db')
                c = conn.cursor()   
                c.execute(sql)
                
                self.data = c.fetchall()
                for i,(mem_phone, mem_name) in enumerate(self.data):
                    self.data_model.appendRow([
                        QStandardItem(str(mem_phone)),
                        QStandardItem(mem_name)
                    ])

                conn.commit()
                conn.close()
            except:
                QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)
                

        