#!/usr/bin/python3

from datetime import *


# ---------------------------------------------
# String helper functions
# ---------------------------------------------
def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    # Follows Python's 0-based indexing
    if amount == -1:  # return all from position
        if offset >= len(s):
            return ""
        return s[-(len(s) - offset + 1):]
    else:
        return s[offset:offset + amount]


# ---------------------------------------------
# Return number of days for a given month & year
# ---------------------------------------------
def days_in_month(month, year):
    dt_format = "%Y-%m-%d"
    match month:
        case 2:
            temp_date = f"{year}-03-01"
            d = datetime.strptime(temp_date, dt_format)
            d = d + timedelta(days=-1)  # last day of February
            return int(right(d.strftime(dt_format), 2))
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30


# ---------------------------------------------
# Movable holidays handling
# ---------------------------------------------
def calc_movable_holidays(year):
    global movHolDay, movHolMonth, movHolYear
    movHolDay = []
    movHolMonth = []
    movHolYear = year

    f = ""

    # 0=Good Friday, 1=Easter Sunday, 2=Easter Monday, 3=Ascension Day, 4=Whit Monday
    f = holiday_good_friday(year)
    movHolMonth.append(int(mid(f, 5, 2)))
    movHolDay.append(int(right(f, 2)))

    f = holiday_easter(year)
    movHolMonth.append(int(mid(f, 5, 2)))
    movHolDay.append(int(right(f, 2)))

    f = holiday_easter_monday(year)
    movHolMonth.append(int(mid(f, 5, 2)))
    movHolDay.append(int(right(f, 2)))

    f = holiday_ascension(year)
    movHolMonth.append(int(mid(f, 5, 2)))
    movHolDay.append(int(right(f, 2)))

    f = holiday_whit_monday(year)
    movHolMonth.append(int(mid(f, 5, 2)))
    movHolDay.append(int(right(f, 2)))


# ---------------------------------------------
# Return holiday name or empty string
# ---------------------------------------------
def is_holiday(y, m, d):
    global movHolDay, movHolMonth, movHolYear

    if y != movHolYear:
        calc_movable_holidays(y)

    # Fixed holidays (German)
    match m:
        case 1:
            if d == 1: return "New Year’s Day"
        case 5:
            if d == 1: return "Labor Day"
        case 10:
            if d == 3: return "German Unity Day"
            if d == 31: return "Reformation Day"
        case 12:
            if d == 25: return "Christmas Day"
            if d == 26: return "Boxing Day"

    # Movable holidays
    if m == movHolMonth[0] and d == movHolDay[0]: return "Good Friday"
    if m == movHolMonth[1] and d == movHolDay[1]: return "Easter Sunday"
    if m == movHolMonth[2] and d == movHolDay[2]: return "Easter Monday"
    if m == movHolMonth[3] and d == movHolDay[3]: return "Ascension Day"
    if m == movHolMonth[4] and d == movHolDay[4]: return "Whit Monday"

    return ""


# ---------------------------------------------
# Gauss algorithm – computes Easter Sunday
# ---------------------------------------------
def holiday_easter(year):
    dt_format = "%Y-%m-%d"
    a = b = c = k = p = q = M = d = N = e = 0
    easter = 0

    a = year % 19
    b = year % 4
    c = year % 7
    k = year // 100
    p = (8 * k + 13) // 25
    q = k // 4
    M = (15 + k - p - q) % 30
    d = (19 * a + M) % 30
    N = (4 + k - q) % 7
    e = (2 * b + 4 * c + 6 * d + N) % 7

    easter = 22 + d + e

    # Special cases
    if d == 29 and e == 6:
        easter = 50
    if d == 28 and e == 6 and a > 10:
        easter = 49

    date = datetime.strptime(f"{year}-03-01", dt_format)
    date = date + timedelta(days=easter - 1)
    return date.strftime(dt_format)


def holiday_good_friday(year):
    dt_format = "%Y-%m-%d"
    d = datetime.strptime(holiday_easter(year), dt_format)
    d = d + timedelta(days=-2)
    return d.strftime(dt_format)


def holiday_easter_monday(year):
    dt_format = "%Y-%m-%d"
    d = datetime.strptime(holiday_easter(year), dt_format)
    d = d + timedelta(days=1)
    return d.strftime(dt_format)


def holiday_ascension(year):
    dt_format = "%Y-%m-%d"
    d = datetime.strptime(holiday_easter(year), dt_format)
    d = d + timedelta(days=39)
    return d.strftime(dt_format)


def holiday_whit_monday(year):
    dt_format = "%Y-%m-%d"
    d = datetime.strptime(holiday_easter(year), dt_format)
    d = d + timedelta(days=50)
    return d.strftime(dt_format)


# ---------------------------------------------
# Prepare calendar arrays
# ---------------------------------------------
def prepare_calendar(from_year, to_year):
    global calYear, calMonth, calDay
    global calWeekday, calWeek, calHoliday
    global monthName, weekdayName

    calYear = []
    calMonth = []
    calDay = []
    calWeekday = []
    calWeek = []
    calHoliday = []

    monthName = []
    weekdayName = []

    for y in range(from_year, to_year + 1):
        calc_movable_holidays(y)

        for m in range(1, 13):
            for d in range(1, days_in_month(m, y) + 1):
                calYear.append(y)
                calMonth.append(m)
                calDay.append(d)

                obj = datetime(y, m, d)
                calWeekday.append(obj.weekday() + 1)  # Monday=1 ... Sunday=7
                calWeek.append(obj.isocalendar()[1])
                calHoliday.append(is_holiday(y, m, d))

    monthName.extend([
        "--", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])

    weekdayName.extend([
        "--", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ])


# ---------------------------------------------
# Runtime globals
# ---------------------------------------------
calYear = [0]
calMonth = [0]
calDay = [0]
calWeekday = [0]
calWeek = [0]
calHoliday = [""]

monthName = [""]
weekdayName = [""]

movHolDay = [0]
movHolMonth = [0]
movHolYear = 0


# ---------------------------------------------
# Test output
# ---------------------------------------------
print(holiday_whit_monday(2025))
print(holiday_good_friday(2025))
print(holiday_easter(2025))
print(days_in_month(2, 1964))

prepare_calendar(2006, 2035)

i = calYear.index(2025)
m = calMonth.index(12, i)
d = calDay.index(25, m)

print(weekdayName[calWeekday[d]])
print("Week:", str(calWeek[d]))
print(calHoliday[d])

