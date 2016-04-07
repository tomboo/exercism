from datetime import date
from calendar import Calendar

wkday_dict = {
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


def meetup_day(yr, mo, wkday, desc):
    # get weekday index
    wkday_i = wkday_dict[wkday]
    match_value = match_token[desc]

    # get list of weeks in month and year
    cal = Calendar()
    wk_list = cal.monthdayscalendar(yr, mo)
    # list of each date corresponding to given weekday
    wkday_dates = [wk[wkday_i] for wk in wk_list if wk[wkday_i] != 0]
    # get date based on (desc)ription
    if desc == 'teenth':
        for d in wkday_dates:
            if d in range(13, 20):
                day = d
    else:
        day = wkday_dates[match_value]

    return date(yr, mo, day)


if __name__ == '__main__':
    print(meetup_day(2000, 1, 'Monday', '1st'))
