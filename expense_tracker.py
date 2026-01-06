import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create CSV file if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "amount", "category", "description"])


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("✅ Expense added successfully!")


def view_expenses():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
def category_summary():
    category_totals = {}
    total_expense = 0

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["amount"])
            category = row["category"]

            total_expense += amount

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    print("\n📊 Expense Summary")
    print(f"Total Expenses: ₹{total_expense}")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount}")


def highest_spending_category():
    category_totals = {}

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["amount"])
            category = row["category"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    if not category_totals:
        print("No expenses recorded yet!")
        return

    # Find category with max expense
    max_category = max(category_totals, key=category_totals.get)
    max_amount = category_totals[max_category]

    print(f"\n💰 Highest Spending Category: {max_category} (₹{max_amount})")
import matplotlib.pyplot as plt

def monthly_summary():
    month_year = input("Enter month and year (MM-YYYY): ")
    category_totals = {}
    total_expense = 0

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            date = row["date"]  # format: YYYY-MM-DD
            month = date[5:7]
            year = date[0:4]
            if f"{month}-{year}" == month_year:
                amount = float(row["amount"])
                category = row["category"]

                total_expense += amount
                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

    if total_expense == 0:
        print(f"No expenses found for {month_year}")
        return

    print(f"\n📅 Expenses for {month_year}")
    print(f"Total Expenses: ₹{total_expense}")
    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount}")

    # ---- Bar Chart ----
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure(figsize=(8,5))
    plt.bar(categories, amounts, color='skyblue')
    plt.title(f'Expenses for {month_year}')
    plt.xlabel('Category')
    plt.ylabel('Amount (₹)')
    plt.show()



def show_menu():
    print("\nSmart Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Highest Spending Category")
    print("5. Monthly Summary")
    print("6. Exit")



while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_summary()
    elif choice == "4":
        highest_spending_category()
    elif choice == "5":
        monthly_summary()
    elif choice == "6":
        print("Goodbye 👋")
        break
    else:
        print("❌ Invalid choice, try again")
