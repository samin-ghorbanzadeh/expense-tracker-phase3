import argparse
from untils import positive_amount, valid_date, non_empty_string
from expense import Expense
from expense_manager import save_expense, read_all_expenses
from viewer import apply_filters
from datetime import datetime
from report import (
    sum_by_category,
    total_expenses,
    days_span,
    daily_average,
    write_report,
)
from visualize import plot_category_bar, plot_daily_line

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command', help='Available commands')

# ---------- Add Subcommand ----------
add_parser = subparsers.add_parser('add', help='Add a new expense entry')
add_parser.add_argument(
    "--amount", type=positive_amount, required=True,
    help='Amount of expense; must be a positive number'
)
add_parser.add_argument(
    "--date", type=valid_date, required=True,
    help='Date of the expense in YYYY-MM-DD format'
)
add_parser.add_argument(
    "--category", type=non_empty_string, required=True,
    help='Category of the expense'
)
add_parser.add_argument(
    "--description", type=str, default="",
    help='Description about the expense'
)

# ---------- View Subcommand ----------
view_parser = subparsers.add_parser('view', help='View list of expenses with optional filters')
view_parser.add_argument(
    "--last", type=int, default=10,
    help="Show the last N expense records (default: 10)"
)
view_parser.add_argument(
    "--category", type=str,
    help="Filter expenses by category"
)
view_parser.add_argument(
    "--from", dest="from_date", type=valid_date,
    help='Filter expenses from this date (inclusive) - format: YYYY-MM-DD'
)
view_parser.add_argument(
    "--to", dest="to_date", type=valid_date,
    help='Filter expenses up to this date (inclusive) - format: YYYY-MM-DD'
)

# ---------- Summary Subcommand ----------
summary_parser = subparsers.add_parser('summary', help='Generate a summary report of expenses')

# ---------- Visualize Subcommand ----------
visualize_parser = subparsers.add_parser('visualize', help='Plot expense charts using matplotlib')

# ---------- Parse and Execute ----------
args = parser.parse_args()

if args.command == 'add':
    expense = Expense(args.amount, args.date, args.category, args.description)
    save_expense(expense, 'expenses.csv')
    print("✅ Expense saved successfully!")

elif args.command == 'view':
    result = sorted(
        apply_filters(args),
        key=lambda e: datetime.strptime(e.date, '%Y-%m-%d'),
        reverse=True
    )
    for e in result:
        print(e)

elif args.command == 'summary':
    expenses = read_all_expenses("expenses.csv")
    total = total_expenses(expenses)
    category_sums = sum_by_category(expenses)
    day_count = days_span(expenses)
    avg = daily_average(total, day_count)

    print("✅ Summary Report:")
    print(f"Total Expenses: {total:.2f}")
    print("By Category:")
    for cat, amt in category_sums.items():
        print(f"  {cat} : {amt:.2f}")
    print(f"Daily Average: {avg:.2f}")

    write_report(total, category_sums, avg)
    print("Report saved to report.csv")

elif args.command == 'visualize':
    expenses = read_all_expenses("expenses.csv")
    plot_daily_line(expenses)
    print('✅ The line chart was plotted')
    plot_category_bar(expenses)
    print('✅ The bar chart was plotted')

        










