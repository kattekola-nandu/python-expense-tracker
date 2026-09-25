from expenses import (
    add_expense,
    view_expenses,
    total_expenses,
    largest_expense,
    average_expense,
    length_expenses,
    delete_expense,
    edit_expense,
    search_expense,
    search_by_date,
    search_by_date_range,
    expense_summary,
    show_expense_summary,
    expense_category_summary,
    show_expense_category_summary,
    monthly_expense_summary,
    category_expense_percentage,
    monthly_category_summary,
    compare_monthly_expenses
)

from budgets import (
    set_category_budget,
    view_category_budgets,
    check_budget_status,
    budget_summary
)

from storage import (
    load_expenses,
    load_budgets,
    save_expense
)

print("===== EXPENSE TRACKER =====")

expenses = load_expenses()
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