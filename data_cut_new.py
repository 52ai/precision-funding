# coding:utf-8
"""
create on Jan 15, 2017 by Wenyan Yu

Function:

分割数据
"""
from datetime import *
import time


def read_data(path_of_file, line_number):
    """
    给定文件的路径和需要读取文件的行数，依次读取数据并显示在屏幕上
    :param path_of_file:
    :param line_number:
    :return: None
    """
    print "文件:",path_of_file,"的前",line_number,"行如下："
    try:
        file_of_read = open(path_of_file)
        for line_of_file in file_of_read.readlines():
            print line_of_file
            line_number -= 1
            if line_number == 0:
                break
    finally:
        file_of_read.close()


dorm_train = "Data/dorm/dorm_train.txt"  # 训练数据的路径
dorm_test = "Data/dorm/dorm_test.txt"  # 测试数据的路径

read_data(dorm_test, 10)
read_data(dorm_test, 10)

"""
line_number = 1
for line in dorm_train.readlines():
    print line_number, ":", line
    line_number += 1
    if line_number > 10000:
        break
"""

students_id_list = []

line_count = 1
for line in dorm_train.readlines():
    # print "学生ID:",line.split(',')[0],
    # print "门禁时间:",line.split(',')[1],
    # print "进出状态:", line.split(',')[2]
    print line
    line_count += 1

    if datetime.strptime(line.split(',')[1].strip('\"'),'%Y/%m/%d %H:%M:%S') > datetime.strptime('2015/02/21 03:31:11','%Y/%m/%d %H:%M:%S'):
       break

    if line.split(',')[0] is not None:
        if int(line.split(',')[0]) not in students_id_list:
            students_id_list.append(int(line.split(',')[0]))

print "学生人数：",len(students_id_list)
print "门禁记录：",line_count



# students_id_list = sorted(students_id_list)

"""
<<<<<<< HEAD
stu_id = open('Data/dorm/stu_id_of_dorm.txt', 'wb')
=======
stu_id = open('Data/dorm/stu_id.txt', 'wb')
>>>>>>> 3999f466fba4a67d9ccaad1f67f354aca2e14f0e

for i in students_id_list:
    stu_id.write(str(i)+'\n')
stu_id.close()
"""

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


