import csv
from datetime import datetime

print("===== EXPENSE TRACKER =====")

def validate_category(category):
    category = category.strip()

    if not category:
        print("Category cannot be empty!")
        return False
    else:
        valid = category.replace(" ", "")

        if not valid.isalpha():
            print("Category should contain only letters!")
            return False
        else:
            return category.title()

def validate_amount(amount):
    if amount <= 0:
        print("Please enter a valid amount!")
        return False
    else:
        return amount

def validate_expense_number(number, expenses):
    try:
        number = int(number)

    except ValueError:
        print("Please enter a valid number!")
        return False

    if number >= 1 and number <= len(expenses):
        return number
    else:
        print("Please enter a number between 1 and", len(expenses))
        return False

def validate_date(date_input):
    try:
        date = datetime.strptime(date_input, "%Y-%m-%d")
        return date_input

    except ValueError:
        print("Please! enter the valid date")
        return False
    
def validate_month(month):
    try:
        m = datetime.strptime(month, "%Y-%m")
        return month

    except ValueError:
        print("Please! enter the valid month")
        return False
    
def add_expense():
    print("===== ADD EXPENSE =====")

    while True:
        try:
            amount = float(input("Enter expense amount: "))
            amount_result = validate_amount(amount)

            if amount_result:
                break

        except ValueError:
            print("Please enter a valid amount!")

    while True:
        category = input("Enter expense category: ")
        category_result = validate_category(category)

        if category_result:
            break

    while True:
        date_input = input("Enter the date (YYYY-MM-DD): ")
        result_date = validate_date(date_input)

        if result_date:
            break

    expense = {
        "amount": amount_result,
        "category": category_result,
        "date": result_date
    }

    return expense
    
def view_expenses(expenses):
    if not expenses:
        print("No expenses found!")

    else:
        print("===== EXPENSES =====")
        print(f"{'No.':<5}{'Category':<20}{'Amount':<12}{'Date'}")
        print("--------------------------------------------")

        s_no = 1

        for exp in expenses:
            print(
                f"{s_no:<5}"
                f"{exp['category']:<20}"
                f"{exp['amount']:<12.2f}"
                f"{exp['date']}"
            )
            s_no += 1

        print("--------------------------------------------")

def total_expenses(expenses):
    if not expenses:
        return 0

    else:
        total_amount = 0

        for exp in expenses:
            total_amount += exp["amount"]

        return total_amount

def largest_expense(expenses):
    if not expenses:
        return 0, []

    else:
        large = 0

        for exp in expenses:
            large = max(exp["amount"], large)

        categories = []

        for exp in expenses:
            if exp["amount"] == large:
                categories.append(exp["category"])

        return large, categories

def average_expense(expenses):
    if not expenses:
        return 0

    else:
        total = total_expenses(expenses)
        size_of_expenses = len(expenses)
        average = total / size_of_expenses
        return average

def length_expenses(expenses):
    if not expenses:
        return 0
    else:
        return len(expenses)

def save_expense(expense):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            expense["amount"],
            expense["category"],
            expense["date"]
        ])

def delete_expense(expenses):
    if not expenses:
        print("No expenses found!")

    else:
        print("===== DELETE EXPENSE =====")
        view_expenses(expenses)

        while True:
            delete_no = input("Enter the number you want to delete: ")
            result = validate_expense_number(delete_no, expenses)

            if result:
                d = result - 1
                expenses.pop(d)
                save_all_expenses(expenses)

                return True

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

def edit_expense(expenses):
    if not expenses:
        print("No expenses found!")

    else:
        print("===== EDIT EXPENSE =====")
        view_expenses(expenses)

        while True:
            edit = input("Enter the number you want to edit: ")
            result = validate_expense_number(edit, expenses)

            if result:
                edit = result - 1
                selected = expenses[edit]

                while True:
                    edit_choice = input(
                        "What do you want to edit?\n"
                        "1. Amount\n"
                        "2. Category\n"
                        "3. Date\n"
                        ": "
                    )

                    if edit_choice == "1" or edit_choice == "2" or edit_choice == "3":
                        break
                    else:
                        print("Invalid choice!")

                if edit_choice == "1":
                    try:
                        edit_as = float(input("Enter the edit amount: "))
                        result = validate_amount(edit_as)

                        if result:
                            selected["amount"] = result
                            save_all_expenses(expenses)
                            return True

                    except ValueError:
                        print("Please enter the valid number")

                elif edit_choice == "2":
                    edit_as = input("Enter the edit category: ")
                    result = validate_category(edit_as)

                    if result:
                        selected["category"] = result
                        save_all_expenses(expenses)
                        return True

                elif edit_choice == "3":
                    while True:
                        edit_as = input("Enter the edit date: ")
                        result_date = validate_date(edit_as)

                        if result_date:
                            break

                    selected["date"] = result_date
                    save_all_expenses(expenses)
                    return True

                return
            
