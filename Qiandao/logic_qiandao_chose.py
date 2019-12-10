from PyQt5.QtWidgets import QDialog,QMessageBox,QLineEdit,QApplication

from Qiandao.UI_Qiandao_chose import Ui_UiQiandaoChose

import os,sys
from Date2Week import DateAndWeek as timefunction
import time



class LogicQiandaoChose(Ui_UiQiandaoChose,QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.day = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


        self.init()
        self.slot_init()



    def init(self):
        self.initday()
        # self.et_chosetime.show()


    def slot_init(self):
        self.bt_back.clicked.connect(self.close)
        self.bt_confrim.clicked.connect(self.accept)

    def getList(self):
        return self.et_chosetime.Selectlist()



    def initday(self):
        tm = time.gmtime()
        week,weekday = timefunction.FromDatetoWeek(year=tm.tm_year,
                                                month=tm.tm_mon,
                                                day=tm.tm_mday)
        self.lb_time.setText("当前日期：{}年{}月{}日 第{}周 {}".format(tm.tm_year,tm.tm_mon,tm.tm_mday,week,self.week2day[int(weekday)]))








if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LogicQiandaoChose()
    login.show()
    sys.exit(app.exec_())