from datetime import datetime 

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