def search_expense(expenses):
    if not expenses:
        print("No expenses found!")

    else:
        print("===== SEARCH CATEGORY =====")

        search = input("Enter category to search: ")
        search = search.strip()

        if not search:
            print("Please enter the item you wanna search")

        else:
            search = search.lower()
            found = False

            print(f"{'No.':<5}{'Category':<20}{'Amount':<12}{'Date'}")
            print("--------------------------------------------")

            s_no = 1

            for exp in expenses:
                formatted_date = datetime.strptime(
                    exp["date"], "%Y-%m-%d"
                ).strftime("%Y-%m-%d")

                if search in exp["category"].lower():
                    print(
                        f"{s_no:<5}"
                        f"{exp['category']:<20}"
                        f"{exp['amount']:<12.2f}"
                        f"{formatted_date}"
                    )
                    s_no += 1
                    found = True

            if found == True:
                print("--------------------------------------------")

            if not found:
                print("No expenses found in this category")

def search_by_date(expenses):
    if not expenses:
        print("No expenses found!")

    else:
        print("===== SEARCH BY DATE =====")

        search_date = input(
            "Enter the date in (YYYY-MM-DD) format for search: "
        )

        result_date = validate_date(search_date)

        if not result_date:
            return

        found = False

        print(f"{'No.':<5}{'Category':<20}{'Amount':<12}{'Date'}")
        print("--------------------------------------------")

        s_no = 1

        for expense in expenses:
            formatted_date = datetime.strptime(
                expense["date"], "%Y-%m-%d"
            ).strftime("%Y-%m-%d")

            if search_date == expense["date"]:
                print(
                    f"{s_no:<5}"
                    f"{expense['category']:<20}"
                    f"{expense['amount']:<12.2f}"
                    f"{formatted_date}"
                )
                s_no += 1
                found = True

        if found:
            print("--------------------------------------------")

        if not found:
            print("The expenses are not found on this date!")

def search_by_date_range(expenses):
    if not expenses:
        print("No expenses found!")

    else:
        print("===== SEARCH BY DATE RANGE =====")

        start = input("Enter the starting date for search: ")
        result_start = validate_date(start)

        if not result_start:
            return

        result_start = datetime.strptime(
            result_start, "%Y-%m-%d"
        )

        end = input("Enter the ending date for search: ")
        result_end = validate_date(end)

        if not result_end:
            return

        result_end = datetime.strptime(
            result_end, "%Y-%m-%d"
        )

        if result_end < result_start:
            print("Please! enter the valid starting and ending dates")

        else:
            found = False

            print(f"{'No.':<5}{'Category':<20}{'Amount':<12}{'Date'}")
            print("--------------------------------------------")

            s_no = 1

            for expense in expenses:
                date = datetime.strptime(
                    expense["date"], "%Y-%m-%d"
                )

                if result_start <= date <= result_end:
                    print(
                        f"{s_no:<5}"
                        f"{expense['category']:<20}"
                        f"{expense['amount']:<12.2f}"
                        f"{expense['date']}"
                    )
                    s_no += 1
                    found = True

            if found:
                print("--------------------------------------------")

            if not found:
                print("The expenses are not found on this date!")

def expense_summary(expenses):
    if not expenses:
        return False

    else:
        count = length_expenses(expenses)
        total = total_expenses(expenses)
        average = average_expense(expenses)
        largest, categories = largest_expense(expenses)

        return count, total, average, largest, categories
        
