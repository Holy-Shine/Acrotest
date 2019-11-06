from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox,QLineEdit,QListWidget,QCheckBox,QListWidgetItem
from PyQt5.QtCore import Qt
from logic_classTime import logicClassTime
from PyQt5.QtWidgets import *

class ComboCheckBox(QComboBox):
    def __init__(self,items, parent=None):#items==[str,str...]
        super(ComboCheckBox,self).__init__(parent)

        self.times = [10,11,12,13,14,15,16,17,18,19,20,21]
        self.ttimes = ['10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00']
        self.day_time_lis = [0,0,0,0,0,0,0]  # 若某天被选中，则读取

        self.daytime = logicClassTime()
        self.daytime.setWindowModality(Qt.ApplicationModal)
        self.items=items
        self.row_num=len(self.items)
        self.Selectedrow_num=0
        self.qCheckBox=[]
        self.qComboBox=[]
        self.qLineEdit=QLineEdit()
        self.qLineEdit.setReadOnly(True)
        self.qListWidget=QListWidget()

        for i in range(0,self.row_num):
            self.addQCheckBox(i)
            self.qCheckBox[i].stateChanged.connect(lambda:self.show(i))
        self.setModel(self.qListWidget.model())
        self.setView(self.qListWidget)
        self.setLineEdit(self.qLineEdit)         
 
    def getTimeWidget(self,i):
        widget = QWidget()

        # grid 布局
        lyout = QGridLayout(widget)
        lyout.setContentsMargins(0, 0, 0, 0)

        cb_daytime = QtWidgets.QComboBox(widget)
        cb_daytime.addItems(self.ttimes)
        lyout.addWidget(cb_daytime, 0, 1, 1, 1)

        ck_day = QtWidgets.QCheckBox(widget)
        ck_day.setText(self.items[i])
        lyout.addWidget(ck_day, 0, 0, 1, 1)
        lyout.setColumnStretch(1, 2)

        return widget, cb_daytime, ck_day

    def addQCheckBox(self,i):
        qItem=QListWidgetItem(self.qListWidget)
        wiget, cb_daytime, ck_day = self.getTimeWidget(i)
        self.qCheckBox.append(ck_day)
        self.qComboBox.append(cb_daytime)
        self.qListWidget.setItemWidget(qItem,wiget)        
 
    def SelectlistAndIdx(self):
        Outputlist=[]
        OutputIdx = []  # 0表示未选中
        for i in range(0,self.row_num):
            if self.qCheckBox[i].isChecked()==True:
                Outputlist.append(self.qCheckBox[i].text())
                OutputIdx.append(1)
            else:
                OutputIdx.append(0)
        self.Selectedrow_num=len(Outputlist)
        return Outputlist, OutputIdx
    
    def show(self, n):

        show=''
        Outputlist,_=self.SelectlistAndIdx()
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in Outputlist:
            show+=i+';'
        
        self.qLineEdit.setText(show)
        self.qLineEdit.setReadOnly(True)
 
 
    def clear(self):
        for i in range(self.row_num):
            self.qCheckBox[i].setChecked(False)
