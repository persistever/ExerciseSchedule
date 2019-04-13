# -*- coding: utf-8 -*-

"""
@File Name: GetInfo
@File Purpose:
"""
import GetInfo
import random
import operator
from CMember import CMember
from CScheduleTimeTable import CScheduleTimeTable


if __name__ == "__main__":

    coachTimeList = GetInfo.get_available_time_of_coach("Data/CoachTime.txt")
    # for item in coachTimeList:
    #     print('day: '+str(item.day)+' time: '+str(item.time))
    luckyMemberList = GetInfo.get_lucky_member_list("Data/LuckyThisWeek.txt")
    memberList = GetInfo.get_available_time_of_member("Data/MemberTime.txt", coachTimeList, luckyMemberList)
    random.shuffle(memberList)

    print("luckyMemberList = "+str(luckyMemberList))
    # for item in memberTimeList:
    #     print(item.name)
    #     print(item.expectNumber)
    #     print(item.priority)
    #     print(item.availableTimeList)
    #     for time in item.availableTimeList:
    #         print('day: '+str(time.day)+' time: '+str(time.time))
    coachTimeTable = CScheduleTimeTable()
    coachTimeTable.merge_all_member_time(memberList)
    # coachTimeTable.print_table()

    for daytime in coachTimeList:
        daytime.get_select_number(coachTimeTable.numTable)
    coachTimeList.sort(key=operator.attrgetter('selectNumber'), reverse=False)
    # for item in coachTimeList:
    #     print('day: '+str(item.day)+' time: '+str(item.time)+' selectNumber: '+str(item.selectNumber))
    coachTimeTable.schedule(coachTimeList, memberList)

    coachTimeList.sort(key=lambda x: (x.day, x.time))
    for coach_time in coachTimeList:
        coach_time.print_coach_time_schedule(memberList)

    if CMember.memberNotSchedule == 0:
        print('\n所有人均已成功安排')
    else:
        print('\n共有 ' + str(CMember.memberNotSchedule) + ' 人没有完全安排，名单如下：')
        for member in memberList:
            member.print_member_unschedule_name()

    for member in memberList:
        member.sort_schedule_time_list()
        print('\n')
        member.print_member_time()



