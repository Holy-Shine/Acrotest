

from GUI.Ui_updateClass import Ui_updateClass
from PyQt5.QtWidgets import QDialog,QMessageBox,QTableView,QHeaderView, QListWidget, QStackedWidget
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import pymysql
from GUI.dbManager import dbManager

class logicUpdateClass(Ui_updateClass, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.beatify()

        self.current_row = -1
        self.cb_coach.setCurrentIndex(0)
        self.tv_show_mem.setEditTriggers(QTableView.NoEditTriggers) # 不可编辑
        self.tv_show_mem.setSelectionBehavior(QTableView.SelectRows) # 选中行
        

        # 设置背景
        # paletter = QPalette()
        # paletter.setBrush(QPalette.Background, QBrush(QPixmap('resource/paike_bg.png')))
        # self.setPalette(paletter)

        self.weekdays = ['周一','周二','周三','周四','周五','周六','周日']
        self.headers = ['联系方式','姓名','类型']
        self.data_model = QStandardItemModel()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        self.data = []
        self.tv_show_mem.setModel(self.data_model)
        self.tv_show_mem.selectionModel().selectionChanged.connect(self.row_sel_change) # 选中事件

        self.tv_show_mem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.btn_flush.clicked.connect(self.on_button_flush)
        self.btn_confirm.clicked.connect(self.on_button_confirm)

        self.cb_day_times = []
        self.coachs = []
        self.setupItem()
        self.listFunc.setCurrentRow(0)
        

    def beatify(self):

        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)   # list和右边窗口index绑定
        

        

    def on_button_confirm(self):
        if self.le_choose_phone.text()=='':
            QMessageBox.warning(self, '提示','未选择待排课学生!', QMessageBox.Yes, QMessageBox.Yes)
        else:
            # 检查是否未选择排课日期
            flag = True
            for cb in self.cb_day_times:
                flag = flag and (not cb.isChecked())
            if flag:
                QMessageBox.warning(self, '提示','未选择排课日期!', QMessageBox.Yes, QMessageBox.Yes)
            
            elif self.cb_coach.currentText()=='未选择':
                QMessageBox.warning(self, '提示','未选择教练!', QMessageBox.Yes, QMessageBox.Yes)
            
            else:

                str_confirm = '姓名：{}\n联系方式：{}\n教练：{}\n排课时间：\n   '.format(
                    self.le_choose_name.text(),
                    self.le_choose_phone.text(),
                    self.cb_coach.currentText()
                    )

                base = 10
                for i, cb in enumerate(self.cb_day_times):
                    if cb.isChecked():
                        day = i//12
                        time = str(base+i%12)
                        str_confirm+=(self.weekdays[day]+': '+time+':00'+'\n   ')

                reply = QMessageBox.warning(self, '确认信息',str_confirm, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

                # 插入数据库
                if reply == QMessageBox.Yes:
                    try:
                        dbm = dbManager()
                        base = 10
                        for i, cb in enumerate(self.cb_day_times):
                            if cb.isChecked():
                                day = i//12+1
                                time = base+i%12
                                sql = '''
                                INSERT INTO mem_class (mem_phone, mem_name, mem_coa_name, year, week, cday, ctime) VALUES(
                                    {},'{}','{}',{},{},{},{}
                                )
                                '''.format(
                                    self.le_choose_phone.text(),
                                    self.le_choose_name.text(),
                                    self.cb_coach.currentText(),
                                    self.cb_year.currentText(),
                                    self.cb_week.currentText(),
                                    day,
                                    time
                                )
                        
                                dbm.excuteSQL(sql)
                        # conn = sqlite3.connect('meminfo.db')
                        # c = conn.cursor()   
                        # c.execute(sql)
                        # conn.commit()
                        # conn.close()
                        for i in range(2):
                            self.data_model.setData(self.data_model.index(self.current_row, i), QBrush(Qt.green), Qt.BackgroundColorRole)
                        QMessageBox.information(self, '提示', '排课成功！',QMessageBox.Ok,QMessageBox.Ok)
                        
                        
                        
                        #删除选中行
                        current_row = self.tv_show_mem.currentIndex().row()
                        self.tv_show_mem.clearSelection()
                        self.data_model.removeRow(current_row)
                    except Exception as e:
                        print(e)
                        QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)
                else:
                    pass                
            


    def row_sel_change(self):
        current_row = self.tv_show_mem.currentIndex().row()
        print(current_row)
        if  current_row < len(self.data):
            selected_phone = str(self.data[current_row][0])
            selected_name = self.data[current_row][1]
            selected_type = int(self.data[current_row][2])
            self.le_choose_name.setText(selected_name)
            self.le_choose_phone.setText(selected_phone)
            self.current_row = current_row

            # 根据当前选中决定教练
            self.cb_coach.clear() # 先清空
            for coch in self.coachs:
                if coch[1]>=selected_type-1:
                    self.cb_coach.addItem(coch[0])
                    
        else:
            self.le_choose_name.setText('')
            self.le_choose_phone.setText('')

        self.clean_up()
        
        
        
    def clean_up(self):
        # 清除工作
        for i in range(84):
            self.cb_day_times[i].setChecked(False)

    def setupItem(self):
        sql = 'SELECT coa_name, coa_type FROM coach'
        try:

            dbm = dbManager()   
            coach = dbm.excuteSQL(sql)
            for coa_name, ctype in (coach):
                # self.cb_coach.addItem(coa_name[0])
                self.coachs.append([coa_name, int(ctype)])

        except Exception as e:
            print(e)
            QMessageBox.critical(self,'错误','数据库异常！无法连接到教练数据库',QMessageBox.Ok,QMessageBox.Ok)       



        # 将checkbox全部放入到cbs中
        for i in range(84):
            self.cb_day_times.append(eval('self.'+'cb_{}'.format(i)))

        self.clean_up()

    def on_button_flush(self):
        # 清空表
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        if self.cb_year.currentText()=='未选择' or self.cb_week.currentText()=='未选择':
            QMessageBox.warning(self, '提示','年和周未选!', QMessageBox.Yes, QMessageBox.Yes)
        else:
            week = self.cb_week.currentText()
            sql = '''SELECT mi.mem_phone, mi.mem_name, mi.mem_type FROM mem_info mi WHERE NOT EXISTS(
                SELECT mc.mem_phone, mc.mem_name FROM mem_class mc WHERE mi.mem_phone=mc.mem_phone and mi.mem_name=mc.mem_name and week={})'''.format(week)
            print(sql)
            try:

                dbm = dbManager()
                types = ['轮滑','平衡车']
                self.data = dbm.excuteSQL(sql)
                for i,(mem_phone, mem_name, mem_type) in enumerate(self.data):
                    self.data_model.appendRow([
                        QStandardItem(str(mem_phone)),
                        QStandardItem(mem_name),
                        QStandardItem(types[int(mem_type)//2])
                    ])

            except Exception as e:
                print(e)
                QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)

            # 若未更新不为空，则确认按钮可用
            if len(self.data)>0:
                self.btn_confirm.setEnabled(True)
            else:
                self.btn_confirm.setEnabled(False)
                

        