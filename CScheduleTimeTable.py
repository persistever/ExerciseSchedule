# -*- coding: utf-8 -*-

"""
@Class Name: CMemberTime
@Class Function: to describe the time of the member
"""
import random


class CScheduleTimeTable:
    def __init__(self):
        self.table = [[], [], [], [], [], [], []]
        for i in range(0, 7):
            for j in range(0, 24):
                self.table[i].append([])
        self.numTable = [[], [], [], [], [], [], []]
        for i in range(0, 7):
            for j in range(0, 24):
                self.numTable[i].append(0)

    def merge_all_member_time(self, member_list):
        for member in member_list:
            self.merge_member_time(member, member_list.index(member))

    def merge_member_time(self, member, member_index):
        for daytime in member.availableTimeList:
            self.table[daytime.day - 1][daytime.time - 1].append(member_index)
            self.numTable[daytime.day - 1][daytime.time - 1] += 1

    def schedule(self, coach_time_list, member_list):
        for coach_time in coach_time_list:
            available_member = self.table[coach_time.day-1][coach_time.time-1]
            # print('Day: '+str(coach_time.day)
            #       + ' Time: ' + str(coach_time.time)
            #       + ' Available Member: ' + str(available_member))

            if len(available_member) == 0:
                continue
            for member_number in available_member:
                member_list[member_number].get_member_conflict(self.numTable)

            available_member.sort(key=lambda member: member_list[member].priority + member_list[member].conflict, reverse=True)  # 按照学员优先级值排序
            # print('排序后Day: ' + str(coach_time.day)
            #       + ' Time: ' + str(coach_time.time)
            #       + ' Available Member: ' + str(available_member))

            privilege_member = []

            for member_number in available_member:
                if (member_list[member_number].priority + member_list[member_number].conflict) \
                        == (member_list[available_member[0]].priority + member_list[available_member[0]].conflict):
                    privilege_member.append(member_number)
                else:
                    break
            # print('优先的Day: ' + str(coach_time.day)
            #       + ' Time: ' + str(coach_time.time)
            #       + ' Privilege Member: ' + str(privilege_member))

            lucky_index = random.randint(0, len(privilege_member)-1)
            coach_time.resultMember.append(privilege_member[lucky_index])  # 需要写一个方法
            coach_time.is_available = 0  # 需要写一个方法
            # print('选中的Day: ' + str(coach_time.day)
            #       + ' Time: ' + str(coach_time.time)
            #       + ' Lucky Member: ' + str(privilege_member[lucky_index]))
            delete_index = member_list[privilege_member[lucky_index]].handle_lucky_member(coach_time.day, coach_time.time)
            # print('Day' + str(coach_time.day) + 'delete_index:\n'+str(delete_index))
            for index in delete_index:
                self.table[index[0]][index[1]].remove(privilege_member[lucky_index])
                self.numTable[index[0]][index[1]] -= 1
            # self.print_table()

    def print_table(self):
        for i in range(0, 7):
            print(self.table[i])
        for i in range(0, 7):
            print(self.numTable[i])




