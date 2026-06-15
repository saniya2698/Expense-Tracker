# Expense Tracker using TXT File

F = "Expense1.txt"


def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    with open(F, "a") as file:
        file.write(f"{date},{category},{amount}\n")

    print("Expense Added Successfully!\n")


def view_expenses():
    try:
        with open(F, "r") as file:
            data = file.readlines()

            if not data:
                print("No expenses found.\n")
                return

            print("\n------ Expense Records ------")
            for line in data:
                date, category, amount = line.strip().split(",")
                print(f"Date: {date} | Category: {category} | Amount: ₹{amount}")

    except FileNotFoundError:
        print("No expense file found.\n")


def total_expenses():
    total = 0

    try:
        with open(F, "r") as file:
            for line in file:
                date, category, amount = line.strip().split(",")
                total += float(amount)

        print(f"\nTotal Expenses: ₹{total}\n")

    except FileNotFoundError:
        print("No expense file found.\n")


def category_summary():
    summary = {}

    try:
        with open(F, "r") as file:
            for line in file:
                date, category, amount = line.strip().split(",")
                amount = float(amount)

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

        print("\n------ Category Summary ------")
        for category, total in summary.items():
            print(f"{category}: ₹{total}")

    except FileNotFoundError:
        print("No expense file found.\n")


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")