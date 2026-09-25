from validation import (
    validate_amount,
    validate_category
)

from storage import save_budget

from expenses import expense_category_summary

def set_category_budget(budgets):
    print("===== SET CATEGORY BUDGET =====")

    while True:
        category = input("Enter the category: ")
        category_result = validate_category(category)

        if category_result:
            break

    while True:
        try:
            budget = float(input("Enter the budget: "))
            budget_result = validate_amount(budget)

            if budget_result:
                break

        except ValueError:
            print("Please enter the valid budget amount")

    category_exists = category_result in budgets

    if category_exists:
        old_budget = budgets[category_result]

        print(
            f"A budget already exists for "
            f"{category_result}: ₹{old_budget:.2f}"
        )

        while True:
            change = input("Do you want to replace it? (Y/N): ")
            change = change.lower()

            if change == "n":
                return

            elif change == "y":
                break

            else:
                print("Please! enter Y/N")

    budgets[category_result] = budget_result

    save = save_budget(budgets)

    if save:
        print("Budget Save successful")

    else:
        print("Budget Save failed")

        if category_exists:
            budgets[category_result] = old_budget

        else:
            del budgets[category_result]

def view_category_budgets(budgets):
    if not budgets:
        print("No budgets set!")
    else:
        print("===== CATEGORY BUDGETS =====")

        for key, value in budgets.items():
            print(f"{key:<20} : ₹{value:.2f}")

def get_budget_status(spent, budget):
    if spent > budget:
        diff = spent - budget
        return ("Over", diff)

    elif spent < budget:
        diff = budget - spent
        return ("Remaining", diff)

    else:
        return ("exactly equal", 0)

def get_budget_warning(percentage_used):
    if percentage_used > 100:
        return "Warning: You have exceeded your budget!"

    elif percentage_used >= 80:
        return "Warning: You are close to your budget!"

    else:
        return "Status: Spending is under control."

def check_budget_status(expenses, budgets):
    if not budgets:
        print("No budgets set!")
        return

    if not expenses:
        print("No expenses found!")
        return

    print("===== BUDGET STATUS =====")

    category_total = expense_category_summary(expenses)

    for category, budget in budgets.items():
        spent = category_total.get(category, 0)
        percentage_used = spent / budget * 100

        if category not in category_total:
            print(f"No expenses recorded for {category}")

        print(f"Category    : {category}")
        print(f"Budget      : ₹{budget:.2f}")
        print(f"Spent       : ₹{spent:.2f}")
        print(f"Budget used : {percentage_used:.2f}%")

        status, diff = get_budget_status(spent, budget)

        if status == "Over":
            print(f"Over budget by : ₹{diff:.2f}")

        elif status == "Remaining":
            print(f"Remaining      : ₹{diff:.2f}")

        else:
            print("Spending is exactly equal to the budget")

        warning = get_budget_warning(percentage_used)

        print(f"{warning}")
        print("--------------------------------")

def budget_summary(expenses, budgets):
    if not budgets:
        print("No budgets set!")
        return

    if not expenses:
        print("No expenses found!")
        return

    category_total = expense_category_summary(expenses)

    print("===== BUDGET SUMMARY =====")

    for category, budget in budgets.items():
        spent = category_total.get(category, 0)

        if category not in category_total:
            print(f"No expenses recorded for {category}")

        percentage_used = spent / budget * 100

        print(f"Category     : {category}")
        print(f"Budget       : ₹{budget:.2f}")
        print(f"Spent        : ₹{spent:.2f}")

        budget_progress_bar(percentage_used)

        status, diff = get_budget_status(spent, budget)

        if status == "Over":
            print(f"Over budget  : ₹{diff:.2f}")

        elif status == "Remaining":
            print(f"Remaining    : ₹{diff:.2f}")

        else:
            print("Spending is exactly equal to the budget")

        warning = get_budget_warning(percentage_used)

        print(warning)
        print("--------------------------------")        

def budget_progress_bar(percentage_used):
    total_blocks = 20

    filled_blocks = percentage_used * total_blocks / 100
    filled_blocks = int(filled_blocks)

    # don't want a progress bar with a negative number of empty blocks
    filled_blocks = max(0, min(filled_blocks, total_blocks))

    empty_blocks = total_blocks - filled_blocks

    filled_characters = "█" * filled_blocks
    empty_characters = "░" * empty_blocks

    progress_bar = filled_characters + empty_characters

    print(f"Progress: {progress_bar}  {percentage_used:.2f}%")
