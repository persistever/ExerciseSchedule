# -*- coding: utf-8 -*-

"""
@Class Name:
@Class Function:
下面所有使用members.memberList的地方目前均跨级调用，不是很规范，不过方便
"""
import random
DAY = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


class CScheduleTimeTable:
    def __init__(self):
        self.table = [[], [], [], [], [], [], []]
        for i in range(0, 7):
            for j in range(0, 24):
                self.table[i].append([])
        self.countTable = [[], [], [], [], [], [], []]
        for i in range(0, 7):
            for j in range(0, 24):
                self.countTable[i].append(0)

    def merge_all_member_time(self, member_list):
        for member in member_list:
            self.merge_member_time(member, member_list.index(member))

    def merge_member_time(self, member, member_index):
        for daytime in member.availableTimeList:
            self.table[daytime.day - 1][daytime.time - 1].append(member_index)
            self.countTable[daytime.day - 1][daytime.time - 1] += 1

    def schedule(self, coach, members):
        for coach_time in coach.timeList:
            available_member = self.table[coach_time.day-1][coach_time.time-1]
            # print(DAY[coach_time.day - 1] + ' ' + str(coach_time.time) + ':00 '
            #       + ' Available Member: ' + str(available_member))

            if len(available_member) == 0:
                continue
            members.get_members_conflict(available_member, self.countTable)
            available_member.sort(
                key=lambda member: members.memberList[member].priority + members.memberList[member].conflict,
                reverse=True)  # 按照学员优先级值以及冲突参数值的和从大到小排序
            # print('排序后结果 ' + DAY[coach_time.day - 1] + ' ' + str(coach_time.time) + ':00 '
            #       + ' Available Member: ' + str(available_member))

            privilege_member = []

            for member_number in available_member:
                if (members.memberList[member_number].priority + members.memberList[member_number].conflict
                        <= (members.memberList[available_member[0]].priority
                            + members.memberList[available_member[0]].conflict)+1.0 or members.memberList[member_number].priority + members.memberList[member_number].conflict
                        >= (members.memberList[available_member[0]].priority
                            + members.memberList[available_member[0]].conflict)-1.0):
                    privilege_member.append(member_number)
                else:
                    break
            # print('优先的Day: ' + str(coach_time.day)
            #       + ' Time: ' + str(coach_time.time)
            #       + ' Privilege Member: ' + str(privilege_member)
            #       + 'Value: ' + str(members.memberList[privilege_member[0]].priority
            #                         + members.memberList[privilege_member[0]].conflict))

            lucky_index = random.randint(0, len(privilege_member)-1)
            coach_time.resultMember.append(privilege_member[lucky_index])
            coach_time.is_available = 0  # 需要写一个方法
            # print('选中的Day: ' + str(coach_time.day)
            #       + ' Time: ' + str(coach_time.time)
            #       + ' Lucky Member: ' + str(privilege_member[lucky_index]))
            delete_index = members.memberList[privilege_member[lucky_index]].\
                handle_lucky_member(coach_time.day, coach_time.time)
            # print('Day' + str(coach_time.day) + 'delete_index:\n'+str(delete_index))
            for index in delete_index:
                self.table[index[0]][index[1]].remove(privilege_member[lucky_index])
                self.countTable[index[0]][index[1]] -= 1
                # if member_list[privilege_member[lucky_index]].name == 'xxx':
                #     print('***')
                #     for daytime in member_list[privilege_member[lucky_index]].availableTimeList:
                #         print('day: '+str(daytime.day)+' time: '+str(daytime.time))
            # self.print_table()

    def print_table(self):
        for i in range(0, 7):
            print(self.table[i])
        for i in range(0, 7):
            print(self.countTable[i])




