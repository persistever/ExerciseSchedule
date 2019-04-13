# -*- coding: utf-8 -*-

"""
@File Name: GetInfo
@File Purpose:
"""

from CCoachTime import CCoachTime
from CMember import CMember
from CTime import CTime


def get_available_time_of_coach(file_name):
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
        temp_string = line[line.find('(')+1:line.find(')')]
        temp_time_list = temp_string.split(' ')
        for time in temp_time_list:
            if time != '' and time != ' ':
                temp_list.append(CCoachTime(int(temp_day), int(time)))
        line = f.readline()
    f.close()
    return temp_list


def get_available_time_of_member(file_name, coach_time_list, lucky_member_list):
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
                temp_priority = line[line.find('*')+1:]
                temp_priority = temp_priority.strip()
            temp_name = line[1:line.find('(')]
            temp_name = temp_name.strip()
            temp_expect_number = line[line.find('(')+1:line.find(')')]
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
            # print(temp_name)
            # print(int(temp_expect_number))
            # print(int(temp_priority))
            # print(temp_available_time_list)
            temp_member = CMember(temp_name, int(temp_expect_number), int(temp_priority)*1.0, temp_available_time_list)
            temp_member.get_member_init_priority(lucky_member_list)
            temp_member.get_member_priority()
            # print(temp_name)
            # print(temp_member.priority)
            temp_list.append(temp_member)
        # print(line)
        line = f.readline()
    f.close()
    return temp_list


def get_lucky_member_list(file_name):
    temp_list = []
    f = open(file_name, 'r')
    line = f.readline()
    while line:
        if line[0] == '#':
            break
        elif line == "上周程序没有完全安排的名单：\n":
            continue
        else:
            temp_list.append(line.strip())
		line = f.readline()
    f.close()
    return temp_list
