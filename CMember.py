# -*- coding: utf-8 -*-

"""
@Class Name: CMember
@Class Purpose:
"""

from CTime import CTime
import math
import random
DAY = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


class CEachMember:
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
        self.canChooseContinuously = 0

    def print_each_member_info(self):
        print('Name: ' + self.name)
        print("有空时间：\n")
        for daytime in self.availableTimeList:
            daytime.print_time()
        print("Priority: " + str(self.priority) + "\n")
        print("连续选课：" + str(self.canChooseContinuously) + "\n")

    def handle_lucky_member(self, day, time):
        delete_daytime = []
        delete_index = []
        self.scheduleTimeList.append(CTime(day, time))
        self.restTimeNumber -= 1
        if self.restTimeNumber == 0:
            self.isSchedule = 1
            # print('已安排完成 ' + str(CMember.memberCount - CMember.memberNotSchedule)+' 人')
            for daytime in self.availableTimeList:
                delete_daytime.append((daytime.day-1, daytime.time-1))
                delete_index.append(daytime)
        else:
            if self.canChooseContinuously == 0:
                for daytime in self.availableTimeList:
                    if daytime.day == day - 1 or daytime.day == day or daytime.day == day + 1:
                        delete_daytime.append((daytime.day-1, daytime.time-1))
                        delete_index.append(daytime)
            else:
                for daytime in self.availableTimeList:
                    if daytime.day == day:
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
            self.initPriority += 10.0

    def get_member_priority(self):
        # self.priority = self.priority * 1.0)
        self.priority = self.initPriority * 1.0 + (4.0 - self.restTimeNumber) / (
                     (self.expectTimeNumber * 1.0) * math.log(len(self.availableTimeList) + 2.0))

    def get_member_conflict(self, count_table):
        temp_count = 0
        for i in range(len(self.availableTimeList)):
            if i == 0:
                continue
            else:
                temp_count += count_table[self.availableTimeList[i].day-1][self.availableTimeList[i].time-1]
        if len(self.availableTimeList) >= 2:
            self.conflict = temp_count*1.0/(len(self.availableTimeList)-1.0)*self.restTimeNumber
        else:
            self.conflict = 0

    def judge_choose_continuously(self):
        temp_day = []
        for daytime in self.availableTimeList:
            if daytime.day not in temp_day:
                temp_day.append(daytime.day)
        if len(temp_day) <= self.expectTimeNumber:
            self.canChooseContinuously = 1


class CMembers:
    def __init__(self, coach_name):
        self.memberList = []
        self.luckyMemberList = []
        self.memberCount = 0
        self.memberNotSchedule = 0
        self.coachName = coach_name

    def get_lucky_member_list(self, file_name):
        temp_list = []
        f = open(file_name, 'r')
        line = f.readline()
        while line:
            if line[0] == '#':
                break
            elif line == "上周程序没有完全安排的名单：\n":
                line = f.readline()
            else:
                temp_list.append(line.strip())
                line = f.readline()
        f.close()
        self.luckyMemberList = temp_list

    def print_lucky_member_list(self):
        print("luckyMemberList = "+str(self.luckyMemberList))

    def get_available_time_of_member(self, file_name, coach_time_list):
        temp_list = []
        f = open(file_name, 'r')
        line = f.readline()
        temp_priority = None
        temp_name = None
        temp_expect_number = None
        temp_available_time_list = None
        while line:
            line = line.replace(' ', ' ')
            line = line.strip()
            line = line.replace('（', '(')
            line = line.replace('）', ')')
            if line[0] == '@':
                temp_available_time_list = []
                if line.find('*') == -1:
                    temp_priority = 0
                else:
                    temp_priority = line[line.find('*') + 1:]
                    temp_priority = temp_priority.strip()
                temp_name = line[1:line.find('(')]
                temp_name = temp_name.strip()
                temp_expect_number = line[line.find('(') + 1:line.find(')')]
            elif "1234567".find(line[0]) != -1:
                line = line.replace('（', '(')
                line = line.replace('）', ')')
                temp_day = line[0]
                temp_string = line[line.find('(') + 1:line.find(')')]
                temp_time_list = temp_string.split(' ')
                for time in temp_time_list:
                    if time != '' and time != ' ':
                        flag = 0
                        for daytime in coach_time_list:
                            if daytime.day == int(temp_day) and daytime.time == int(time):
                                flag = 1
                                break
                        if flag == 1:
                            temp_available_time_list.append(CTime(int(temp_day), int(time)))
            elif line[0] == '#':
                temp_member = CEachMember(temp_name, int(temp_expect_number), int(temp_priority) * 1.0,
                                          temp_available_time_list)
                temp_member.get_member_init_priority(self.luckyMemberList)
                temp_member.get_member_priority()
                temp_list.append(temp_member)
                self.memberCount += 1
                self.memberNotSchedule += 1
            line = f.readline()
        f.close()
        self.memberList = temp_list

    def print_members_info(self):
        print("本次选课总人数" + str(self.memberCount)+"\n")
        for each_member in self.memberList:
            each_member.print_each_member_info()

    def preparations(self):
        random.shuffle(self.memberList)
        for each_member in self.memberList:
            each_member.judge_choose_continuously()
            if len(each_member.availableTimeList) == 0:
                print(each_member.name + "没有填写可约时间\n")

    def get_members_conflict(self, available_member, count_table):
        for member_number in available_member:
            self.memberList[member_number].get_member_conflict(count_table)

    def refresh_member_not_schedule(self):
        temp_num = 0
        for each_member in self.memberList:
            if each_member.isSchedule == 0:
                temp_num += 1
        self.memberNotSchedule = temp_num

