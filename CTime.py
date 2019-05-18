# -*- coding: utf-8 -*-

"""
@Class Name: CMemberTime
@Class Function: to describe the time of the member
"""
DAY = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


class CTime:
    def __init__(self, day, time):
        self.day = day
        self.time = time

    def print_time(self):
        print(DAY[self.day - 1] + ' ' + str(self.time) + ':00' + '\n')
