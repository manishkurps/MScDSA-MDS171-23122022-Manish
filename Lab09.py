# TASK Lab 09
# Expense Tracker

# Define a class called ExpenseTracker to manage expenses and income.
class ExpenseTracker:

    def _init_(self):
        # Initialize the transactions dictionary with empty lists for expenses and income.
        self.transactions = {
            "expenses": [],
            "income": []
        }

    # Method to store a transaction in the particular category.
    def storeTransaction(self, type, category, cost, description, date):
        transaction = {
            "category": category,
            "cost": cost,
            "description": description,
            "date": date
        }

        if type == "expense":
            self.transactions["expenses"].append(transaction)
        else:
            self.transactions["income"].append(transaction)

    # Method to view all transactions, both income and expenses.
    def viewTransaction(self):
        print("INCOME")
        for income in self.transactions["income"]:
            print(income)

        print("EXPENSES")
        for expense in self.transactions['expenses']:
            print(expense)

    # Method to calculate and display the total income and total expense.
    def totalIncomeExpense(self):
        print("Total Income")
        total_income = sum(income["cost"] for income in self.transactions["income"])
        print(total_income)

        print("Total Expense")
        total_expense = sum(expense["cost"] for expense in self.transactions["expenses"])
        print(total_expense)

    # Method to load transactions from a CSV file and populate the ExpenseTracker.
    def transaction(self, transaction):
        self.transactions = {
            "expenses": [],
            "income": []
        }
        with open("transaction.csv", 'r') as file:
            for read in file:
                parts = read.strip().split(',')
                transaction_type, category, cost, description, date = parts
                self.storeTransaction(transaction_type, category, cost, description, date)

# Create an object for the expenseTracker class.
myTransactions = ExpenseTracker()

# Load transactions from a CSV file "PythonLab09.csv" when the program starts.
myTransactions.transaction("transaction")

# Options will be provided to the users using this while loop
while True:
    print("\nMenu:")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Transactions")
    print("4. View total Inome and Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        cost = int(input("Enter cost: "))
        description = input("Enter description: ")
        date = input("Enter date: ")
        myTransactions.storeTransaction("expense", category, cost, description, date)
        print("Transaction added successfully to CSV file")

    elif choice == "2":
        category = input("Enter category: ")
        cost = int(input("Enter cost: "))
        description = input("Enter description: ")
        date = input("Enter date: ")
        myTransactions.storeTransaction("income", category, cost, description, date)
        print("Transaction added successfully to CSV file")

    elif choice == "3":
        myTransactions.viewTransaction()
    elif choice == "4":
        myTransactions.totalIncomeExpense()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice. Please try again.")