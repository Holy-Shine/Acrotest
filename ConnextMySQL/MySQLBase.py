import pymysql
import pymysql.cursors



class MySQLBaseFunction():

    def __init__(self,HostIP, Username, Password):
        self.HostIP = HostIP
        self.Username = Username
        self.Password = Password

        self.cursor = None


    #改变服务器IP地址
    def ChangeIP(self,newHostIP):
        self.IP = newHostIP


    #改变服务器用户
    def ChangeUser(self,Username,Password):
        self.Username = Username
        self.Password = Password


    #确保游标存在
    def CheckCursor(self):
        if(self.cursor == None):
            return False
        else:
            return True

    #连接数据库
    def ConnectMySQL(self):
        try:
            cnn = pymysql.connect(host='121.199.17.205',  # IP
                                  user='Jessie',  # 用户名
                                  password='Jessie.121406',  # 密码
                                  port=3306,  # 端口号
                                  charset='utf8')  # 注意是utf8不是utf-8
            # 使用cursor()方法获取操作游标
            self.cursor = cnn.cursor()
            return True
        except Exception:
            return False

    #测试连接
    def MySQLTest(self):
        flag = False
        if(self.CheckCursor()):
            self.cursor.execute("use meminfo;")
            self.cursor.execute("show tables;")
            result = self.cursor.fetchall()
            flag = True
            return flag,result
        else:
            return flag,"请先连接数据库"




    #从数据库中查询某项
    def SelectFromDataBse(self,str):
        flag = False
        if (self.CheckCursor()):
            self.cursor.execute(str)
            result = self.cursor.fetchall()
            return flag, result
        else:
            return flag,"请先连接数据库"


    #插入数据项
    def InsertFromDataBse(self,str):
        flag = False
        if (self.CheckCursor()):
            self.cursor.execute(str)
            result = self.cursor.fetchall()
            return flag, result
        else:
            return flag,"请先连接数据库"


    #删除数据项
    def DeleteFromDataBse(self,str):
        flag = False
        if (self.CheckCursor()):
            self.cursor.execute(str)
            result = self.cursor.fetchall()
            return flag, result
        else:
            return flag,"请先连接数据库"




