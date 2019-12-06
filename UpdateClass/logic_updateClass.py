from UpdateClass.Ui_updateClass import Ui_updateClass
from Date2Week.DateAndWeek import *
from PyQt5.QtWidgets import QDialog,QMessageBox,QTableView,QHeaderView, QListWidget, QStackedWidget
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import pymysql

class logicUpdateClass(Ui_updateClass, QDialog):
    def __init__(self, MySQL):
        super().__init__()
        self.setupUi(self)
        self.beatify()

        self.current_row = -1
        self.cb_coach.setCurrentIndex(0)
        self.tv_show_mem.setEditTriggers(QTableView.NoEditTriggers) # 不可编辑
        self.tv_show_mem.setSelectionBehavior(QTableView.SelectRows) # 选中行
        
        self.MySQL = MySQL
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

        self.cb_year.currentIndexChanged.connect(self.event_label_status_change)
        self.cb_week.currentIndexChanged.connect(self.event_label_status_change)

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
                sql_T = []
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
                        sql_T.append('T'+str(day)+time)

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

                        flag = self.MySQL.InsertFromDataBse(sql)
                        if (flag == True):
                            for i in range(2):
                                self.data_model.setData(self.data_model.index(self.current_row, i), QBrush(Qt.green),
                                                        Qt.BackgroundColorRole)
                            QMessageBox.information(self, '提示', '排课信息插入成功！', QMessageBox.Ok, QMessageBox.Ok)
                        else:
                            QMessageBox.information(self, '提示', '排课信息插入失败！', QMessageBox.Ok, QMessageBox.Ok)

                    except:
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
            self.cb_coach.addItem('未选择')
            for coch in self.coachs:
                if coch[1]==selected_type or coch[1]==2:
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
        from datetime import datetime as dt
        year = dt.now().year
        self.cb_year.clear()
        self.cb_year.addItems(['未选择',str(year),str(year+1)])

        try:
            flag,result = self.MySQL.SelectFromDataBse(sql)
            print(result)
            for coa_name, ctype in (result):
                self.cb_coach.addItem(coa_name)
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
                types = ['轮滑', '平衡车']
                flag, result = self.MySQL.SelectFromDataBse(sql)
                if (flag == True):
                    self.data = result
                    for i, (mem_phone, mem_name, mem_type) in enumerate(self.data):
                        self.data_model.appendRow([
                            QStandardItem(str(mem_phone)),
                            QStandardItem(mem_name),
                            QStandardItem(types[int(mem_type)])
                        ])
                else:
                    QMessageBox.information(self, '提示', '未排课信息查找失败！', QMessageBox.Ok, QMessageBox.Ok)

            except Exception as e:
                print(e)
                QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)

            # 若未更新不为空，则确认按钮可用
            if len(self.data)>0:
                self.btn_confirm.setEnabled(True)
            else:
                self.btn_confirm.setEnabled(False)


    def event_label_status_change(self):
        if self.cb_week.currentText()=='未选择' or self.cb_year.currentText()=='未选择':
            self.lb_status.setText('未选')

        else:
            year = int(self.cb_year.currentText())
            week = int(self.cb_week.currentText())
            F = FromWeektoDate(year,week,1)
            T = FromWeektoDate(year,week,7)
            text = '''{}-{}-{}至{}-{}-{}'''.format(F[0],F[1],F[2], T[0],T[1],T[2])
            self.lb_status.setText(text)

            if week == 1:
                weekday = getFirstWeekDate(year)
                
                # 使得一些日子不可用
                
                print(weekday)
                for i in range(1, int(weekday)):
                    eval('self.tb_{}'.format(i)).setEnabled(False)

            elif week == 52:
                weekday = getLastWeekDate(year)
            
                # 使得一些日子不可用
                
                print(weekday)
                for i in range(int(weekday)+1,8):
                    eval('self.tb_{}'.format(i)).setEnabled(False)

            else:
                for i in range(1,8):
                    eval('self.tb_{}'.format(i)).setEnabled(True)                
                
            
            