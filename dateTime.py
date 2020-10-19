# Program Name: dateTime.py
# Program Author: Russell Holmes
# Last Edit Date: 10/19/2020

from datetime import datetime, timedelta


def half_birthday(year, month, day):
    birthday = datetime(year, month, day)
    return birthday + timedelta(weeks=24)


if __name__ == '__main__':
    print(half_birthday(2000, 1, 1))
