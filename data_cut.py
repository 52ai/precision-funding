# coding:utf-8
"""
create on Jan 15, 2017 by Wenyan Yu

Function:

分割数据
"""
from datetime import *
import time

dorm_train = open("Data/dorm/dorm_train.txt")

"""
line_number = 1
for line in dorm_train.readlines():
    print line_number, ":", line
    line_number += 1
    if line_number > 10000:
        break
"""

students_id_list = []

"""
# 13126,"2014/01/21 03:31:11","1"

print date.fromtimestamp(time.time())
print datetime.today()
dt = datetime.now()

print dt
print '(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y/%m/%d %H:%M:%S')
dt1 = datetime.strptime('2014/01/21 03:31:11', '%Y/%m/%d %H:%M:%S')
dt2 = datetime.strptime('2014/02/21 03:31:11', '%Y/%m/%d %H:%M:%S')
print (dt2 - dt1)/10
"""

for line in dorm_train.readlines():
    # print "学生ID:",line.split(',')[0],
    # print "门禁时间:",line.split(',')[1],
    # print "进出状态:", line.split(',')[2]
    print line

    if datetime.strptime(line.split(',')[1].strip('\"'),'%Y/%m/%d %H:%M:%S') > datetime.strptime('2014/02/21 03:31:11','%Y/%m/%d %H:%M:%S'):
       break

    if line.split(',')[0] is not None:
        if int(line.split(',')[0]) not in students_id_list:
            students_id_list.append(int(line.split(',')[0]))

print "学生人数：",len(students_id_list)
students_id_list = sorted(students_id_list)
stu_id = open('Data/dorm/stu_id.txt', 'wb')

for i in students_id_list:
    stu_id.write(str(i)+'\n')
"""
统计截止2014/03/21 03:31:11 共计3290个人
统计截止2014/04/21 03:31:11 共计3300个人
统计截止2014/05/21 03:31:11 共计3304个人
统计截止2014/06/21 03:31:11 共计3306个人

"""

"""
dorm_train.txt 前几行数据如下：

13126,"2014/01/21 03:31:11","1"
13126,"2014/01/21 04:53:55","0"
18484,"2014/01/21 05:16:18","1"
296,"2014/01/21 05:55:05","1"
9760,"2014/01/21 08:44:53","1"
6778,"2014/01/21 09:21:33","1"
18200,"2014/01/21 09:50:07","1"
8894,"2014/01/21 10:09:52","1"
9228,"2014/01/21 10:28:23","0"
6778,"2014/01/21 10:36:06","0"
5924,"2014/01/21 10:38:47","1"

"""


