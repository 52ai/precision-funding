# coding:utf-8

from datetime import *
import time


# 13126,"2014/01/21 03:31:11","1"

print date.fromtimestamp(time.time())
print datetime.today()
dt = datetime.now()

print dt
print '(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y/%m/%d %H:%M:%S')
dt1 = datetime.strptime('2014/01/21 03:31:11', '%Y/%m/%d %H:%M:%S')
dt2 = datetime.strptime('2014/02/21 03:31:11', '%Y/%m/%d %H:%M:%S')
print (dt2 - dt1)/10
print dt1

print dt1.time()
print dt1.date()