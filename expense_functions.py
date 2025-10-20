import json
import os
import time

# تابع لود فایل json
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    else:
        return []
    
# تابع دخیره در فایل json
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)

# تابع ورود مبلغ
def add_expense():
    print("\n ====== Add new Expense =====")
    name = input("Enter expense name : ")
    amount = float(input("Enter amount : "))
    category = input("Enter category (e.g., food, transport, etc.): ")
    
    expense = {
        'name' : name,
        'amount' : amount,
        'category' : category
    }

    expenses.append(expense)
    save_expenses()
    print(f"\n ✅ Expense {name} added successfully!!")
    time.sleep(1)

# تابع نمایش هزینه ها
def view_expense():
    print("==== All Expense ====")
    if not expenses:
        print("no expense recorder yet!")
        time.sleep(1)
    else:
        for i, exp in enumerate(expenses,start=1):
            print(f"{i}. name : {exp['name']} --->  ${exp['amount']:.2f} in {exp['category']}")
            
    input("\nPress Enter to return to menu...")
    
# تابع حذف هزینه
def delete_expense():
    print("\n=== Delete Expense ===")
    if not expenses:
        print("No expenses to delete.")
        time.sleep(1)
        return

    # نمایش لیست هزینه‌ها
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} - ${exp['amount']:.2f} ({exp['category']})")

    try:
        index = int(input("\nEnter the number of the expense to delete: "))
        if 1 <= index <= len(expenses):
            deleted = expenses.pop(index - 1)
            save_expenses()
            print(f"✅ Deleted: {deleted['name']} - ${deleted['amount']}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

    time.sleep(1)

# تابع جمع هزینه ها

def view_total_expense():
    print("==== View total Expense ====")
    if not expenses:
        print("No expense recorder yet..!")
    else:
        total = sum(exp["amount"] for exp in expenses)
        print(f"your total expenses : ${total:.2f}")
    
    time.sleep(1)
    

expenses = load_expenses()
