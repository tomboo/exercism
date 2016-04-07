#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import timedelta, date

weekdays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
            "Friday": 4, "Saturday": 5, "Sunday": 6}
weeks_of_the_month = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3,
                      "5th": 4, "last": -1}


class MeetupDayException(BaseException):
    pass


def meetup_day(year, month, weekday, occurrence):

    if occurrence == "teenth":
        for day in range(13, 20):
            if weekdays[weekday] == date(year, month, day).weekday():
                return date(year, month, day)
    else:
        curr_date = date(year, month, 1)  # first day of the month

        # finding first suitable weekday of the month
        if weekdays[weekday] < curr_date.weekday():
            curr_date += timedelta(days=7 + weekdays[weekday] -
                            curr_date.weekday())
        else:
            curr_date += timedelta(days=weekdays[weekday] -
                            curr_date.weekday())

        # retrieving all suitable weekdays of the month
        all_weekdays_in_month = list()
        while curr_date.month == month:
            all_weekdays_in_month.append(curr_date)
            curr_date += timedelta(days=7)

        # retrieving weekday of the month with the given occurrence
        try:
            curr_date = all_weekdays_in_month[weeks_of_the_month[occurrence]]
        except IndexError:
            raise MeetupDayException

        return curr_date

if __name__ == '__main__':
    meetup_day(2015, 2, 'Monday', '5th')