def show_expense_summary(expenses):
    summary = expense_summary(expenses)

    if summary:
        print("===== EXPENSE SUMMARY =====")

        count, total, average, largest, categories = summary

        print(f"Number of expenses : {count}")
        print(f"Total expenses     : ₹{total:.2f}")
        print(f"Average expense    : ₹{average:.2f}")
        print(f"Largest expense    : ₹{largest:.2f}")
        print("Largest categories :")

        for category in categories:
            print(f"- {category}")

        print("============================")

        return True

    else:
        print("No expenses found!")
        return False

def expense_category_summary(expenses):
    category_total = {}

    if not expenses:
        return category_total

    else:
        for expense in expenses:
            category = expense["category"]

            if category in category_total:
                category_total[category] = (
                    expense["amount"] + category_total[category]
                )

            else:
                category_total[category] = expense["amount"]

        return category_total

def show_expense_category_summary(category_total):
    print("===== CATEGORY SUMMARY =====")
    print(f"{'Category':<20}{'Total':>12}")
    print("--------------------------------")

    for key, value in category_total.items():
        print(f"{key:<20}₹{value:>10.2f}")

    print("--------------------------------")
    
def monthly_expense_summary(expenses):
    if not expenses:
        print("No expenses found!")
    else:
        print("===== MONTHLY EXPENSE SUMMARY =====")

        month = input("Enter the month in YYYY-MM format: ")
        result_month = validate_month(month)

        if not result_month:
            return

        result_month = datetime.strptime(result_month, "%Y-%m")

        found = False
        monthly_total = 0
        count = 0

        for expense in expenses:
            date = datetime.strptime(expense["date"], "%Y-%m-%d")

            if result_month.year == date.year and result_month.month == date.month:
                monthly_total += expense["amount"]
                count += 1
                found = True

        if not found:
            print("No expenses are found in this month")
        else:
            monthly_average = monthly_total / count

            print("===== MONTHLY EXPENSE SUMMARY =====")
            print(f"Total monthly expenses   : ₹{monthly_total:.2f}")
            print(f"Number of expenses       : {count}")
            print(f"Average monthly expenses : ₹{monthly_average:.2f}")
            print("====================================")

def category_expense_percentage(expenses):
    if not expenses:
        print("No expenses found!")

    else:
        print("===== CATEGORY EXPENSE PERCENTAGE =====")
        print(f"{'Category':<20}{'Amount':>12}{'Percentage':>15}")
        print("-----------------------------------------------")

        summary = expense_category_summary(expenses)
        total = total_expenses(expenses)

        for key, value in summary.items():
            percentage = value / total * 100

            print(
                f"{key:<20}"
                f"₹{value:>10.2f}"
                f"{percentage:>14.2f}%"
            )

        print("-----------------------------------------------")

def monthly_category_summary(expenses):
    if not expenses:
        print("No expenses found!")

    else:
        print("===== MONTHLY CATEGORY SUMMARY =====")

        month = input("Enter the month in YYYY-MM format: ")
        result_month = validate_month(month)

        if not result_month:
            return

        result_month = datetime.strptime(
            result_month, "%Y-%m"
        )

        monthly_expenses = []
        found = False

        for expense in expenses:
            date = datetime.strptime(
                expense["date"], "%Y-%m-%d"
            )

            if (
                result_month.year == date.year
                and result_month.month == date.month
            ):
                monthly_expenses.append(expense)
                found = True

        if not found:
            print("No expenses are found in this month")
            return

        category_total = expense_category_summary(monthly_expenses)

        print(f"{'Category':<20}{'Amount':>12}")
        print("--------------------------------")

        for key, value in category_total.items():
            print(f"{key:<20}₹{value:>10.2f}")

        print("--------------------------------")

