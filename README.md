# 💰 Expense Tracker

A Python-based console application for managing personal expenses, including adding, viewing, editing, deleting, searching, analyzing expenses, and tracking category budgets.

## 📌 Project Description

Expense Tracker is a Python console application designed to help users manage and analyze their daily expenses.

The application allows users to:

- Add and store expenses
- View, edit, and delete expenses
- Search expenses by category and date
- Calculate total, average, and largest expenses
- Generate category and monthly expense summaries
- Compare expenses between different months
- Set category-based budgets
- Check budget usage and status
- Store expenses and budgets using CSV files

The project is organized into separate Python modules to keep the code clean, reusable, and easy to maintain.

## ✨ Features

### 💸 Expense Management

- Add new expenses
- View all expenses
- Edit existing expenses
- Delete expenses
- Search expenses by category
- Search expenses by date
- Search expenses within a date range

### 📊 Expense Analysis

- Calculate total expenses
- Calculate average expenses
- Find the largest expense
- Count the number of expenses
- Generate overall expense summaries
- Generate category-wise expense summaries
- Generate monthly expense summaries
- Calculate category-wise expense percentages
- Generate monthly category summaries
- Compare expenses between two months

### 💰 Budget Management

- Set category-based budgets
- View category budgets
- Check budget status
- Display budget warnings
- Generate budget summaries
- Display budget progress

### 💾 Data Storage

- Save expenses to CSV files
- Load expenses automatically when the application starts
- Save category budgets to CSV files
- Load category budgets automatically

## 📁 Project Structure

```text
expense_tracker/
│
├── main.py
├── expenses.py
├── budgets.py
├── validation.py
├── storage.py
│
├── expenses.csv
├── budget.csv
└── Expense_Tracker.py
```


### File Description

| File | Purpose |
|------|---------|
| `main.py` | Runs the application and handles the menu |
| `expenses.py` | Contains expense-related functions |
| `budgets.py` | Contains budget management functions |
| `validation.py` | Handles input validation |
| `storage.py` | Handles CSV data storage |
| `expenses.csv` | Stores expense data |
| `budget.csv` | Stores category budget data |
| `Expense_Tracker.py` | Original working backup |


## 🛠️ Technologies Used

- Python 3
- CSV
- Built-in Python modules
- Modular programming
- Functions
- Lists and dictionaries
- Exception handling
- Input validation
- File handling


## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the project folder

```bash
cd expense_tracker
```

### 3. Run the application

```bash
python main.py
```

### 4. Use the menu

After running the application, the menu will be displayed. Select the required option by entering its corresponding number.


## 💾 Data Storage

The Expense Tracker uses CSV files to store data locally.

### Expense Data

Expenses are stored in:

```text
expenses.csv
```

The file contains information such as:

- Expense amount
- Expense category
- Expense date

### Budget Data

Category budgets are stored in:

```text
budget.csv
```

The application automatically loads the saved data when it starts and updates the CSV files when expenses or budgets are modified.

No external database is required.


## 📋 Menu Options

When the application starts, the following menu is available:

| Option | Feature |
|--------|---------|
| 1 | Add Expense |
| 2 | View Expenses |
| 3 | Total Expenses |
| 4 | Largest Expense |
| 5 | Average Expense |
| 6 | Number of Expenses |
| 7 | Delete Expense |
| 8 | Edit Expense |
| 9 | Search Category |
| 10 | Expense Summary |
| 11 | Search by Date |
| 12 | Search by Date Range |
| 13 | Expense Category Summary |
| 14 | Monthly Expenses Summary |
| 15 | Category Expenses by Percentage |
| 16 | Monthly Category Summary |
| 17 | Compare Monthly Expenses |
| 18 | Set Category Budget |
| 19 | View Category Budget |
| 20 | Check Budget Status |
| 21 | Budget Summary |
| 22 | Exit |


## 💻 Example Usage

### Adding an Expense

```text
===== ADD EXPENSE =====
Enter expense amount: 250
Enter expense category: Food
Enter the date (YYYY-MM-DD): 2026-09-22
Expense added successfully!
```

### Viewing Expenses

```text
===== EXPENSES =====
No. Category             Amount      Date
--------------------------------------------
1    Food                250.00      2026-09-22
2    Travel              500.00      2026-09-21
--------------------------------------------
```

### Budget Status

```text
===== BUDGET STATUS =====
Category             Budget        Spent        Status
Food                 ₹3000.00      ₹250.00      Remaining
```

## 🚀 Future Improvements

The project can be further improved with:

- Web-based user interface
- Flask backend
- SQLite or SQL database
- Interactive charts and dashboards
- User authentication
- Expense export and reporting
- Mobile-friendly interface
- Advanced financial analytics


## 👨‍💻 Author

**Nandu**

B.Tech CSE Student | Python Developer | Web Development Enthusiast

This project was built as part of my journey to learn Python through practical, project-based development.


## 📄 License

This project is created for educational and personal learning purposes.