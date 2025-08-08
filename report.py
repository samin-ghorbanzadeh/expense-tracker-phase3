from collections import defaultdict
from datetime import datetime
import csv
import pandas as pd

def total_expenses(expenses):
    return sum(e.amount for e in expenses)

def sum_by_category(expenses):
    result = defaultdict(float)
    for e in expenses:
        result[e.category] += e.amount
    return result

def days_span(expenses):
    if not expenses:
        return 0
    dates = [datetime.strptime(e.date, '%Y-%m-%d') for e in expenses]
    return (max(dates) - min(dates)).days + 1

def daily_average(total, day_count):
    if day_count > 0:
        return total / day_count
    return 0

def write_report(total, category_sums, daily_avg):
    with open('report.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Type", "Label", "Value"])
        writer.writeheader()

        writer.writerow({"Type": "Total", "Label": "", "Value": f"{total:.2f}"})
        for cat, amt in category_sums.items():
            writer.writerow({"Type": "Category", "Label": cat, "Value": f"{amt:.2f}"})
        writer.writerow({"Type": "Average", "Label": "", "Value": f"{daily_avg:.2f}"})
def write_excel_report():
    df = pd.read_csv('report.csv')
    df.to_excel('report.xlsx', index=False, engine='openpyxl')
    