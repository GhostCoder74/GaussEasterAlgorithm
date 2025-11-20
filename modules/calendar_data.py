# SPDX-License-Identifier: GPL-3.0-or-later

from datetime import datetime
from utils import days_in_month
from holidays import get_holiday

def build_calendar(start_year: int, end_year: int) -> list:
    """Return a full calendar list of dicts."""
    data = []

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            for day in range(1, days_in_month(month, year) + 1):
                date = datetime(year, month, day)
                entry = {
                    "year": year,
                    "month": month,
                    "day": day,
                    "weekday": date.weekday() + 1,
                    "week": date.isocalendar()[1],
                    "holiday": get_holiday(year, month, day)
                }
                data.append(entry)

    return data

