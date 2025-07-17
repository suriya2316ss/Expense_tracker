import csv
from datetime import datetime

# ------------------ 1. Add Expense ------------------
def add_expense():
    amount = input("Enter amount spent (e.g.150): ₹")
    category = input("Enter category (e.g. Food, Travel, etc.): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])
    print("✅ Expense added successfully!\n")

# ------------------ 2. View Expenses ------------------
def view_expenses():
    print("\n📄 All Recorded Expenses:")
    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"₹{row[0]} | {row[1]} | {row[2]}")
    except FileNotFoundError:
        print("❌ No expenses found yet.\n")

# ------------------ 3. Show Total ------------------
def show_total():
    total = 0
    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[0])
        print(f"\n💰 Total Spent: ₹{total}\n")
    except FileNotFoundError:
        print("❌ No expenses to calculate.\n")

# ------------------ 4. Main Menu ------------------
def main():
    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spent")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()  
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❗ Invalid option. Please try again.")

# ------------------ 5. Run App ------------------
main()
