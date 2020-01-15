
import json

from ConnecMySQL.MySQLBase import MySQLBaseFunction
from FaceFunction.FaceUtil import FaceRecognition

def CheckDB():
    try:
        f = open('./BasicInfos/DBInfo.json', encoding='utf-8')
        user_dic = json.load(f)
        MySQL = MySQLBaseFunction(HostIP=user_dic['DB_info'][0]['ip'],
                                  Username=user_dic['DB_info'][0]['user'],
                                  Password=user_dic['DB_info'][0]['password'],
                                  DataBase=user_dic['DB_info'][0]['database'])
        flag = MySQL.ConnectMySQL()
        return flag,MySQL
    except Exception as e:
        print(e)

def CheckFace():
    try:
        f = open('./BasicInfos/FaceSDK.json', encoding='utf-8')
        user_dic = json.load(f)
        Appkey = user_dic['FaceSDK'][0]['Appkey'].encode()
        SDKey = user_dic['FaceSDK'][0]['SDKey'].encode()

        facefunction = FaceRecognition(Appkey=Appkey, SDKey=SDKey)
        flag = facefunction.ActivationFace()
        return  flag,facefunction
    except Exception as e:
        print(e)

if __name__ == '__main__':
    flag, MySQL = CheckFace()
    print(flag)