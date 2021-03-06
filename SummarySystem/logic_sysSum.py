from SummarySystem.Ui_sumSys import Ui_sumSys
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
import time
import numpy as np


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D


# 中文问题
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

from datetime import datetime as dt

# 多线程数据库

from WorkThread.WorkThread import *

class logicSysSum(QMainWindow, Ui_sumSys):
    def __init__(self, MySQL, parent=None):
        super(logicSysSum, self).__init__(parent)


        self.setupUi(self)
        self.MySQL = MySQL

        # 办卡人数-柱状图横纵坐标数据
        self.bar_x = np.array([1,2])
        self.bar_org_y = np.array([0,0])
        self.bar_y = np.array([100,200])

        self.fulid_selected_month = []
        self.fulid_selected_month_2=[]



        

        self.time_limit = 30   # 更新50次

        self.sql_thread = None
        self.excel_thread = None

        self.sql_thread_BXnum = None

        
        # 办卡续卡流水界面的相关初始化
        self.tv_fluid.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.fluid_headers = ['联系方式','姓名','办/续卡','办/续卡金额','办/续卡日期']
        self.fluid_data_model = QStandardItemModel()
        self.fluid_data_model.setHorizontalHeaderLabels(self.fluid_headers)
        self.fluid_data = []
        self.tv_fluid.setModel(self.fluid_data_model)
        self.tv_fluid.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 入库出库流水界面的相关初始化
        self.tv_fluid_2.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑
        self.fluid_headers_inout = ['货物名','价格','数量','出/入库','操作日期']
        self.fluid_data_model_inout = QStandardItemModel()
        self.fluid_data_model_inout.setHorizontalHeaderLabels(self.fluid_headers)
        self.fluid_data_inout = []
        self.tv_fluid_2.setModel(self.fluid_data_model_inout)
        self.tv_fluid_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)        



        # 按钮事件绑定        
        self.btn_show_bar.clicked.connect(self.on_btn_showhis)
        self.btn_show_BXline.clicked.connect(self.on_btn_show_BXline)
        self.btn_show_MoneyLine.clicked.connect(self.on_btn_showMoney)
        self.btn_fluid_getDB.clicked.connect(self.on_btn_getBXfluid)
        self.btn_fluid_excrt.clicked.connect(self.on_btn_save_crt_fluid)
        self.btn_fluid_expall.clicked.connect(self.on_btn_save_all_fluid)
        self.btn_show_inout_bar.clicked.connect(self.on_btn_showInout)
        self.btn_show_inoutLine.clicked.connect(self.on_btn_showInout_his)

        self.btn_fluid_getDB_2.clicked.connect(self.on_btn_getBXfluid_2)
        self.btn_fluid_excrt_2.clicked.connect(self.on_btn_save_crt_fluid_2)
        self.btn_fluid_expall_2.clicked.connect(self.on_btn_save_all_fluid_2)

        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listFunc.currentRowChanged.connect(self.event_left_rowSelected)
        self.listFunc.setCurrentRow(0)


        self.Init_Widgets()


    def get_Bar_data(self, year, month):

        sql_date = '%{}-{}-%'.format(year,month)
        sql_bk = '''
        SELECT COUNT(*) FROM banka AS bk where bk.banka_type=0 and bk.banka_date like '{}'
        '''.format(sql_date)
        sql_xk = '''
        SELECT COUNT(*) FROM banka AS bk where bk.banka_type=1 and bk.banka_date like '{}'
        '''.format(sql_date)

        try:
            # 查询当月办卡续卡
            flag = True
            flag_bk,result_bk = self.MySQL.SelectFromDataBse(sql_bk)
            flag_xk,result_xk = self.MySQL.SelectFromDataBse(sql_xk)
            flag &= flag_bk
            flag &= flag_xk 
            
            if (flag):
                bk = result_bk[0][0] if result_bk[0][0]!=None else 0
                xk = result_xk[0][0] if result_xk[0][0]!=None else 0
                self.bar_y = np.array([bk,xk])
                
            else:
                QMessageBox.information(self, '提示', '查询失败！', QMessageBox.Ok, QMessageBox.Ok)

        except Exception as e:
            print(e)
            QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)          


    def get_BX_line_data(self, cur_year, cur_month, num_months):
        self.BX_line_x = []
        self.BX_line_ybk = []
        self.BX_line_yxk = []
        self.BX_line_xticks = []
        months = [1,2,3,4,5,6,7,8,9,10,11,12]

        try:
            flag = True    
            # 查询近n个月的办卡续卡人数
            for i in range(num_months-1,-1,-1):
                month = months[cur_month-i-1]
                year = cur_year
                if cur_month-i<0:
                    year -= 1
                sql = '''
                SELECT COUNT(*) FROM banka AS bk where bk.banka_type=0 and bk.banka_date like '%{}-{}-%'
                '''.format(year, month)

                flag_bkhi, result_bkhis = self.MySQL.SelectFromDataBse(sql)
                sql = '''
                SELECT COUNT(*) FROM banka AS bk where bk.banka_type=1 and bk.banka_date like '%{}-{}-%'
                '''.format(year, month)

                flag_xkhi, result_xkhis = self.MySQL.SelectFromDataBse(sql)
                   

                flag &= flag_bkhi
                flag &= flag_xkhi

                if (flag):
                    ybk = result_bkhis[0][0] if result_bkhis[0][0]!=None else 0
                    yxk = result_xkhis[0][0] if result_xkhis[0][0]!=None else 0
                    self.BX_line_ybk.append(ybk)
                    self.BX_line_yxk.append(yxk)
                    self.BX_line_xticks.append('{}-{}'.format(year,month)) 
                    
                else:
                    QMessageBox.information(self, '提示', '查询失败！', QMessageBox.Ok, QMessageBox.Ok)

        except Exception as e:
            print(e)
            QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)        


    def get_Money_Line_data(self, cur_year, cur_month, num_months):
        self.line_y = []
        self.line_xticks = []

        months = [1,2,3,4,5,6,7,8,9,10,11,12]

        try:
            flag = True    
            # 查询近n个月的办卡续卡人数
            for i in range(num_months-1,-1,-1):
                month = months[cur_month-i-1]
                year = cur_year
                if cur_month-i<0:
                    year -= 1
                sql = '''
                SELECT SUM(banka_fee) FROM banka AS bk where bk.banka_date like '%{}-{}-%'
                '''.format(year, month)

                flag1, result= self.MySQL.SelectFromDataBse(sql)

                flag &= flag1

                if (flag):
                    if result[0][0] == None:
                        self.line_y.append(0)
                    else:
                        self.line_y.append(int(result[0][0]))
                    self.line_xticks.append('{}-{}'.format(year,month)) 
                    
                else:
                    QMessageBox.information(self, '提示', '查询失败！', QMessageBox.Ok, QMessageBox.Ok)

        except Exception as e:
            print(e)
            QMessageBox.critical(self,'错误','数据库异常！',QMessageBox.Ok,QMessageBox.Ok)         


    def event_left_rowSelected(self):
        current_row = self.listFunc.currentIndex().row()

        # 办卡续卡统计
        if current_row == 0:
            self.BX_num_month = 6  # 默认展示6个月的历史数据
            
            self.cur_year = dt.now().year
            self.cur_month = dt.now().month
            self.bar_year = dt.now().year
            self.bar_month = dt.now().month

            self.cb_bar_year.setItemText(0, str(self.cur_year-2))
            self.cb_bar_year.setItemText(1, str(self.cur_year-1))
            self.cb_bar_year.setItemText(2, str(self.cur_year))
            # self.get_Bar_data(self.cur_year, self.cur_month)  #获取当月的bar数据
            # self.get_BX_line_data(self.cur_year, self.cur_month, self.BX_num_month) # 获取BX数据         
        # 营业额统计
        elif current_row == 1:
            pass

        # 办卡续卡流水
        elif current_row == 2:

            if len(self.fluid_data)==0:
                self.btn_fluid_excrt.setEnabled(False)


            
            # 初始化年
            self.cb_fluid_year.clear()
            self.cb_fluid_year.addItems([str(self.cur_year-2),str(self.cur_year-1),str(self.cur_year)])
            self.cb_fluid_year.setCurrentIndex(2)

        # 入库出库统计
        elif current_row == 3:
            self.inout_num_month = 6  # 默认展示6个月的历史数据
            
            self.cur_year = dt.now().year
            self.cur_month = dt.now().month
            self.bar_year = dt.now().year
            self.bar_month = dt.now().month

            self.cb_bar_inout_year.setItemText(0, str(self.cur_year-2))
            self.cb_bar_inout_year.setItemText(1, str(self.cur_year-1))
            self.cb_bar_inout_year.setItemText(2, str(self.cur_year))

        # 出库入库流水
        elif current_row == 4:

            if len(self.fluid_data_inout)==0:
                self.btn_fluid_excrt_2.setEnabled(False)


            
            # 初始化年
            self.cb_fluid_year_2.clear()
            self.cb_fluid_year_2.addItems([str(self.cur_year-2),str(self.cur_year-1),str(self.cur_year)])
            self.cb_fluid_year_2.setCurrentIndex(2)
            




    def banka_setAx(self):
        self.BarFigure.ax.set_xlim(0,4)
        self.BarFigure.ax.set_ylim(0,max(2*np.max(self.bar_y),50))
        self.BarFigure.ax.set_xticks([1.2,2.2])
        self.BarFigure.ax.set_xticklabels(['办卡人数','续卡人数'])
        self.BarFigure.ax.set_title('{}年{}月办卡续卡人数统计'.format(self.bar_year, self.bar_month))
        self.BarFigure.ax.set_ylabel('人数(人)')
       # self.BarFigure.ax.text(1.2,201,'123', fontsize=20)
        

        self.bar = self.BarFigure.ax.bar(self.bar_x, self.bar_org_y, width=0.4)

        self.patches = self.bar.patches


    def money_setAx(self):
        self.LineFigure.ax.set_xlim(0, self.Money_num_month+1)

        margin = (max(self.line_y)-min(self.line_y))/10
        self.LineFigure.ax.set_ylim(min(self.line_y)-margin, max(self.line_y)+margin)
        self.line_xlis = []
        self.line_ylis = []

        self.line = Line2D(self.line_xlis, self.line_ylis, marker='o')
        self.LineFigure.ax.add_line(self.line)
        self.LineFigure.ax.set_ylabel('营业额（单位元）')
        self.LineFigure.ax.set_title('近{}个月的营业额'.format(self.Money_num_month))
        self.LineFigure.ax.set_xticks(range(1,self.Money_num_month+2))
        self.LineFigure.ax.set_xticklabels(self.line_xticks)

    def BX_setAx(self):
        self.BXLineFigure.ax.set_xlim(0, self.BX_num_month+1)

        margin = (max(self.BX_line_ybk+self.BX_line_yxk)-min(self.BX_line_ybk+self.BX_line_yxk))/10
        self.BXLineFigure.ax.set_ylim(min(self.BX_line_ybk+self.BX_line_yxk)-margin, max(self.BX_line_ybk+self.BX_line_yxk)+margin)

        self.timer_BX_line_x = []
        self.timer_BX_line_ybk = []
        self.timer_BX_line_yxk = []

        self.BXline_bk = Line2D(self.timer_BX_line_x, self.timer_BX_line_ybk, marker='^')
        self.BXline_xk = Line2D(self.timer_BX_line_x, self.timer_BX_line_yxk, marker='o')

        
        self.BXLineFigure.ax.add_line(self.BXline_bk)
        self.BXLineFigure.ax.add_line(self.BXline_xk)

        self.BXLineFigure.ax.set_xticks(range(1,self.BX_num_month+2))
        self.BXLineFigure.ax.set_xticklabels(self.BX_line_xticks)


        

    # 按钮事件
    def on_btn_show_BXline(self):
        self.BX_num_month = (self.cb_show_num_month.currentIndex()+1)*3
        self.get_BX_line_data(self.cur_year, self.cur_month, self.BX_num_month) # 获取BX数据 
        self.BXLineFigure.ax.cla()
        self.BX_setAx()
        self.BXct = 0
        self.timerBX = QTimer()
        self.timerBX.start(1)
        self.timerBX.timeout.connect(self.BXLineUpdate)


    def on_btn_showInout_his(self):
        num_show_inout_his = (self.cb_show_num_month_2.currentIndex()+1)*3
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        cur_year = self.cur_year
        cur_month = self.cur_month
        print(num_show_inout_his)
        try:
            # 查询近n个月的办卡续卡人数
            year_months = []
            out_moneys = [0]*num_show_inout_his
            in_moneys = [0]*num_show_inout_his

            for i in range(num_show_inout_his-1,-1,-1):
                month = months[cur_month-i-1]
                year = cur_year
                if cur_month-i<0:
                    year -= 1
                year_months.append('{}-{}-'.format(year,month))

            sql = '''SELECT * FROM goods_inout WHERE inout_date REGEXP '{}'
            '''.format('|'.join(year_months))
            
            flag, result = self.MySQL.SelectFromDataBse(sql)
            if flag:
                for line in result:
                    date_str=line[3]
                    in_or_out = line[2]
                    for i, d_str in enumerate(year_months):
                        if date_str.startswith(d_str):
                            if in_or_out==1:
                                in_moneys[i]+=line[1]*line[4]
                            else:
                                out_moneys[i]+=line[1]*line[4]
                
                print(in_moneys, out_moneys)


                # 画图
                yin_kui = list(np.array(out_moneys)-np.array(in_moneys))
                self.InoutLineFigure.ax.cla()
                x=range(1,num_show_inout_his+1)
                line_inmoneys = Line2D(x, in_moneys, marker='^', color='g', label='入库金额')
                line_outmoneys = Line2D(x,out_moneys, marker='o', color='b', label='出库金额')
                line_yinkui = Line2D(x,yin_kui, marker='*', color='yellow', label='盈利')

                if num_show_inout_his >=9:
                    rotate = -30
                else:
                    rotate = 0

                
                margin = (max(out_moneys+in_moneys)-min(yin_kui))/10

                self.InoutLineFigure.ax.set_ylim(min(yin_kui)-margin, max(out_moneys+in_moneys)+margin)
                self.InoutLineFigure.ax.add_line(line_inmoneys)
                self.InoutLineFigure.ax.add_line(line_outmoneys)
                self.InoutLineFigure.ax.add_line(line_yinkui)           
                self.InoutLineFigure.ax.axhline(0,color='red',ls="--",label='盈亏线')

                self.InoutLineFigure.ax.set_xlim(0, num_show_inout_his+1)
                self.InoutLineFigure.ax.set_xticks(range(1,num_show_inout_his+2))
                self.InoutLineFigure.ax.set_xticklabels([i[:-1] for i in year_months],rotation=rotate)
                self.InoutLineFigure.ax.set_title('近{}个月的进出库以及利润'.format(num_show_inout_his))

                self.InoutLineFigure.ax.legend(loc='best')
                self.InoutLineFigure.draw()
            else:
                QMessageBox.critical(self, '错误', '连接数据库失败！\n考虑是否是以下原因引起：\n (1)网络连接出现问题', QMessageBox.Ok, QMessageBox.Ok) 
        except Exception as e:
            print(e)        

    def on_btn_showhis(self):
        
        self.bar_year = int(self.cb_bar_year.currentText())
        self.bar_month = int(self.cb_bar_month.currentText())

        self.get_Bar_data(self.bar_year, self.bar_month)  #获取当月的bar数据

        self.BarFigure.ax.cla()
        self.banka_setAx()


        self.cur_y = np.array([0.,0.])
        self.ct = 0  # 当前0次
        # 定时器控制动态更新
        self.timer = QTimer()
        self.timer.start(1)
        self.ts = time.time()
        self.timer.timeout.connect(self.BarUpdate)


    def on_btn_save_all_fluid_2(self):
        sql = '''
        SELECT * FROM goods_inout WHERE inout_date ORDER BY inout_date
        '''

        self.sql_thread = MySQLThread(self.MySQL, sql)
        self.sql_thread.trigger.connect(self.on_thread_export_all_data_2)
        self.sql_thread.start()
    def on_btn_save_all_fluid(self):
        sql = '''
        SELECT * FROM banka WHERE banka_date ORDER BY banka_date
        '''

        self.sql_thread = MySQLThread(self.MySQL, sql)
        self.sql_thread.trigger.connect(self.on_thread_export_all_data)
        self.sql_thread.start()
    

    def on_btn_save_crt_fluid_2(self):
        filepath = QFileDialog.getSaveFileName(self, '导出到EXCEL','./当前数据.xls','Excel Files(*.xls)')[0]

        # 检查文件是否已经打开
        if filepath!='':
            flag=True
            try:
                myfile=open(filepath,'r+')
            except IOError:
                flag=False
                QMessageBox.warning(self, '提示', '文件已经打开，请先关闭相应的文件！',QMessageBox.Ok, QMessageBox.Ok)
            if flag:


                self.btn_fluid_getDB_2.setEnabled(False)
                self.btn_fluid_excrt_2.setEnabled(False)
                self.btn_fluid_expall_2.setEnabled(False)

                headers = ['货物名','价格','出/入库','操作日期','数量']
                self.excel_thread = WriteExcelThread(self.fluid_data_inout, filepath, header=headers, labels=['出库','入库'],label_idx=2)
                self.excel_thread.trigger.connect(self.on_thread_export_crtdata_2)
                self.excel_thread.start()        

    def on_btn_save_crt_fluid(self):
        filepath = QFileDialog.getSaveFileName(self, '导出到EXCEL','./当前数据.xls','Excel Files(*.xls)')[0]

        # 检查文件是否已经打开
        if filepath!='':
            flag=True
            try:
                myfile=open(filepath,'r+')
            except IOError:
                flag=False
                QMessageBox.warning(self, '提示', '文件已经打开，请先关闭相应的文件！',QMessageBox.Ok, QMessageBox.Ok)
            if flag:


                self.btn_fluid_getDB.setEnabled(False)
                self.btn_fluid_excrt.setEnabled(False)
                self.btn_fluid_expall.setEnabled(False)

                self.excel_thread = WriteExcelThread(self.fluid_data, filepath, header=self.fluid_headers, labels=['办卡','续卡'],label_idx=2)
                self.excel_thread.trigger.connect(self.on_thread_export_crtdata)
                self.excel_thread.start()
    

    def on_btn_getBXfluid_2(self):
        # 无效校验
        flag = False
        flag2 = False
        self.fulid_selected_month_2.clear()
        # 清空
        self.fluid_data_inout.clear()
        self.fluid_data_model_inout.clear()
        self.fluid_data_model_inout.setHorizontalHeaderLabels(self.fluid_headers_inout)


        for i in range(1,len(self.cb_fluid_month_2.qCheckBox)):
            if self.cb_fluid_month_2.qCheckBox[i].isChecked():
                flag = True
                self.fulid_selected_month_2.append(i)

        for i in range(1,len(self.cb_fluid_inout.qCheckBox)):
            if self.cb_fluid_inout.qCheckBox[i].isChecked():
                flag2 = True


        inout_term = ''        
        if self.cb_fluid_inout.qCheckBox[1].isChecked() and not self.cb_fluid_inout.qCheckBox[2].isChecked():
            inout_term='and goods_in=0'
        elif not self.cb_fluid_inout.qCheckBox[1].isChecked() and self.cb_fluid_inout.qCheckBox[2].isChecked():
            inout_term='and goods_in=1'
        
        print(inout_term)
        if flag == False:
            QMessageBox.warning(self, '提示','未选择月份!', QMessageBox.Yes, QMessageBox.Yes)
        
        elif flag2==False:
            QMessageBox.warning(self, '提示','未选择出/入库!', QMessageBox.Yes, QMessageBox.Yes)
        else:

            search_terms = []
            for m in self.fulid_selected_month_2:
                date = '{}-{}-'.format(self.cb_fluid_year_2.currentText(), m)
                search_terms.append(date)


            sql = '''
            SELECT * FROM goods_inout WHERE inout_date REGEXP '{}' {} ORDER BY inout_date
            '''.format('|'.join(search_terms), inout_term)



            self.btn_fluid_getDB_2.setEnabled(False)
            self.btn_fluid_excrt_2.setEnabled(False)
            self.btn_fluid_expall_2.setEnabled(False)
            # 开一个线程执行sql
            self.sql_thread = MySQLThread(self.MySQL, sql)
            self.sql_thread.trigger.connect(self.on_thread_show_fluid_tv_2)

            self.sql_thread.start()

    def on_btn_getBXfluid(self):
        # 无效校验
        flag = False
        self.fulid_selected_month.clear()
        # 清空
        self.fluid_data.clear()
        self.fluid_data_model.clear()
        self.fluid_data_model.setHorizontalHeaderLabels(self.fluid_headers)


        for i in range(1,len(self.cb_fluid_month.qCheckBox)):
            if self.cb_fluid_month.qCheckBox[i].isChecked():
                flag = True
                self.fulid_selected_month.append(i)
        print(self.fulid_selected_month)
        if flag == False:
            QMessageBox.warning(self, '提示','未选择月份!', QMessageBox.Yes, QMessageBox.Yes)
        else:

            search_terms = []
            for m in self.fulid_selected_month:
                date = '{}-{}-'.format(self.cb_fluid_year.currentText(), m)
                search_terms.append(date)

            sql = '''
            SELECT * FROM banka WHERE banka_date REGEXP '{}' ORDER BY banka_date
            '''.format('|'.join(search_terms))



            self.btn_fluid_getDB.setEnabled(False)
            self.btn_fluid_excrt.setEnabled(False)
            self.btn_fluid_expall.setEnabled(False)
            # 开一个线程执行sql
            self.sql_thread = MySQLThread(self.MySQL, sql)
            self.sql_thread.trigger.connect(self.on_thread_show_fluid_tv)

            self.sql_thread.start()



    def on_btn_showInout(self):
        if len(self.cb_inout_goods.currentText())==0:
            QMessageBox.critical(self, '错误','未选择任何货物',QMessageBox.Ok,QMessageBox.Ok)
        else:
            goods_name = self.cb_inout_goods.currentText()
            year = int(self.cb_bar_inout_year.currentText())
            month = int(self.cb_bar_inout_month.currentText())

            in_money = 0
            out_money = 0
            try:
                sql = '''SELECT * FROM goods_inout WHERE goods_name='{}' and inout_date like '%{}-{}-%' '''.format(goods_name, year, month)

                flag, result = self.MySQL.SelectFromDataBse(sql)
                if flag:
                    for line in result:
                        if line[2]==0:
                            out_money+=line[1]*line[4]
                        else:
                            in_money+=line[1]*line[4]
                    

                    print(in_money, out_money)
                    # 画图
                    self.InoutBarFigure.ax.cla()  # 先清空
                    self.InoutBarFigure.ax.set_xlim(0,4)
                    self.InoutBarFigure.ax.set_ylim(0,2*max(in_money, out_money,100))
                    self.InoutBarFigure.ax.set_xticks([1.2,2.2])
                    self.InoutBarFigure.ax.set_xticklabels(['进货金额','出货'])
                    self.InoutBarFigure.ax.set_title('{}年{}月{}进出货统计'.format(year, month,goods_name))
                    self.InoutBarFigure.ax.set_ylabel('金额(元)')
            
                    if in_money!=0 or out_money!=0:
                        self.InoutBarFigure.ax.bar(self.bar_x, np.array([in_money, out_money]), width=0.4)       
                    self.InoutBarFigure.ax.text(1.2,in_money+max(in_money, out_money,100)/10,'{}'.format(in_money), ha='center', va='center')
                    self.InoutBarFigure.ax.text(2.2,out_money+max(in_money, out_money,100)/10,'{}'.format(out_money), ha='center', va='center')                    
                    self.InoutBarFigure.draw()            
                else:
                    QMessageBox.critical(self, '错误', '连接数据库失败！\n考虑是否是以下原因引起：\n (1)网络连接出现问题', QMessageBox.Ok, QMessageBox.Ok) 
            except Exception as e:
                print(e)

    def on_btn_showMoney(self):
        self.Money_num_month = (self.cb_show_num_month_money.currentIndex()+1)*3

        self.get_Money_Line_data(self.cur_year,self.cur_month, self.Money_num_month)
        self.LineFigure.ax.cla()
        self.money_setAx()
        self.Mnyct = 0  # 当前0次
        # 定时器控制动态更新
        self.timer = QTimer()
        self.timer.start(1)
        self.ts = time.time()
        self.timer.timeout.connect(self.LineUpdate)


    # 更新办卡续卡历史图

    def BXLineUpdate(self):
        stride = self.time_limit // self.BX_num_month

    
        if self.BXct%stride==0 and self.BXct//stride < self.BX_num_month:
            x = self.BXct//stride+1
            ybk = self.BX_line_ybk[self.BXct//stride]
            yxk = self.BX_line_yxk[self.BXct//stride]

            self.timer_BX_line_x.append(x)
            self.timer_BX_line_ybk.append(ybk)
            self.timer_BX_line_yxk.append(yxk)

            self.BXline_bk = Line2D(self.timer_BX_line_x, self.timer_BX_line_ybk, marker='^', color='g', label='办卡')
            self.BXline_xk = Line2D(self.timer_BX_line_x, self.timer_BX_line_yxk, marker='o', color='b', label='续卡')
            self.BXLineFigure.ax.cla()
            self.BXLineFigure.ax.add_line(self.BXline_bk)
            self.BXLineFigure.ax.add_line(self.BXline_xk)
            
            if self.BX_num_month >=9:
                rotate = -30
            else:
                rotate = 0
            self.BXLineFigure.ax.set_xticks(range(1,self.BX_num_month+2))
            self.BXLineFigure.ax.set_xticklabels(self.BX_line_xticks,rotation=rotate)
            
            self.BXLineFigure.draw()
        self.BXct+=1
        if self.BXct == 30:
            self.BXLineFigure.ax.set_ylabel('人数(人)')
            self.BXLineFigure.ax.set_title('近{}个月的办卡续卡趋势'.format(self.BX_num_month))

            self.BXLineFigure.ax.legend(loc='best')
            self.BXLineFigure.draw()
            self.timerBX.stop() 

    # 更新柱状图
    def BarUpdate(self):

        self.cur_y[0] += self.bar_y[0]*1./self.time_limit
        self.cur_y[1] += self.bar_y[1]*1./self.time_limit
        self.ct+=1

        #print(self.cur_y)
        for i in range(len(self.patches)):
            self.patches[i].set_height(self.cur_y[i])
        self.bar.patches = self.patches
        self.BarFigure.draw()
        if self.ct == self.time_limit:
            print(self.bar_y[0],self.bar_y[1])
            self.BarFigure.ax.text(1.2,self.bar_y[0]+np.max(self.bar_y)/10,'{}人'.format(self.bar_y[0]), ha='center', va='center')
            self.BarFigure.ax.text(2.2,self.bar_y[1]+np.max(self.bar_y)/10,'{}人'.format(self.bar_y[1]), ha='center', va='center')
            self.BarFigure.draw()
            self.timer.stop()


    def LineUpdate(self):
        stride = self.time_limit // self.Money_num_month

        if self.Mnyct%stride==0 and self.Mnyct//stride < self.Money_num_month:
            x = self.Mnyct//stride+1
            y = self.line_y[self.Mnyct//stride]
            self.line_xlis.append(x)
            self.line_ylis.append(y)
            self.LineFigure.ax.text(x-0.5,y+0.5, str(y))
            self.line = Line2D(self.line_xlis, self.line_ylis, marker='o')
            self.LineFigure.ax.add_line(self.line)
            if self.Money_num_month >=9:
                rotate = -15
            else:
                rotate = 0
            self.LineFigure.ax.set_xticks(range(1,self.Money_num_month+2))
            self.LineFigure.ax.set_xticklabels(self.line_xticks,rotation=rotate)
            self.LineFigure.draw()

        self.Mnyct+=1
        if self.Mnyct == 30:
            self.timer.stop()

    # 在控件中添加画板
    def Init_Widgets(self):
        self.PrepareBarCanvas()
        self.PrepareLineCanvas()
        self.PrepareBXLineCanvas()
        self.PrepareInoutBarCanvas()
        self.PrepareInoutLineCanvas()

    def PrepareInoutBarCanvas(self):
        self.InoutBarFigure = Figure_Canvas()
        self.InoutBarFigureLayout = QGridLayout(self.gb_inout)
        self.InoutBarFigureLayout.addWidget(self.InoutBarFigure)
    
    def PrepareInoutLineCanvas(self):
        self.InoutLineFigure = Figure_Canvas()
        self.InoutLineFigureLayout = QGridLayout(self.gb_inouthis)
        self.InoutLineFigureLayout.addWidget(self.InoutLineFigure)
    
    def PrepareBXLineCanvas(self):
        self.BXLineFigure = Figure_Canvas()
        self.BXLineFigureLayout = QGridLayout(self.gb_bankhis)
        self.BXLineFigureLayout.addWidget(self.BXLineFigure)
             


    def PrepareLineCanvas(self):
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.gb_money)
        self.LineFigureLayout.addWidget(self.LineFigure)
    

    def PrepareBarCanvas(self):
        self.BarFigure = Figure_Canvas()
        self.BarFigureLayout = QGridLayout(self.gb_banka)
        self.BarFigureLayout.addWidget(self.BarFigure)
        
     
# 线程结束函数
    def on_thread_show_fluid_tv_2(self, sql_data):
        inout = ['出库','入库']
        for i, data in enumerate(sql_data):
            self.fluid_data_model_inout.appendRow([
                QStandardItem(data[0]),
                QStandardItem(str(data[1])),
                QStandardItem(str(data[4])),
                QStandardItem(inout[data[2]]),
                QStandardItem(data[3])
            ])
            self.fluid_data_inout.append(data)
        
        self.btn_fluid_getDB_2.setEnabled(True)
        self.btn_fluid_excrt_2.setEnabled(True)
        self.btn_fluid_expall_2.setEnabled(True)   

    def on_thread_show_fluid_tv(self, sql_data):
        BX =  ['办卡','续卡']
        for i, data in enumerate(sql_data):
            self.fluid_data_model.appendRow([
                QStandardItem(data[0]),
                QStandardItem(data[1]),
                QStandardItem(BX[data[2]]),
                QStandardItem(str(data[3])),
                QStandardItem(data[4])
            ])
            self.fluid_data.append(data)
        
        self.btn_fluid_getDB.setEnabled(True)
        self.btn_fluid_excrt.setEnabled(True)
        self.btn_fluid_expall.setEnabled(True)


    def on_thread_export_crtdata_2(self):
        self.btn_fluid_getDB_2.setEnabled(True)
        self.btn_fluid_excrt_2.setEnabled(True)
        self.btn_fluid_expall_2.setEnabled(True)
        QMessageBox.information(self, '提示','导出成功!', QMessageBox.Yes, QMessageBox.Yes)   

    def on_thread_export_crtdata(self):
        self.btn_fluid_getDB.setEnabled(True)
        self.btn_fluid_excrt.setEnabled(True)
        self.btn_fluid_expall.setEnabled(True)
        QMessageBox.information(self, '提示','导出成功!', QMessageBox.Yes, QMessageBox.Yes)


    def on_thread_export_all_data_2(self, sql_data):
        filepath = QFileDialog.getSaveFileName(self, '导出到EXCEL','./所有流水数据.xls','Excel Files(*.xls)')[0]

        # 检查文件是否已经打开
        if filepath!='':
            flag=True
            try:
                myfile=open(filepath,'r+')
            except IOError:
                flag=False
                QMessageBox.warning(self, '提示', '文件已经打开，请先关闭相应的文件！',QMessageBox.Ok, QMessageBox.Ok)
            if flag:
                
                self.btn_fluid_getDB_2.setEnabled(False)
                self.btn_fluid_excrt_2.setEnabled(False)
                self.btn_fluid_expall_2.setEnabled(False)
                headers = ['货物名','价格','出/入库','操作日期','数量']
                self.excel_thread = WriteExcelThread(sql_data, filepath, header=headers, labels=['出库','入库'],label_idx=2)
                self.excel_thread.trigger.connect(self.on_thread_export_crtdata_2)
                self.excel_thread.start()

    def on_thread_export_all_data(self, sql_data):
        filepath = QFileDialog.getSaveFileName(self, '导出到EXCEL','./所有流水数据.xls','Excel Files(*.xls)')[0]

        # 检查文件是否已经打开
        if filepath!='':
            flag=True
            try:
                myfile=open(filepath,'r+')
            except IOError:
                flag=False
                QMessageBox.warning(self, '提示', '文件已经打开，请先关闭相应的文件！',QMessageBox.Ok, QMessageBox.Ok)
            if flag:

                self.btn_fluid_getDB.setEnabled(False)
                self.btn_fluid_excrt.setEnabled(False)
                self.btn_fluid_expall.setEnabled(False)
                self.excel_thread = WriteExcelThread(sql_data, filepath,header=self.fluid_headers, labels=['办卡','续卡'], label_idx=2)
                self.excel_thread.trigger.connect(self.on_thread_export_crtdata)
                self.excel_thread.start()


    def myclear(self):
        self.fluid_data_model.clear()
        self.fluid_data_model.setHorizontalHeaderLabels(self.fluid_headers)
        self.fluid_data = []
        
        self.fluid_data_model_inout.clear()
        self.fluid_data_model_inout.setHorizontalHeaderLabels(self.fluid_headers_inout)
        self.fluid_data_inout=[]

        self.BXLineFigure.ax.cla()
        self.BXLineFigure.draw()
        self.BarFigure.ax.cla()
        self.BarFigure.draw()
        self.LineFigure.ax.cla()
        self.LineFigure.draw()

        self.InoutBarFigure.ax.cla()
        self.InoutBarFigure.draw()

        self.InoutLineFigure.ax.cla()
        self.InoutLineFigure.draw()        

        self.listFunc.setCurrentRow(0)
        self.cb_fluid_month.clear()

        # 初始化进出货选择
        sql = '''SELECT DISTINCT goods_name FROM goods_inout'''
        try:
            flag, result = self.MySQL.SelectFromDataBse(sql)
            if flag:
                self.cb_inout_goods.clear()
                for name in result:
                    self.cb_inout_goods.addItem(name[0])
                    print(name[0])
            else:
                QMessageBox.critical(self, '错误', '连接数据库失败！\n考虑是否是以下原因引起：\n (1)网络连接出现问题', QMessageBox.Ok, QMessageBox.Ok)
        except Exception as e:
            print(e)
            QMessageBox.critical(self, '错误', '连接数据库失败！\n考虑是否是以下原因引起：\n (1)网络连接出现问题', QMessageBox.Ok, QMessageBox.Ok)
        


# 画板类
class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.9, height=2.7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)

    def test(self):
        x = [1,2,3,4,5,6,7]
        y = [2,1,3,5,6,4,3]
        self.ax.plot(x,y)






        

# 
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = logicSysSum()
#     ui.show()
#     sys.exit(app.exec_())
