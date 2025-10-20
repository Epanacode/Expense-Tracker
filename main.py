import time
from expense_functions import load_expenses, save_expenses, add_expense, view_expense, delete_expense, view_total_expense







# تابع main -----------------------------



def main_menu():
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. View total expenses")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
           add_expense()

        elif choice == "2":
           view_expense()
           
        elif choice == "3":
            delete_expense()
            

        elif choice == "4":
            view_total_expense()
            
        elif choice == "5":
            print("\n👋 Exiting... Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")
            time.sleep(1)


if __name__ == "__main__":
    main_menu()
    
    
    
# test commit