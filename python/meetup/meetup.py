import datetime
import calendar

weekday_token = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
    }

modifier_token = {
    '1st': 0,
    '2nd': 1,
    '3rd': 2,
    '4th': 3,
    '5th': 4,
    'last': -1,
    'teenth': 100
    }


def meetup_day(year=2000, month=1, weekday='Monday', modifier='1st'):
    weekday_value = weekday_token[weekday]
    modifier_value = modifier_token[modifier]

    cal = calendar.monthcalendar(year, month)
    col = [week[weekday_value] for week in cal if week[weekday_value] != 0]

    if modifier == 'teenth':
        for day in col:
            if day in range(13, 20):
                break
    else:
        day = col[modifier_value]

    return datetime.date(year, month, day)


if __name__ == '__main__':
    print(meetup_day())
    print(meetup_day(2013, 5, 'Tuesday', '1st'))  # date(2013, 5, 7)
    print(meetup_day(2013, 5, 'Monday', 'teenth'))  # date(2013, 5, 13)
    # print(meetup_day(2015, 2, 'Monday', '5th'))
