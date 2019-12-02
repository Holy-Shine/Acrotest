from SummarySystem.Ui_sumSys import Ui_sumSys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
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

class logicSysSum(QMainWindow, Ui_sumSys):
    def __init__(self, parent=None):
        super(logicSysSum, self).__init__(parent)


        self.setupUi(self)


        # 办卡人数-柱状图横纵坐标数据
        self.x = np.array([1,2])
        self.org_y = np.array([0,0])
        self.y = np.array([100,200])


        # 6个月的营业额-点线图横纵坐标
        self.line_x = np.arange(1,7,1)
        self.line_y = [100,200,400,300,200,500]
        self.line_z = np.array([100,200,400,300,200,500])
        

        self.time_limit = 30   # 更新50次

        self.Init_Widgets()
        
        self.btn_show.clicked.connect(self.on_btn_showhis)
        self.btn_show_money.clicked.connect(self.on_btn_showMoney)

        self.listFunc.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)


    def banka_setAx(self):
        self.BarFigure.ax.set_xlim(0,4)
        self.BarFigure.ax.set_ylim(0,2*np.max(self.y))
        self.BarFigure.ax.set_xticks([1.2,2.2])
        self.BarFigure.ax.set_xticklabels(['办卡人数','续卡人数'])
       # self.BarFigure.ax.text(1.2,201,'123', fontsize=20)
        

        self.bar = self.BarFigure.ax.bar(self.x, self.org_y, width=0.4)

        self.patches = self.bar.patches


    def money_setAx(self):
        self.LineFigure.ax.set_xlim(0, 8)
        self.LineFigure.ax.set_ylim(np.min(self.line_z)-50, np.max(self.line_z)+100)
        self.line_xlis = []
        self.line_ylils = []

        self.line = Line2D(self.line_xlis, self.line_ylils, marker='o')
        self.LineFigure.ax.add_line(self.line)
        self.LineFigure.ax.set_ylabel('营业额（单位元）')
        self.LineFigure.ax.set_title('近6个月的营业额')


    # 按钮事件
    def on_btn_showhis(self):
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
        self.LineFigure.ax.cla()
        self.money_setAx()
        self.ct = 0  # 当前0次
        # 定时器控制动态更新
        self.timer = QTimer()
        self.timer.start(1)
        self.ts = time.time()
        self.timer.timeout.connect(self.LineUpdate)


    
    # 更新柱状图
    def BarUpdate(self):

        self.cur_y[0] += self.y[0]*1./self.time_limit
        self.cur_y[1] += self.y[1]*1./self.time_limit
        self.ct+=1

        #print(self.cur_y)
        for i in range(len(self.patches)):
            self.patches[i].set_height(self.cur_y[i])
        self.bar.patches = self.patches
        self.BarFigure.draw()
        if self.ct == self.time_limit:
            self.BarFigure.ax.text(1.2,self.y[0]+20,'{}人'.format(self.y[0]), ha='center', va='center')
            self.BarFigure.ax.text(2.2,self.y[1]+20,'{}人'.format(self.y[1]), ha='center', va='center')
            self.BarFigure.draw()
            self.timer.stop()

    def LineUpdate(self):
        if self.ct%5==0:
            x = self.ct//5+1
            y = self.line_y[self.ct//5]
            self.line_xlis.append(x)
            self.line_ylils.append(y)
            self.LineFigure.ax.text(x-0.5,y+0.5, str(y))
            self.line = Line2D(self.line_xlis, self.line_ylils, marker='o')
            self.LineFigure.ax.add_line(self.line)
            self.LineFigure.draw()
            print(self.ct//5)
        self.ct+=1
        if self.ct == 30:
            self.timer.stop()

    # 在控件中添加画板
    def Init_Widgets(self):
        self.PrepareBarCanvas()
        self.PrepareLineCanvas()


    def PrepareLineCanvas(self):
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.gb_money)
        self.LineFigureLayout.addWidget(self.LineFigure)
        self.money_setAx()

    def PrepareBarCanvas(self):
        self.BarFigure = Figure_Canvas()
        self.BarFigureLayout = QGridLayout(self.gb_banka)
        self.BarFigureLayout.addWidget(self.BarFigure)
        
        self.banka_setAx()



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
