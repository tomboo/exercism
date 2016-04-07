from datetime import date
from calendar import monthrange

weekday_token = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
    }

match_token = {
    '1st': 0,
    '2nd': 1,
    '3rd': 2,
    '4th': 3,
    '5th': 4,
    'last': -1,
    'teenth': -2
    }


def meetup_day(year=2000, month=1, weekday='Monday', match='1st'):
    weekday_value = weekday_token[weekday]
    match_value = match_token[match]

    bom, days = monthrange(year, month)
    firstmatch = (weekday_value - bom) % 7 + 1
    match_range = range(firstmatch, days + 1, 7)
    if match == 'teenth':
        for day in match_range:
            if day in range(13, 20):
                break
    else:
        day = match_range[match_value]

    return date(year, month, day)


if __name__ == '__main__':
    print(meetup_day())
    print(meetup_day(2013, 5, 'Tuesday', '1st'))  # date(2013, 5, 7)
    print(meetup_day(2013, 5, 'Monday', 'teenth'))  # date(2013, 5, 13)
    # print(meetup_day(2015, 2, 'Monday', '5th'))
