from UpdateClass.Ui_updateClass import Ui_updateClass
from Date2Week.DateAndWeek import *
from PyQt5.QtWidgets import QDialog,QMessageBox,QTableView,QHeaderView, QListWidget, QStackedWidget
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import pymysql
from datetime import datetime as dt
from WorkThread.WorkThread import *

class logicUpdateClass(Ui_updateClass, QDialog):
    def __init__(self, MySQL):
        super().__init__()
        self.setupUi(self)
        self.beatify()

        self.current_row = -1
        self.cb_coach.setCurrentIndex(0)
        self.tv_show_mem.setEditTriggers(QTableView.NoEditTriggers) # 不可编辑
        self.tv_show_mem.setSelectionBehavior(QTableView.SelectRows) # 选中行
        self.tv_show_mem_3.setEditTriggers(QTableView.NoEditTriggers) # 不可编辑
        self.te_current_paike.setReadOnly(True)
        self.tv_show_mem_3.setSelectionBehavior(QTableView.SelectRows) # 选中行        
        self.MySQL = MySQL
        # 设置背景
        # paletter = QPalette()
        # paletter.setBrush(QPalette.Background, QBrush(QPixmap('resource/paike_bg.png')))
        # self.setPalette(paletter)
        self.sql_thread_2 = None

        self.weekdays = ['周一','周二','周三','周四','周五','周六','周日']
        self.headers = ['联系方式','姓名','类型']
        self.data_model = QStandardItemModel()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        self.data = []
        self.tv_show_mem.setModel(self.data_model)
        self.tv_show_mem.selectionModel().selectionChanged.connect(self.row_sel_change) # 选中事件

        self.data_model_2 = QStandardItemModel()
        self.data_model_2.setHorizontalHeaderLabels(self.headers)
        self.data_2 = []
        self.tv_show_mem_3.setModel(self.data_model_2)
        self.tv_show_mem_3.selectionModel().selectionChanged.connect(self.row_sel_change_2) # 选中事件

        self.cb_year.currentIndexChanged.connect(self.event_label_status_change)
        self.cb_week.currentIndexChanged.connect(self.event_label_status_change)

        self.cb_year_2.currentIndexChanged.connect(self.event_label_status_change_2)
        self.cb_week_2.currentIndexChanged.connect(self.event_label_status_change_2)


        self.listFunc.currentRowChanged.connect(self.event_left_rowSelected)
        self.listFunc.setCurrentRow(0)

        self.tv_show_mem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tv_show_mem_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.btn_flush.clicked.connect(self.on_button_flush)
        self.btn_confirm.clicked.connect(self.on_button_confirm)

        self.btn_confirm_2.clicked.connect(self.on_button_confirm_update)
        self.btn_upclass_search.clicked.connect(self.on_button_search_update)

        self.cb_day_times = []
        self.cb_day_times2 = []
        self.tbs_1 = []
        self.tbs_2 = []
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

                str_confirm = '姓名：{}\n联系方式：{}\n课程类型：{}\n教练：{}\n排课时间：\n   '.format(
                    self.le_choose_name.text(),
                    self.le_choose_phone.text(),
                    self.le_choose_type.text(),
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
                        types = ['轮滑','平衡车']
                        flag = True
                        for i, cb in enumerate(self.cb_day_times):
                            if cb.isChecked():
                                day = i//12
                                time = str(base+i%12)                                
                                sql = '''
                                INSERT INTO mem_class (mem_phone, mem_name,mem_type, mem_coa_name, year, week, cday, ctime) VALUES(
                                    '{}','{}',{},'{}',{},{},{},{}
                                )
                                '''.format(
                                    self.le_choose_phone.text(),
                                    self.le_choose_name.text(),
                                    types.index(self.le_choose_type.text()),
                                    self.cb_coach.currentText(),
                                    self.cb_year.currentText(),
                                    self.cb_week.currentText(),
                                    day+1,
                                    time
                                )

                                flag1 = self.MySQL.InsertFromDataBse(sql)
                                flag &= flag1
                        if (flag == True):
                            self.data_model.removeRow(self.tv_show_mem.currentIndex().row())
                            # for i in range(2):
                            #     self.data_model.setData(self.data_model.index(self.current_row, i), QBrush(Qt.green),
                            #                             Qt.BackgroundColorRole)
                            QMessageBox.information(self, '提示', '排课信息插入成功！', QMessageBox.Ok, QMessageBox.Ok)
                        else:
                            QMessageBox.information(self, '提示', '排课信息插入失败！', QMessageBox.Ok, QMessageBox.Ok)

                    except Exception as e:
                        print(e)
                        QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)
                else:
                    pass                
            




    def row_sel_change_2(self):

        types = ['轮滑','平衡车']
        current_row = self.tv_show_mem_3.currentIndex().row()
        if current_row < len(self.data_2):
            dt_txt = self.data_2[current_row][3]
            selected_phone = str(self.data_2[current_row][0])
            selected_name = self.data_2[current_row][1]
            selected_type = int(self.data_2[current_row][2])
            self.le_choose_name_3.setText(selected_name)
            self.le_choose_phone_3.setText(selected_phone)
            self.le_choose_type_3.setText(types[selected_type])  
            self.te_current_paike.setText(dt_txt)   

            # 清空checkbox
            for cb in self.cb_day_times2:
                cb.setChecked(False) 
            # 根据当前选中决定教练
            self.cb_coach_2.clear() # 先清空
            self.cb_coach_2.addItem('未选择')
            for coch in self.coachs:
                if coch[1]==selected_type or coch[1]==2:
                    self.cb_coach_2.addItem(coch[0])      


            # 重置当前cb和tb
            self.setAllTab(self.tbs_2)
            self.setAllCheckBox(self.cb_day_times2)

            # 修改checkbox
            times = dt_txt.split('\n')
            for daytime in times[1:]:
                week, time = daytime.split(': ')
                week_idx = self.weekdays.index(week)
                time_idx = int(time[:2])-10

                self.cb_day_times2[week_idx*12+time_idx].setChecked(True)
            
            # 检查当前日期，设置某些tab不可选
            year = dt.now().year
            month = dt.now().month
            day = dt.now().day

            cweek, cweekday = FromDatetoWeek(year, month, day)

            if int(self.cb_week_2.currentText())<cweek:  # 设置了过去的周，则均不可选
                self.setAllTab(self.tbs_2, enable=False)

            elif int(self.cb_week_2.currentText())==cweek:  # 若刚好是当前周次
                for i in range(0, int(cweekday)-1):
                    self.tbs_2[i].setEnabled(False)

            

    def row_sel_change(self):
        current_row = self.tv_show_mem.currentIndex().row()
        print(current_row)
        types = ['轮滑','平衡车']
        if  current_row < len(self.data):
            selected_phone = str(self.data[current_row][0])
            selected_name = self.data[current_row][1]
            selected_type = int(self.data[current_row][2])
            self.le_choose_name.setText(selected_name)
            self.le_choose_phone.setText(selected_phone)
            self.le_choose_type.setText(types[selected_type])
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
        self.cb_year_2.clear()
        self.cb_year.addItems(['未选择',str(year),str(year+1)])
        self.cb_year_2.addItems(['未选择',str(year), str(year+1)])

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
            self.cb_day_times2.append(eval('self.cb_{}_2'.format(i)))


        # 将两个tab全部放入tab中
        for i in range(1,8):
            self.tbs_1.append(eval('self.tb_{}'.format(i)))
            self.tbs_2.append(eval('self.tb_{}_2'.format(i)))


        self.clean_up()

    def on_button_search_update(self):
        # 校验
        if self.cb_year_2.currentText()=='未选择' or self.cb_week_2.currentText()=='未选择':
            QMessageBox.information(self,'提示','未选年和周！',QMessageBox.Ok,QMessageBox.Ok)
        elif self.le_upclass_term.text()=='':
            QMessageBox.information(self,'提示','查询关键词不能为空！',QMessageBox.Ok,QMessageBox.Ok)
        
        else:
            year = self.cb_year_2.currentText()
            week = self.cb_week_2.currentText()
            search_term = self.le_upclass_term.text()

            # 查询未签到的排课数据
            sql = '''
            SELECT * FROM mem_class WHERE year={} and week={} and (mem_phone like '%{}%' OR mem_name like '%{}%') and mem_signed=0
            '''.format(year, week,search_term, search_term)

            self.btn_upclass_search.setEnabled(False)
            self.btn_confirm_2.setEnabled(False)
            self.sql_thread_2 = MySQLThread(self.MySQL, sql)
            self.sql_thread_2.trigger.connect(self.on_thread_getSearchData)
            self.sql_thread_2.start()



    def on_button_confirm_update(self):
        # 校验
        current_row = self.tv_show_mem_3.currentIndex().row()
        if current_row == -1:
            QMessageBox.information(self,'提示','未选择任何学员',QMessageBox.Ok,QMessageBox.Ok)

        else:
            # 拿到选中信息
            types = ['轮滑', '平衡车']
            name = self.le_choose_name_3.text()
            phone = self.le_choose_phone_3.text()
            type = types.index(self.le_choose_type_3.text())
            year = self.cb_year_2.currentText()
            week = self.cb_week_2.currentText()

            # 检查 checkbox
            flag = False
            for cb in self.cb_day_times2:
                flag |= cb.isChecked()

            dl_sql = '''
            DELETE FROM mem_class WHERE mem_name='{}' and mem_phone='{}' and mem_type={} and year={} and week={} and mem_signed=0
            '''.format(name, phone, type, year, week)
            if flag == False:
                # 删除排课


                hint = '''确认删除【{}】在第{}年第{}周的所有未签到安排吗？
                '''.format(name, year, week)

                reply = QMessageBox.warning(self, '确认信息',hint, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

                if reply == QMessageBox.Yes:
                    flag = self.MySQL.DeleteFromDataBse(dl_sql)
                    if flag:
                        QMessageBox.information(self, '提示','删除成功', QMessageBox.Ok)

            else:
                if self.cb_coach_2.currentText()=='未选择':
                    QMessageBox.warning(self, '提示','未选择教练!', QMessageBox.Yes, QMessageBox.Yes)
                
                else:
                    
                    str_confirm = '姓名：{}\n联系方式：{}\n课程类型：{}\n教练：{}\n排课时间：\n   '.format(
                        name,
                        phone,
                        self.le_choose_type_3.text(),
                        self.cb_coach_2.currentText()
                        )
                    base = 10
                    for i, cb in enumerate(self.cb_day_times2):
                        if cb.isChecked():
                            day = i//12
                            time = str(base+i%12)
                            str_confirm+=(self.weekdays[day]+': '+time+':00'+'\n   ')

                    reply = QMessageBox.warning(self, '确认信息',str_confirm, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

                    # 插入数据库
                    if reply == QMessageBox.Yes:
                        try:
                            # 先删除
                            self.MySQL.DeleteFromDataBse(dl_sql)
                            types = ['轮滑','平衡车']
                            flag = True
                            for i, cb in enumerate(self.cb_day_times2):
                                if cb.isChecked():
                                    day = i//12
                                    time = str(base+i%12)                                
                                    sql = '''
                                    INSERT INTO mem_class (mem_phone, mem_name,mem_type, mem_coa_name, year, week, cday, ctime) VALUES(
                                        '{}','{}',{},'{}',{},{},{},{}
                                    )
                                    '''.format(
                                        phone,
                                        name,
                                        types.index(self.le_choose_type_3.text()),
                                        self.cb_coach_2.currentText(),
                                        year,
                                        week,
                                        day+1,
                                        time
                                    )

                                    flag1 = self.MySQL.InsertFromDataBse(sql)
                                    flag &= flag1
                            if (flag == True):
                                self.data_model_2.removeRow(self.tv_show_mem_3.currentIndex().row())
                                # for i in range(2):
                                #     self.data_model.setData(self.data_model.index(self.current_row, i), QBrush(Qt.green),
                                #                             Qt.BackgroundColorRole)
                                QMessageBox.information(self, '提示', '排课信息插入成功！', QMessageBox.Ok, QMessageBox.Ok)
                            else:
                                QMessageBox.information(self, '提示', '排课信息插入失败！', QMessageBox.Ok, QMessageBox.Ok)
                        
                        except Exception as e:
                            print(e)
                            QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)


                    

                
                

        

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

    def event_left_rowSelected(self):
        current_row = self.listFunc.currentIndex().row()
        # 按周次排课

        if current_row == 0:
            pass

        # 更新排课信息
        elif current_row ==1:
            pass
           # cyear = dt.now().year
         


        
    
    def event_label_status_change_2(self):
        if self.cb_week_2.currentText()=='未选择' or self.cb_year_2.currentText()=='未选择':
            self.lb_status_2.setText('未选')

        else:
            for cb in self.cb_day_times2:
                cb.setChecked(False)
            year = int(self.cb_year_2.currentText())
            week = int(self.cb_week_2.currentText())-1
            F = FromWeektoDate(year,week,1)
            T = FromWeektoDate(year,week,7)


            begin_m = F[1]
            begin_d = F[2]
            end_m = T[1]
            end_d = T[2]

            for i in range(1,8):
                eval('self.tb_{}_2'.format(i)).setEnabled(True)   
            if week == 0:
                weekday = getFirstWeekDate(year)
                
                # 使得一些日子不可用
                begin_d = 1
                begin_m = 1
                for i in range(1, int(weekday)):
                    eval('self.tb_{}_2'.format(i)).setEnabled(False)

            elif week == 52:
                weekday = getLastWeekDate(year)
            
                # 使得一些日子不可用
                
                end_m =12
                end_d = 31
                print(weekday)
                for i in range(int(weekday)+1,8):
                    eval('self.tb_{}_2'.format(i)).setEnabled(False)

        







            text = '''{}-{}-{}至{}-{}-{}'''.format(year,begin_m,begin_d, year,end_m,end_d)
            self.lb_status_2.setText(text)    

    def event_label_status_change(self):
        if self.cb_week.currentText()=='未选择' or self.cb_year.currentText()=='未选择':
            self.lb_status.setText('未选')

        else:
            for cb in self.cb_day_times:
                cb.setChecked(False)
            year = int(self.cb_year.currentText())
            week = int(self.cb_week.currentText())-1
            F = FromWeektoDate(year,week,1)
            T = FromWeektoDate(year,week,7)

            begin_m = F[1]
            begin_d = F[2]
            end_m = T[1]
            end_d = T[2]

            for i in range(1,8):
                eval('self.tb_{}'.format(i)).setEnabled(True)

            if week == 0:
                weekday = getFirstWeekDate(year)
                
                # 使得一些日子不可用
                begin_d=1
                begin_m=1
                for i in range(1, int(weekday)):
                    eval('self.tb_{}'.format(i)).setEnabled(False)

            elif week == 52:
                weekday = getLastWeekDate(year)
            
                # 使得一些日子不可用
                end_d=31
                end_m=12
                print(weekday)
                for i in range(int(weekday)+1,8):
                    eval('self.tb_{}'.format(i)).setEnabled(False)

   

            text = '''{}-{}-{}至{}-{}-{}'''.format(year,begin_m,begin_d, year,end_m,end_d)
            self.lb_status.setText(text)             
                
            
    def on_thread_getSearchData(self, data):
        self.data_model_2.clear()
        self.data_model_2.setHorizontalHeaderLabels(self.headers)
        if len(data)>0:
            weeks = ['周一','周二','周三','周四','周五','周六','周日']
            types = ['轮滑', '平衡车']
            self.data_2 = []
            day_times = '{}年第{}周: '.format(self.cb_year_2.currentText(), self.cb_week_2.currentText())

            rst_dic = {}
            for i,line in enumerate(data):
                key = tuple([line[0], line[1], line[2]])
                if key not in rst_dic:
                    rst_dic[key] = day_times
                rst_dic[key]+= '\n{}: {}:00'.format(weeks[line[6]-1], line[7])

            
            for i, key in enumerate(rst_dic):
                self.data_2.append([key[0], key[1], key[2], rst_dic[key]])
                self.data_model_2.appendRow([
                    QStandardItem(key[0]),
                    QStandardItem(key[1]),
                    QStandardItem(types[key[2]])
                ])
            self.lb_sch_status_2.setText('查找状态：当前找到{}条记录'.format(len(self.data_2)))
        self.btn_upclass_search.setEnabled(True)
        self.btn_confirm_2.setEnabled(True)



################################################ 重置/设置函数区 ###################################################
    def setAllCheckBox(self, cbs, checked=False):
        for cb in cbs:
            cb.setChecked(checked)

    def setAllTab(self, tbs, enable=True):
        for tb in tbs:
            tb.setEnabled(enable)


    def myclear(self):
        # 页签1清空
        self.data = []
        self.data_model.clear()
        self.data_model.setHorizontalHeaderLabels(self.headers)
        self.le_choose_name.clear()
        self.le_choose_phone.clear()
        self.le_choose_type.clear()
        self.cb_year.setCurrentIndex(0)
        self.cb_week.setCurrentIndex(0)
        self.cb_coach.clear()
        self.setAllTab(self.tbs_1)
        self.setAllCheckBox(self.cb_day_times)

        # 页签2清空
        self.data_2 = []
        self.data_model_2.clear()
        self.data_model_2.setHorizontalHeaderLabels(self.headers)
        self.le_choose_name_3.clear()
        self.le_choose_phone_3.clear()
        self.le_choose_type_3.clear()
        self.cb_year_2.setCurrentIndex(0)
        self.cb_week_2.setCurrentIndex(0)
        self.cb_coach_2.clear()
        self.setAllTab(self.tbs_2)
        self.setAllCheckBox(self.cb_day_times2)  
        self.le_upclass_term.clear()
        self.lb_sch_status_2.setText('查找状态：当前找到0条记录')

        self.listFunc.setCurrentRow(0)  # 选中第一个页签


        