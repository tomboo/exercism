from datetime import datetime
from datetime import timedelta


def add_gigasecond(dt):
    return dt + timedelta(seconds=10**9)

if __name__ == '__main__':
    print(add_gigasecond(datetime(2011, 4, 25)))
