# coding:utf-8

"""
create on Jan 15,2017 by Wenyan Yu

对寝室的门禁数据进行分析

从初步的门禁数据分析可知，整个训练集共有2115065条门禁记录，有学生人数7834个

计划对7834个学生做下面统计分析处理：

先将原始数据处理成下面格式

学生_ID(stu_id) , 日期(date_info), 最早出寝室时间(first_out), 最晚会宿舍时间(last_in)

拟用两层字典（dict）加一个namedtuple来表示该信息

{stu_id1: {date_info1: (first_out, last_out)
           date_info2: (first_out, last_out)
           date_info3: (first_out, last_out)
           ...

        }
 stu_id2: {date_info1: (first_out, last_out)
           date_info2: (first_out, last_out)
           date_info3: (first_out, last_out)
           ...

        }
 ...
}

stu_id_dict = {}
date_info_dict = {}
DormRecord = namedtuple('DormRecord', ['first_out', 'last_in'])
statistic_info = DormRecord(dt1.time(), dt2.time())

统计之后的数据规模大概是
7834 × 365 = 286160 (还可以吧)

测试数据集如下：
13126,"2014/01/21 03:31:11","1"
13126,"2014/01/21 04:53:55","0"

其中“1”表示出寝室，"0"表示进寝室


处理数据的大致思路如下：

1.读取测试数据集的一行数据
2.将该行数据处理成stu_id, date_info, time_info, status
3.判断stu_id是否存在于stu_id_dict中
    如不存在：
        if status == "1":
            first_out = time_info
            last_in = None
        if status == "0":
            first_out = None
            last_in = time_info
        在stu_id_dict中添加一条记录{stu_id_dict: {date_info: (first_out, last_in)}}
    如果存在：
        判断date_info 时候存在于stu_id_dict.get(stu_info_dict)中
            如果不存在：
                在stu_id_dict.get(stu_info_dict)中添加一条记录
            如果存在：
                则判断status的状态，然后根据规则，修改first_out和last_in
4.如此循环直至，训练集所有的记录都处理完成


"""

from datetime import *
from collections import namedtuple
import pickle


def store_structured_data(data_obj, file_to_store):
    """
    将结构化数据存储到文件中
    :param data_obj:
    :param file_to_store:
    :return: None
    """
    try:
        fw = open(file_to_store, 'w')
        pickle.dump(data_obj, fw)
    finally:
        fw.close()


def retrieve_structured_data(file_of_retrieve):
    """
    从文件中读取结构化数据
    :param data_obj:
    :param file_of_retrieve:
    :return: data_obj
    """
    try:
        fr = open(file_of_retrieve)
        data_obj = pickle.load(fr)
        fr.close()
        return data_obj
    except (IOError,UnboundLocalError) as e:
        print "文件打开失败！"
        return None





"""
DormRecord = namedtuple('DormRecord', ['first_out', 'last_in'])
students_dorm_record_dict = {}
dt1 = datetime.strptime('2014/01/21 03:31:11', '%Y/%m/%d %H:%M:%S')
dt2 = datetime.strptime('2014/01/21 21:31:11', '%Y/%m/%d %H:%M:%S')

statistic_tuple = DormRecord(dt1.time(),dt2.time())

statistic_dict = {}
statistic_dict.setdefault(dt1.date(),statistic_tuple )
students_id = 13126
students_dorm_record_dict.setdefault(students_id,statistic_dict)

dt3 = datetime.strptime('2014/01/22 05:31:11', '%Y/%m/%d %H:%M:%S')
dt4 = datetime.strptime('2014/01/22 11:31:11', '%Y/%m/%d %H:%M:%S')

statistic_tuple = DormRecord(dt3.time(),dt4.time())

statistic_dict.setdefault(str(dt3.date()),statistic_tuple )
students_id = 13126
students_dorm_record_dict.setdefault(students_id,statistic_dict)
print students_dorm_record_dict
print 13126 in students_dorm_record_dict
print students_dorm_record_dict.get(13126).get('2014-01-22').first_out
test_pickle = "Data/dorm/test_pickle.txt"
store_structured_data(students_dorm_record_dict, test_pickle)
# print retrieve_structured_data(test_pickle)
"""