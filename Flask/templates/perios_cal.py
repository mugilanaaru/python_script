from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_period(start_date_str, end_date_str):
    """
    Calculate the difference between two dates.
    Returns both days and a human-readable string.
    """
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    # Total days difference
    days = (end_date - start_date).days

    # Human-readable difference
    diff = relativedelta(end_date, start_date)
    readable = f"{diff.years} years, {diff.months} months, {diff.days} days"

    return days, readable