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
"""

from datetime import *
from collections import namedtuple
import pickle

DormRecord = namedtuple('DormRecord', ['first_out', 'last_in'])  # 需要统计的信息以namedtuple的形式表示
LineInfo = namedtuple('LineInfo', ['stu_id', 'date_info', 'time_info', 'status'])


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


def manipulate_line_info(line):
    """
    给定line，将该行数据处理成stu_id, date_info, time_info, status
    :param line:
    :return: LineInfo
    """
    if line is not None:
        line = line.split(",")
        # print line
        stu_id = str(line[0])
        dt = datetime.strptime(line[1].strip('\"'), '%Y/%m/%d %H:%M:%S')
        date_info = dt.date()
        time_info = dt.time()
        status = line[2].strip().strip('\"')
        return LineInfo(stu_id, date_info, time_info, status)
    else:
        print "该行信息为空！"
        return None



def manipulate_data_info(file_to_manipulate, line_number):
    """
    根据要求把数据处理成需要的格式,并将数据存储到dorm_info_pickle.txt
    其中line_number表示需要处理的行数
    :param file_to_manipulate:
    :param line_number:
    :return: stu_id_dict
    """
    stu_id_dict = {}
    date_info_dict = {}
    try:
        fw = open(file_to_manipulate, 'rb')
        for line in fw.readlines():
            line_info = manipulate_line_info(line)
            print line_info
            line_number -= 1
            if line_number == 0:
                break
    finally:
        fw.close()
    return stu_id_dict


if __name__ == "__main__":
    dorm_train = "Data/dorm/dorm_train.txt"
    print manipulate_data_info(dorm_train, 5)