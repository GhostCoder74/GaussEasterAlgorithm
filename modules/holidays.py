# SPDX-License-Identifier: GPL-3.0-or-later

from datetime import datetime
from easter import (
    good_friday, easter_sunday, easter_monday,
    ascension_day, pentecost_monday
)
from utils import mid, right

_cached_year = None
_mov_days = []
_mov_months = []

def load_movable_holidays(year: int):
    """Calculate movable holidays for a given year."""
    global _cached_year, _mov_days, _mov_months

    if year == _cached_year:
        return

    _cached_year = year
    _mov_days = []
    _mov_months = []

    holiday_funcs = [
        good_friday,
        easter_sunday,
        easter_monday,
        ascension_day,
        pentecost_monday,
    ]

    for func in holiday_funcs:
        date_str = func(year)
        _mov_months.append(int(mid(date_str, 5, 2)))
        _mov_days.append(int(right(date_str, 2)))


def get_holiday(year: int, month: int, day: int) -> str:
    """Return the holiday name or empty string."""
    load_movable_holidays(year)

    # Fixed holidays
    if month == 1 and day == 1:
        return "New Year's Day"
    if month == 5 and day == 1:
        return "Labor Day"
    if month == 10:
        if day == 3: return "German Unity Day"
        if day == 31: return "Reformation Day"
    if month == 12:
        if day == 25: return "Christmas Day"
        if day == 26: return "Second Christmas Day"

    # Movable holidays
    names = ["Good Friday", "Easter Sunday", "Easter Monday",
             "Ascension Day", "Pentecost Monday"]

    for i in range(5):
        if month == _mov_months[i] and day == _mov_days[i]:
            return names[i]

    return ""

