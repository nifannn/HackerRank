import calendar
if __name__ == '__main__':
    month, day, year = list(map(int, input().split(" ")))
    print(list(calendar.day_name)[calendar.weekday(year, month, day)].upper())
