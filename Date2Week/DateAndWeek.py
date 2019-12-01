import time
from datetime import datetime


def FromDatetoWeek(year,month,day):
    date_day = '{}{}{}'.format(year,month,day)
    week = int(datetime.strptime(date_day, "%Y%m%d").strftime("%W")) + 1
    weekday = '7' \
        if datetime.strptime(date_day, "%Y%m%d").strftime("%w") == '0' \
        else datetime.strptime(date_day,"%Y%m%d").strftime("%w")
    return week,weekday


def FromWeektoDate(year,week,day):
    if(day==7):
        day = 0
        week+=1
    date = '{}-{}-{}'.format(year,week,day)
    res =time.strptime(date, '%Y-%U-%w')
    return res.tm_year,res.tm_mon,res.tm_mday
if __name__ == '__main__':
    y = '2019'
    m = '12'
    d = '01'


    week,weekday = FromDatetoWeek(y,m,d)
    print('{}年第{}周的周{}'.format(2019,week,weekday))
    year,mon,day = FromWeektoDate(2019,int(week)-1,int(weekday))
    print('{}年第{}月{}日'.format(year, mon, day))