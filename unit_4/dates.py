# all the seconds in a minute
def gen_secs():
    for sec in range(60):
        yield sec


# all the minutes in an hour
def gen_minutes():
    for minute in range(60):
        yield minute


# all hours in a day
def gen_hours():
    for hour in range(24):
        yield hour


# all times in a day
def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


# all the years since the start parameter
def gen_years(start=2019):
    for year in range(start, 2024):
        yield year


# months in a year
def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31, 2: 29 if leap_year else 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    for day in range(1, days_in_month[month] + 1):
        yield day


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def gen_date():
    for year in gen_years():
        leap_year = is_leap_year(year)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


def main():
    # דוגמת הרצה של הפונקציה gen_date
    gen = gen_date()
    for _ in range(1000000):
        date = next(gen)
    print(date)
    for _ in range(1000000):
        date = next(gen)
    print(date)
    for _ in range(1000000):
        date = next(gen)
    print(date)


if __name__ == "__main__":
    main()
