# -*- coding: utf-8 -*-

"""
@File Name: GetInfo
@File Purpose:
"""
# import GetInfo


from CCoach import CCoach
from CMember import CMembers
from CScheduleTimeTable import CScheduleTimeTable


if __name__ == "__main__":

    coach = CCoach()
    coach.get_time_list_of_coach("Data/CoachTime.txt")

    members = CMembers("刘迎")
    members.get_lucky_member_list("Data/LuckyThisWeek.txt")
    members.print_lucky_member_list()
    members.get_available_time_of_member("Data/MemberTime.txt", coach.timeList)
    members.preparations()
    # members.print_members_info()

    scheduleTimeTable = CScheduleTimeTable()
    scheduleTimeTable.merge_all_member_time(members.memberList)
    # scheduleTimeTable.print_table()
    coach.sort_by_select_number(scheduleTimeTable.countTable)
    # coach.print_time_list_of_coach()

    scheduleTimeTable.schedule(coach, members)
    members.refresh_member_not_schedule()
    coach.print_schedule_result_of_coach(members.memberList)
    coach.write_schedule_result_of_coach_to_file(members.memberList)
    if members.memberNotSchedule == 0:
        print('\n所有人均已成功安排')
    else:
        print('\n共有 ' + str(members.memberNotSchedule) + ' 人没有完全安排，名单如下：')
        for member in members.memberList:
            member.print_member_unschedule_name()

    for member in members.memberList:
        member.sort_schedule_time_list()
        print('\n')
        member.print_member_time()

    # Create a successfile to show all the process has completed
    f = open('Data/success', 'a')
    f.close()




