from datetime import datetime

from validation import (
    validate_amount,
    validate_category,
    validate_expense_number,
    validate_date,
    validate_month
)

from storage import (
    save_expense,
    save_all_expenses
)

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
