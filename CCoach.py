# -*- coding: utf-8 -*-
"""
@File Name: CCoach.py
@File Purpose:
"""

import operator
DAY = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

"""
@Class Name: CMemberTime
@Class Function: to describe a certain time of the coach
"""


class CCoachTime:
    def __init__(self, day, time):
        self.day = day
        self.time = time
        self.resultMember = []  # 谁选了这节课，用列表形式方便之后拓展
        self.selectNumber = 0  # 该时间的选择人数
        self.is_available = 1  # 该时间是否可选

    def print_coach_time_schedule(self, member_list):
        if self.is_available == 1:
            print(DAY[self.day-1]
                  + ' ' + str(self.time) + ':00'
                  + ' 未安排')
        else:
            print(DAY[self.day-1]
                  + ' ' + str(self.time) + ':00'
                  + ' ' + str(member_list[self.resultMember[0]].name))

    def get_select_number(self, num_table):
        self.selectNumber = num_table[self.day-1][self.time-1]

    def print_time_of_coach(self):
        print(DAY[self.day - 1] + ' ' + str(self.time) + ':00 ' + "选课人数：" + str(self.selectNumber))


"""
@Class Name: CMemberTimeList
@Class Function: to describe the all the time points of the coach
"""


class CCoach:
    def __init__(self):
        self.timeList = []
        self.initTimeList = []
        self.CountList = 0

    def get_time_list_of_coach(self, file_name):
        temp_list = []
        f = open(file_name, 'r')
        line = f.readline()
        while line:
            line = line.replace(' ', ' ')
            line = line.strip()
            line = line.replace('（', '(')
            line = line.replace('）', ')')
            # print(line)
            temp_day = line[0]
            if temp_day == '#':
                break
            temp_string = line[line.find('(') + 1:line.find(')')]
            temp_time_list = temp_string.split(' ')
            for time in temp_time_list:
                if time != '' and time != ' ':
                    temp_list.append(CCoachTime(int(temp_day), int(time)))
            line = f.readline()
        f.close()
        self.timeList = temp_list
        self.initTimeList = temp_list

    def sort_by_select_number(self, count_table):
        for each_time in self.timeList:
            each_time.get_select_number(count_table)
        self.timeList.sort(key=operator.attrgetter('selectNumber'), reverse=False)

    def print_time_list_of_coach(self):
        for each_time in self.timeList:
            each_time.print_time_of_coach()

    def print_schedule_result_of_coach(self, member_list):
        self.timeList.sort(key=lambda x: (x.day, x.time))
        for each_time in self.timeList:
            each_time.print_coach_time_schedule(member_list)
