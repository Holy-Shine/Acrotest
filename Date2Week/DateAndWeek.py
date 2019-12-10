import time
from datetime import datetime


def FromDatetoWeek(year,month,day):
    try:
        date_day = '{}{}{}'.format(year,month,day)
        week = int(datetime.strptime(date_day, "%Y%m%d").strftime("%W")) + 1
        weekday = '7' \
            if datetime.strptime(date_day, "%Y%m%d").strftime("%w") == '0' \
            else datetime.strptime(date_day,"%Y%m%d").strftime("%w")
        return week,weekday
    except Exception as e:
        print(e)


def FromWeektoDate(year,week,day):
    if(day==7):
        day = 0
        week+=1
    date = '{}-{}-{}'.format(year,week,day)
    res =time.strptime(date, '%Y-%U-%w')
    return res.tm_year,res.tm_mon,res.tm_mday

def getCurrentYMD():
    tm = time.gmtime()
    return '{}-{}-{}'.format(tm.tm_year,tm.tm_mon,tm.tm_mday)

#返回某年有几周
def getWeekNum(year):
    date_day = '{}{}{}'.format(year, 12, 31)
    week = int(datetime.strptime(date_day, "%Y%m%d").strftime("%W")) + 1
    return week

#返回某年第一周的第一天是周几
def getFirstWeekDate(year):
    try:
        _, weekday = FromDatetoWeek(year, '01', '01')
        return int(weekday)
    except Exception as e:
        print(e)

#返回某年最后一周是周几
def getLastWeekDate(year):
    _, weekday = FromDatetoWeek(year, '12', '31')
    return  int(weekday)

if __name__ == '__main__':
    y = '2019'
    m = '1'
    d = '1'
    #
    #
    week,weekday = FromDatetoWeek(y,m,d)
    print('{}年第{}周的周{}'.format(2019,week,weekday))
    year,mon,day = FromWeektoDate(2019,int(week)-1,int(weekday))
    print('{}年第{}月{}日'.format(year, mon, day))
    # print(getWeekNum(2022))

    # year = 2020
    # print("{}年的第一天是周{}".format(year,getFirstWeekDate(year)))
    # print("{}年的最后一天是周{}".format(year,getLastWeekDate(year)))