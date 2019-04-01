# -*- coding: utf-8 -*-

"""
@Class Name: CMemberTime
@Class Function: to describe the time of the member
"""
DAY = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


class CCoachTime:
    def __init__(self, day, time):
        self.day = day
        self.time = time
        # self.availableMember = []
        self.resultMember = []
        self.selectNumber = 0
        self.is_available = 1

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







