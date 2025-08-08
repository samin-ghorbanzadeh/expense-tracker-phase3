import argparse
from datetime import datetime

def positive_amount(value):
    try:
        fvalue = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid float")
    if fvalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not positive")
    return fvalue

def valid_date(date_str):
    try:
        # برمی‌گردونیم رشته‌ی تاریخ به فرمت استاندارد (YYYY-MM-DD)
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        return dt.strftime('%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError(f"{date_str} is not a valid date")

def non_empty_string(value):
    if not value.strip():
        raise argparse.ArgumentTypeError("This field cannot be empty")
    return value




















