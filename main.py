import json
from datetime import datetime
from utils.global_utils.display_menu import display_menu

# TODO: work on view_transactions() to display a list of all saved transactions

transactions_path = "C:/Users/ffree/OneDrive/Documents/GitHub/Budget-App/transactions.json" 



try:
    with open(transactions_path, "x"):
        transactions = {}
        print("Save data not found. Creating new file...")
    
except FileExistsError:
    try:
        with open(transactions_path, "r") as file:
            transactions = json.load(file)
            print("Save data found.")
    except json.JSONDecodeError as e:
        print(f"No Data: {e}")
        transactions = {}


def main(): # CRUD operation names will go here as my own note

    while True:
        
        menu_options = ("Add Transaction", "Display Transaction History", "View Summary", "Edit Transaction", "Delete Transaction", "Exit")
        display_menu("Menu", menu_options)
        menu_choice = getValidInput("Enter a choice", True, False, 1, len(menu_options))
        match menu_choice:
            case 1:
                add_transaction()
            case 2:
                view_transactions()
            case 3:
                view_summary()
            case 4:
                edit_transaction()
            case 5:
                delete_transaction()
            case 6:
                with open(transactions_path, "w") as file:
                    json.dump(transactions, file, indent=4)
                break
            case _:
                print("Invalid selection.")

def add_transaction(): # Create
    # print("Adds Transaction.")
    new_key = int(len(transactions))
    date = get_date()
    category = input("Enter expense type: ") # Might make a category selection menu
    note = input("Enter a note: ")
    amount_spent = getValidInput("Enter the amount spent", True, True)

    info = {
        "note": note,
        "category": category,
        "date": date,
        "amount_spent": amount_spent
    }
    
    transactions.update({new_key: info})
    
    return info

def view_transactions(): # Read
    labels = ("Note", "Category", "Date", "Amount Spent")
    divider = "-"
    for i in labels:
        print(f"{i:^15}",end="")
    print(f"\n{divider*60}")
    for key in transactions:
        note = transactions[key]["note"]
        category = transactions[key]["category"]
        date = transactions[key]["date"]
        amount_spent = transactions[key]["amount_spent"]
        print(f"{note:^15}{category:^15}{date:^15}{amount_spent:^15}")

def view_summary(): # Read
    print("Displays summary")

def edit_transaction(): # Update
    print("Edits selected transaction")

def delete_transaction(): # Delete
    print("Deletes selected transaction")

def get_date():
    year = getValidInput("Enter a year", True, False, 1, 9999)
    month = getValidInput("Enter a month", True, False, 1, 12)
    months_with_31_days = (1, 3, 5, 6, 7, 10, 12)
    months_with_30_days = (4, 8, 9, 11)
    if month in months_with_31_days:
        day = getValidInput("Enter a day", True, False, 1, 31)
    elif month in months_with_30_days:
        day = getValidInput("Enter a day", True, False, 1, 30)
    else:
        if year % 4 == 0:
            day = getValidInput("Enter a day", True, False, 1, 29)
        else:
            day = getValidInput("Enter a day", True, False, 1, 28)
    if len(str(month)) == 1:
        if len(str(day)) == 1:
            return f"0{month}-0{day}-{year}"
        else:
            return f"0{month}-{day}-{year}"
    else:
        return f"{month}-{day}-{year}"
    

def getValidInput(prompt, is_number=False, is_float=False, min_number=None, max_number=None, length=None):
    while True:
        user_input = input(f"{prompt}: ")
        isValid = False

        if is_number:
            if user_input.isdigit():
                isValid = True
                user_input = int(user_input)

            elif is_float:
                try:
                    user_input = float(user_input)
                    isValid = True

                except:
                    print("Invalid input. Please enter a decimal number.")

            else:
                print("Invalid input. Please enter a number.")
                
            if min_number != None and max_number != None:
                if user_input in range(min_number, max_number+1):
                    isValid = True
                        
                else:
                    print(f"Invalid input. Please enter a number from {min_number} to {max_number}.")
                    isValid = False

            
        else:
            if length != None:
                if len(user_input) == length:
                    isValid = True
                else:
                    print(f"Invalid input. Input must be {length} characters long.")
        if isValid == True:
            break
        else:
            print("Please Try again.")

    return user_input

main()