import matplotlib.pyplot as plt 
from expense_manager import read_all_expenses
from report import sum_by_category
from report import days_span
from collections import defaultdict
from datetime import datetime, timedelta
import os

def get_category_sums(expenses):
    category = []
    amount = []    
    sum_category = sum_by_category(expenses)
    for i, j in sum_category.items():
        category.append(i)
        amount.append(j)
    return category, amount

def daily_total_amount(expenses):
    daily_totals = defaultdict(float)
    for expense in expenses:
        daily_totals[expense.date] += expense.amount
    date_amount = tuple(sorted(daily_totals.items()))
    
    count_days = days_span(expenses)
    start_date = datetime.strptime(date_amount[0][0], '%Y-%m-%d')  
    
    date_list = []
    for i in range(count_days):
        day = start_date + timedelta(days=i)
        date_str = day.strftime('%Y-%m-%d')
        date_list.append(date_str)
    date_tuple = tuple(date_list)
    
    zero = []
    for i in range(count_days):
        zero.append(0)
    zero_tuple = tuple(zero)
    
    early_time_tuples = tuple(zip(date_tuple, zero_tuple))
    d1 = dict(early_time_tuples)
    d2 = dict(date_amount)

    result_dict = {}
    for date, amount in d1.items():
        result_dict[date] = amount
    for date, amount in d2.items():
        if date in result_dict:
            result_dict[date] += amount
        else:
            result_dict[date] = amount
    return result_dict

def plot_category_bar(expenses):
    category, amount = get_category_sums(expenses)
    plt.bar(category, amount)
    plt.title("Amount Spent by Category")
    plt.xlabel("category")
    plt.ylabel("total payment")
    os.makedirs('data/reports', exist_ok=True)
    plt.savefig('data/reports/category_spending_bar.png')
    plt.show()
    plt.close()

def plot_daily_line(expenses):
    daily_amount = daily_total_amount(expenses)
    date = list(daily_amount.keys())
    amount = list(daily_amount.values())
    
    converted_dates = []
    for d in date:
        converted_dates.append(datetime.strptime(d, '%Y-%m-%d'))
    
    date_amount_pairs = list(zip(converted_dates, amount))
    date_amount_pairs.sort()
    
    sorted_date = []
    sorted_amount = []
    for d, a in date_amount_pairs:
        sorted_date.append(d)
        sorted_amount.append(a)
    
    final_dates = []
    for d in sorted_date:
        final_dates.append(d.strftime('%Y-%m-%d'))
    
    plt.plot(final_dates, sorted_amount, '-o')
    plt.title("Daily Spending Overview")
    plt.xlabel("date")
    plt.xticks(rotation=45)
    plt.ylabel("expense") 
    plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    os.makedirs('data/reports', exist_ok=True)
    plt.savefig('data/reports/daily_expense_line.png')
    plt.show()
    plt.close()





















