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
print students_dorm_record_dict.get(13126).get('2014-01-22')
test_pickle = "Data/dorm/test_pickle.txt"
store_structured_data(students_dorm_record_dict, test_pickle)

# print retrieve_structured_data(test_pickle)