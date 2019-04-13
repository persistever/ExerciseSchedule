# -*- coding: utf-8 -*-

"""
@Class Name: CMember
@Class Purpose:
"""

from CTime import CTime
import math
DAY = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


class CMember:
    memberCount = 0
    memberNotSchedule = 0

    def __init__(self, name, expect_time_number, priority, init_available_time_list):
        self.name = name
        self.expectTimeNumber = expect_time_number
        self.restTimeNumber = expect_time_number
        self.initPriority = priority
        self.priority = priority
        self.initAvailableTimeList = init_available_time_list
        self.availableTimeList = init_available_time_list
        self.scheduleTimeList = []
        self.isSchedule = 0
        self.conflict = 0.0
        CMember.memberCount += 1
        CMember.memberNotSchedule = CMember.memberCount

    def handle_lucky_member(self, day, time):
        delete_daytime = []
        delete_index = []
        self.scheduleTimeList.append(CTime(day, time))
        self.restTimeNumber -= 1
        if self.restTimeNumber == 0:
            self.isSchedule = 1
            CMember.memberNotSchedule -= 1
            # print('已安排完成 ' + str(CMember.memberCount - CMember.memberNotSchedule)+' 人')
            for daytime in self.availableTimeList:
                delete_daytime.append((daytime.day-1, daytime.time-1))
                delete_index.append(daytime)
        else:
            for daytime in self.availableTimeList:
                if daytime.day == day - 1 or daytime.day == day or daytime.day == day + 1:
                    delete_daytime.append((daytime.day-1, daytime.time-1))
                    delete_index.append(daytime)
        for index in delete_index:
            self.availableTimeList.remove(index)
        self.get_member_priority()
        return delete_daytime

    def sort_schedule_time_list(self):
        self.scheduleTimeList.sort(key=lambda x: (x.day, x.time))

    def print_member_time(self):
        print('姓名: ' + self.name + '\n已安排的时间为: ')
        for daytime in self.scheduleTimeList:
            print(DAY[daytime.day - 1] + ' ' + str(daytime.time) + ':00')
        if self.isSchedule == 0:
            print("尚有 " + str(self.restTimeNumber) + " 节课无法安排，请联系教练")

    def print_member_unschedule_name(self):
        if self.isSchedule == 0:
            print(self.name)

    def get_member_init_priority(self, lucky_member_list):
        if self.name in lucky_member_list:
            self.initPriority += 1

    def get_member_priority(self):
        # self.priority = self.priority
        # self.priority = self.initPriority*1.0 + (self.restTimeNumber*1.0)/((self.expectTimeNumber*1.0) * math.log(len(self.availableTimeList)+2.0))
        self.priority = self.initPriority * 1.0 + (4.0 - self.restTimeNumber) / (
                    (self.expectTimeNumber * 1.0) * math.log(len(self.availableTimeList) + 2.0))
        # self.priority = self.initPriority * 1.0

    def get_member_conflict(self, num_table):
        temp_count = 0
        for i in range(len(self.availableTimeList)):
            if i == 0:
                continue
            else:
                temp_count += num_table[self.availableTimeList[i].day-1][self.availableTimeList[i].time-1]
        if len(self.availableTimeList) >= 2:
            self.conflict = temp_count*1.0/(len(self.availableTimeList)-1.0)*self.restTimeNumber
        else:
            self.conflict = 0








