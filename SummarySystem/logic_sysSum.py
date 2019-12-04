from SummarySystem.Ui_sumSys import Ui_sumSys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout,QMessageBox
from PyQt5.QtCore import QTimer
import sys, time
import numpy as np 

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib
import matplotlib.cbook as cbook

# 中文问题
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

from datetime import datetime as dt

class logicSysSum(QMainWindow, Ui_sumSys):
    def __init__(self, MySQL, parent=None):
        super(logicSysSum, self).__init__(parent)


        self.setupUi(self)
        self.MySQL = MySQL

        # 办卡人数-柱状图横纵坐标数据
        self.bar_x = np.array([1,2])
        self.bar_org_y = np.array([0,0])
        self.bar_y = np.array([100,200])





        

        self.time_limit = 30   # 更新50次

        
        
        self.btn_show_bar.clicked.connect(self.on_btn_showhis)
        self.btn_show_BXline.clicked.connect(self.on_btn_show_BXline)
        self.btn_show_MoneyLine.clicked.connect(self.on_btn_showMoney)

        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)
        self.listFunc.currentRowChanged.connect(self.event_left_rowSelected)
        self.listFunc.setCurrentRow(0)


        self.Init_Widgets()


    def get_Bar_data(self, year, month):

        sql_date = '%{}-{}%'.format(year,month)
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
                self.bar_y = np.array([result_bk[0][0],result_xk[0][0]])
                
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
                SELECT COUNT(*) FROM banka AS bk where bk.banka_type=0 and bk.banka_date like '%{}-{}%'
                '''.format(year, month)

                flag_bkhi, result_bkhis = self.MySQL.SelectFromDataBse(sql)
                sql = '''
                SELECT COUNT(*) FROM banka AS bk where bk.banka_type=1 and bk.banka_date like '%{}-{}%'
                '''.format(year, month)

                flag_xkhi, result_xkhis = self.MySQL.SelectFromDataBse(sql)
                   

                flag &= flag_bkhi
                flag &= flag_xkhi

                if (flag):
                    self.BX_line_ybk.append(result_bkhis[0][0])
                    self.BX_line_yxk.append(result_xkhis[0][0])
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
                SELECT SUM(banka_fee) FROM banka AS bk where bk.banka_date like '%{}-{}%'
                '''.format(year, month)

                flag1, result= self.MySQL.SelectFromDataBse(sql)
                   

                flag &= flag1

                if (flag):
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
            
            # self.get_Bar_data(self.cur_year, self.cur_month)  #获取当月的bar数据
            # self.get_BX_line_data(self.cur_year, self.cur_month, self.BX_num_month) # 获取BX数据         
        # 营业额统计
        elif current_row == 1:
            pass
            


    def banka_setAx(self):
        self.BarFigure.ax.set_xlim(0,4)
        self.BarFigure.ax.set_ylim(0,2*np.max(self.bar_y))
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

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = logicSysSum()
#     ui.show()
#     sys.exit(app.exec_())