def compare_monthly_expenses(expenses):
    if not expenses:
        print("No expenses found!")

    else:
        print("===== MONTHLY COMPARISON =====")

        month1 = input("Enter the first month in YYYY-MM format: ")
        m1 = validate_month(month1)

        if not m1:
            return

        m1 = datetime.strptime(m1, "%Y-%m")

        month2 = input("Enter the second month in YYYY-MM format: ")
        m2 = validate_month(month2)

        if not m2:
            return

        m2 = datetime.strptime(m2, "%Y-%m")

        if m1 == m2:
            print("Please enter two different months!")
            return

        total1 = 0
        total2 = 0

        found1 = False
        found2 = False

        for expense in expenses:
            date = datetime.strptime(
                expense["date"], "%Y-%m-%d"
            )

            if date.year == m1.year and date.month == m1.month:
                total1 += expense["amount"]
                found1 = True

            if date.year == m2.year and date.month == m2.month:
                total2 += expense["amount"]
                found2 = True

        if not found1 and not found2:
            print("No expenses found for either month!")
            return

        print(f"{month1} total: ₹{total1:.2f}")
        print(f"{month2} total: ₹{total2:.2f}")

        if not found1:
            print(f"No expenses found in {month1}")

        if not found2:
            print(f"No expenses found in {month2}")

        difference = abs(total1 - total2)
        print(f"Difference: ₹{difference:.2f}")

        if total1 > total2:
            print(f"{month1} has higher spending.")

        elif total2 > total1:
            print(f"{month2} has higher spending.")

        else:
            print("Both months have equal spending.")

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

expenses=load_expenses()

budgets = load_budgets()

def menu():
    print("======== MENU ========")
    print("1.Add Expenses")
    print("2.View Expenses")
    print("3.Total Expenses")
    print("4.Largest Expense")
    print("5.Average Expense")
    print("6.Number of Expenses")
    print("7.Delete Expense")
    print("8.Edit Expense")
    print("9.Search Category")
    print("10.Expense Summary")
    print("11.Search by Date")
    print("12.Search by Date Range")
    print("13.Expense Category Summary")
    print("14.Monthly Expenses Summary")
    print("15.Category Expenses by Percentage")
    print("16.Monthly Category Summary")
    print("17.Compare Monthly Expenses")
    print("18.Set Category Budget")
    print("19.View Category Budget")
    print("20.Check Budget Status")
    print("21.Budget Summary")
    print("22.Exit")

    choice = input("Enter your choice: ")
    return choice

def handle_choice(choice, expenses, budgets):

    if choice == "1":
        add = add_expense()
        expenses.append(add)
        save_expense(add)
        print("Expense added successfully!")

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        total = total_expenses(expenses)

        print("===== TOTAL EXPENSES =====")
        print(f"Total expense: ₹{total:.2f}")
        print("==========================")

    elif choice == "4":
        largest, categories = largest_expense(expenses)

        print("===== LARGEST EXPENSE =====")
        print(f"Amount    : ₹{largest:.2f}")
        print("Categories :")

        for i in categories:
            print(f"- {i}")

        print("===========================")

    elif choice == "5":
        avg = average_expense(expenses)

        print("===== AVERAGE EXPENSE =====")
        print(f"Average expenses: ₹{avg:.2f}")
        print("===========================")

    elif choice == "6":
        count = length_expenses(expenses)

        print("===== NUMBER OF EXPENSES =====")
        print(f"Number of expenses: {count}")
        print("==============================")

    elif choice == "7":
        deleted = delete_expense(expenses)

        if deleted:
            print("Expense deleted successfully!")

    elif choice == "8":
        result = edit_expense(expenses)

        if result:
            print("Updated successfully!")

    elif choice == "9":
        search_expense(expenses)

    elif choice == "10":
        result = show_expense_summary(expenses)

        if not result:
            print("No expenses found!")

    elif choice == "11":
        search_by_date(expenses)

    elif choice == "12":
        search_by_date_range(expenses)

    elif choice == "13":
        print("===== EXPENSE CATEGORY SUMMARY =====")
        category_total = expense_category_summary(expenses)
        show_expense_category_summary(category_total)

    elif choice == "14":
        monthly_expense_summary(expenses)

    elif choice == "15":
        category_expense_percentage(expenses)

    elif choice == "16":
        monthly_category_summary(expenses)

    elif choice == "17":
        compare_monthly_expenses(expenses)

    elif choice == "18":
        set_category_budget(budgets)

    elif choice == "19":
        view_category_budgets(budgets)

    elif choice == "20":
        check_budget_status(expenses, budgets)

    elif choice == "21":
        budget_summary(expenses, budgets)

    elif choice == "22":
        return False

    else:
        print("Invalid choice")

    return True

while True:
    choice = menu()

    result = handle_choice(choice, expenses, budgets)

    if not result:
        print("Thank you for using Expense Tracker!")
        break