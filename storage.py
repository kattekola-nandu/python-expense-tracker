import csv
from validation import (
    validate_amount,
    validate_category,
    validate_date
)

def save_expense(expense):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            expense["amount"],
            expense["category"],
            expense["date"]
        ])

def load_expenses():
    loaded_expenses = []

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for data in reader:
                if len(data) < 3:
                    continue

                try:
                    data[0] = float(data[0])

                except ValueError:
                    print(f"Skipping invalid expense: {data}")
                    continue

                valid_amount = validate_amount(data[0])

                if not valid_amount:
                    continue

                valid_category = validate_category(data[1])

                if not valid_category:
                    continue

                valid_date = validate_date(data[2])

                if not valid_date:
                    continue

                expense = {
                    "amount": valid_amount,
                    "category": valid_category,
                    "date": valid_date
                }

                loaded_expenses.append(expense)

    except FileNotFoundError:
        print("No expense file found. Starting with an empty list.")

    return loaded_expenses

def save_all_expenses(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for exp in expenses:
            writer.writerow([
                exp["amount"],
                exp["category"],
                exp["date"]
            ])

def save_budget(budgets):
    try:
        with open("budget.csv", "w", newline="") as file:
            writer = csv.writer(file)

            for category, budget in budgets.items():
                writer.writerow([category, budget])

        return True

    except OSError:
        print("Unable to save budgets!")
        return False

def load_budgets():
    loaded_budgets = {}

    try:
        with open("budget.csv", "r") as file:
            reader = csv.reader(file)

            for data in reader:
                if len(data) != 2:
                    continue

                try:
                    category = data[0]
                    category = validate_category(category)

                    if not category:
                        continue

                    budget_amount = float(data[1])
                    budget_amount = validate_amount(budget_amount)

                    if not budget_amount:
                        continue

                except ValueError:
                    print(f"Skipping invalid budget: {data}")
                    continue

                if category in loaded_budgets:
                    print(
                        f"Skipping duplicate budget: "
                        f"[{category}, {budget_amount}]"
                    )
                    continue

                loaded_budgets[category] = budget_amount

    except FileNotFoundError:
        print(
            "No budget file found. "
            "Starting with an empty dictionary."
        )

    return loaded_budgets
