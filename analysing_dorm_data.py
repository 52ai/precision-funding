# coding:utf-8

"""
create on Jan 15,2017 by Wenyan Yu

对寝室的门禁数据进行分析
从初步的门禁数据分析可知，整个训练集共有2115065条门禁记录，有学生人数7834个
计划对7834个学生做下面统计分析处理：
先将原始数据处理成下面格式
学生_ID(stu_id) , 日期(date_info), 最早出寝室时间(first_out), 最晚会宿舍时间(last_in)
拟用两层字典（dict）加一个namedtuple来表示该信息
{stu_id1: {date_info1: (first_out, last_out),
           date_info2: (first_out, last_out),
           date_info3: (first_out, last_out),
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
LineInfo = namedtuple('LineInfo', ['stu_id', 'date_info', 'time_info', 'status', 'dorm_record'])


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
    给定line，将该行数据处理成stu_id, date_info, time_info, status, dorm_record
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
        if status == "1":
            first_out = time_info
            last_in = None
        elif status == "0":
            first_out = None
            last_in = time_info
        dorm_record = DormRecord(first_out, last_in)
        return LineInfo(stu_id, date_info, time_info, status, dorm_record)
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
    # 早上出门的时间默认为23:59:59 晚上回去的时间默认为00:00:00

    try:
        fw = open(file_to_manipulate, 'rb')
        for line in fw.readlines():
            line_info = manipulate_line_info(line)
            date_info_dict = {} # 初始化,门禁时间记录信息字典
            """
            开始处理
            """
            # print line_info
            # 如果stu_id不在stu_id_dict中,则需要新增记录
            if line_info.stu_id not in stu_id_dict:
                date_info_dict.setdefault(line_info.date_info, line_info.dorm_record )
                stu_id_dict.setdefault(line_info.stu_id, date_info_dict)
            elif line_info.stu_id in stu_id_dict:
                # 如果stu_id记录已存在且日期记录不存在,则在该stu_id中新增日期记录
                if line_info.date_info not in stu_id_dict.get(line_info.stu_id):
                    # print stu_id_dict.get(line_info.stu_id)
                    date_info_dict = stu_id_dict.get(line_info.stu_id)
                    # print date_info_dict
                    date_info_dict.setdefault(line_info.date_info, line_info.dorm_record)
                    # print date_info_dict
                # 如果stu_id记录已存在且日期记录也存在,则需要修改该stu_id中日期记录的时间记录值
                elif line_info.date_info in stu_id_dict.get(line_info.stu_id):
                    # 如果状态信息为"1",则表明该记录为出寝室的记录
                    if line_info.status == "1":
                        new_time = line_info.dorm_record.first_out
                        old_time = stu_id_dict.get(line_info.stu_id).get(line_info.date_info).first_out
                        # print "new:",new_time
                        # print "old:",old_time
                        if old_time is not None:
                            # 由于记录是按照时间顺序排列的,实际上new_time一般都要比old_time大,下面的这个if里的内容不执行
                            # print new_time < old_time
                            if new_time < old_time:
                                new_dorm_record = DormRecord(new_time, stu_id_dict.get(line_info.stu_id).get(line_info.date_info).last_in)
                                # 若新时间记录比旧时间记录要早,那么将旧时间记录更新为新时间记录
                                stu_id_dict.get(line_info.stu_id)[line_info.date_info] = new_dorm_record
                                #print "update old:", stu_id_dict.get(line_info.stu_id).get(line_info.date_info).first_out

                        elif old_time is None:
                            new_dorm_record = DormRecord(new_time, stu_id_dict.get(line_info.stu_id).get(line_info.date_info).last_in)
                            # 若旧时间记录为None,则更新时间记录为新记录
                            stu_id_dict.get(line_info.stu_id)[line_info.date_info] = new_dorm_record
                            # print "update old:", stu_id_dict.get(line_info.stu_id).get(line_info.date_info).first_out
                    # 如果状态信息为"0",则表明该记录为进寝室的记录
                    elif line_info.status == "0":
                        new_time = line_info.dorm_record.last_in
                        old_time = stu_id_dict.get(line_info.stu_id).get(line_info.date_info).last_in
                        # print "new:", new_time
                        # print "old:", old_time
                        if old_time is not None:
                            # 如果old_time已经有值,则根据规则更新它的值
                            if new_time > old_time:
                                # print new_time > old_time
                                new_dorm_record = DormRecord(stu_id_dict.get(line_info.stu_id).get(line_info.date_info).first_out, new_time)
                                # 若新时间记录比旧时间记录要晚,那么将旧时间记录更新为新时间记录
                                stu_id_dict.get(line_info.stu_id)[line_info.date_info] = new_dorm_record
                                # print "update old:", stu_id_dict.get(line_info.stu_id).get(line_info.date_info).last_in

                        elif old_time is None:
                            new_dorm_record = DormRecord(stu_id_dict.get(line_info.stu_id).get(line_info.date_info).first_out, new_time)
                            # 若旧时间记录为None,则更新时间记录为新记录
                            stu_id_dict.get(line_info.stu_id)[line_info.date_info] = new_dorm_record
                            # print "update old:", stu_id_dict.get(line_info.stu_id).get(line_info.date_info).last_in

            """
            结束处理
            """
            # print line_info
            line_number -= 1
            if line_number == 0:
                break
    finally:
        fw.close()
    return stu_id_dict


if __name__ == "__main__":
    dorm_train = "Data/dorm/dorm_train.txt"
    print "开始处理数据:"
    time_start = datetime.now()
    # stu_id_dict = manipulate_data_info(dorm_train, 2115065) # 训练集的记录总数为2115065
    time_end = datetime.now()
    print "数据处理结束!time consuming: %s" %(time_end-time_start)
    # store_structured_data(stu_id_dict, "Data/dorm/stu_dorm_info_dict.txt")
    """
    retrieve_data = retrieve_structured_data("Data/dorm/stu_dorm_info_dict.txt")
    for keys in retrieve_data:
        print retrieve_data[keys]
    """
    retrieve_data = retrieve_structured_data("Data/dorm/stu_dorm_info_dict.txt")
    print retrieve_data
