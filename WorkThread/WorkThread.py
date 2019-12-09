from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import xlwt

class MySQLThread(QThread):
    trigger = pyqtSignal(tuple)

    def __init__(self,MySQL,sql,parent=None):
        super(MySQLThread, self).__init__(parent)
        self.sql = sql
        self.MySQL = MySQL
    
    def run(self):

        # 执行查询
        _, data = self.MySQL.SelectFromDataBse(self.sql)
        self.trigger.emit(data)

class WriteExcelThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, data, filepath,parent=None):
        super(WriteExcelThread, self).__init__(parent)
        self.data = data
        self.filepath = filepath

    def run(self):
        if self.filepath=='':
            pass
        else:
        # 写文件
            wb = xlwt.Workbook()
            sheet = wb.add_sheet('数据')

            # 写表头
            hearder = ['联系方式','姓名','办/续卡','办/续卡金额','办/续卡日期']
            for i in range(len(hearder)):
                sheet.write(0, i, hearder[i])
            
            j=1
            BX = ['办卡','续卡']
            for line in self.data:
                for i in range(len(hearder)):
                    if i==2:
                        sheet.write(j, i, BX[line[i]])
                    else:
                        sheet.write(j, i, line[i])
                j+=1
            
            wb.save(self.filepath)
            self.trigger.emit()
        


