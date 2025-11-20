# SPDX-License-Identifier: GPL-3.0-or-later

from datetime import datetime, timedelta

def left(s: str, amount: int) -> str:
    return s[:amount]

def right(s: str, amount: int) -> str:
    return s[-amount:]

def mid(s: str, offset: int, amount: int) -> str:
    if amount == -1:
        if offset >= len(s):
            return ""
        return s[offset:]
    return s[offset:offset + amount]


def days_in_month(month: int, year: int) -> int:
    """Return number of days in a month, including leap day."""
    if month == 2:
        temp = datetime(year, 3, 1) - timedelta(days=1)
        return temp.day
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    raise ValueError("Invalid month")

