import pymysql
import pymysql.cursors

host='121.199.17.205',  # IP
user='Jessie',  # 用户名
password='Jessie.121406',  # 密码
database = 'meminfo',
port=3306,  # 端口号
charset='utf8'

class MySQLBaseFunction():

    def __init__(self,HostIP, Username, Password,DataBase):
        self.HostIP = HostIP
        self.Username = Username
        self.Password = Password
        self.database = DataBase

        self.cursor = None

        self.conn = None

    #改变服务器IP地址
    def ChangeIP(self,newHostIP):
        self.IP = newHostIP


    #改变访问的数据库
    def ChangeDataBase(self,newDataBase):
        self.database = newDataBase


    #改变服务器用户
    def ChangeUser(self,Username,Password):
        self.Username = Username
        self.Password = Password


    #确保游标存在
    def CheckCursor(self):
        if(self.cursor == None or self.conn == None):
            return False
        else:
            return True

    #连接数据库
    def ConnectMySQL(self):
        try:
            self.conn = pymysql.connect(host=self.HostIP[0],  # IP
                                  user=self.Username[0],  # 用户名
                                  password=self.Password[0],  # 密码
                                  port=3306,  # 端口号
                                  database= self.database[0],
                                  charset='utf8')  # 注意是utf8不是utf-8
            # 使用cursor()方法获取操作游标
            self.cursor = self.conn.cursor()
            print("已经成功连接数据库！")
            return True
        except Exception as e:
            print("连接数据库失败！")
            print(e)
            return False

    #测试连接
    def MySQLTest(self):
        flag = False
        if(self.CheckCursor()):
            self.cursor.execute("use meminfo;")
            self.cursor.execute("show tables;")
            self.conn.commit()
            flag = True
            return flag
        else:
            return flag

    #从数据库中查询某项
    def SelectFromDataBse(self,str):
        flag = False
        if (self.CheckCursor()):
            self.cursor.execute(str)
            result = self.cursor.fetchall()
            self.conn.commit()
            flag = True
            return flag, result
        else:
            return flag,"请先连接数据库"


    #插入数据项
    def InsertFromDataBse(self,str):
        flag = False
        if (self.CheckCursor()):
            self.cursor.execute(str)
            self.conn.commit()
            flag = True
            return flag
        else:
            return flag

    def UpdateFromDataBse(self,str):
        flag = False
        if (self.CheckCursor()):
            self.cursor.execute(str)
            self.conn.commit()
            flag = True
            return flag
        else:
            return flag


    #删除数据项
    def DeleteFromDataBse(self,str):
        flag = False
        if (self.CheckCursor()):
            self.cursor.execute(str)
            self.conn.commit()
            flag = True
            return flag
        else:
            return flag


if __name__ == '__main__':
    MySQL = MySQLBaseFunction(HostIP=host,
                                   Username=user,
                                   Password=password,
                                   DataBase= database)
    MySQL.ConnectMySQL()

