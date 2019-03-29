# -*- coding: utf-8 -*-

"""
@Class Name: CTimeTable
@Class Function:
"""


class CTimeList:
    timeList = []
    timeNumber = 0

    def __init__(self, time_list=[]):
        self.timeList = time_list
        self.timeNumber = len(time_list)

    def refresh_time_list(self, day):
        for time in self.timeList:
            if time.day == day:
                self.timeList.remove(time)
            if time.day > day:
                break



