# coding:utf-8

"""
create on Jan 15,2017 by Wenyan Yu

对寝室的门禁数据进行分析

从初步的门禁数据分析可知，整个训练集共有2115065条门禁记录，有学生人数7834个

计划对7834个学生做下面统计分析处理：

先将原始数据处理成下面格式

学生_ID , 日期, 最早出寝室时间, 最晚会宿舍时间

"""

from datetime import *
from collections import namedtuple

DormRecord = namedtuple('DormRecord', ['students_id', 'date_record', 'first_out_time_record', 'last_in_time_record'])
students_dorm_record_dict = {}

test = DormRecord('123', '2014-2-21', '07:12:12', "21:21:21")
students_dorm_record_dict.setdefault(test.students_id,test)

print students_dorm_record_dict
print '123' in students_dorm_record_dict