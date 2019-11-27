import pymysql


class dbManager():
    def __init__(self):
        self.conn = pymysql.connect(
                        host='121.199.17.205',
                        user='Jessie',
                        password='Jessie.121406',
                        database = 'meminfo',
                        port = 3306,
                        charset='utf8')

    def excuteSQL(self,sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()  
        
        return cursor.fetchall()

    def __del__(self):
        self.conn.close()
