# -*- coding: utf-8 -*-

"""
@File Name: GetInfo
@File Purpose:
"""
import GetInfo
import random
from CMember import CMember
from CScheduleTimeTable import CScheduleTimeTable


if __name__ == "__main__":

    coachTimeList = GetInfo.get_available_time_of_coach("Data/CoachTime.txt")
    # for item in coachTimeList:
    #     print('day: '+str(item.day)+' time: '+str(item.time))
    memberList = GetInfo.get_available_time_of_member("Data/MemberTime.txt", coachTimeList)
    random.shuffle(memberList)
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
    coachTimeTable.schedule(coachTimeList, memberList)

    for coach_time in coachTimeList:
        coach_time.print_coach_time_schedule(memberList)

    if CMember.memberNotSchedule == 0:
        print('\n所有人均已成功安排')
    else:
        print('\n共有 ' + str(CMember.memberNotSchedule) + ' 人没有完全安排，名单如下：')
        for member in memberList:
            member.print_member_unschedule_name()

    for member in memberList:
        print('\n')
        member.print_member_time()



