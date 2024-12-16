import json
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir) # Adds parent folder to module import paths

from utils import display_menu, get_valid_input

data_dir = os.path.join(parent_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

transactions_path = os.path.join(data_dir, 'transactions.json') 

try:
    if not os.path.exists(transactions_path):
        with open(transactions_path, "w") as file:
            json.dump({}, file)
            transactions = {}
            print("Save data not found. Creating new save file...")
    else:
        with open(transactions_path, "r") as file:
            transactions = json.load(file)
            print("Save data found.")
except (json.JSONDecodeError, FileNotFoundError) as e:
    print(f"File Error: {e}. Creating new save file...")
    transactions = {}

# Menu Funcs 

def add_transaction(): # Create
    # print("Adds Transaction.")
    new_key = str(len(transactions))
    print()
    date = get_date()
    category = get_category() # Might make a category selection menu
    note = input("Enter a note: ")
    amount = get_valid_input("Enter the amount", True, True)
    print()
    info = {
        "note": note,
        "category": category,
        "date": date,
        "amount": amount
    }
    
    transactions.update({new_key: info})
    
    return info

def view_transactions(): # Read
    print()
    labels = ("Note", "Category", "Date", "Amount")
    divider = "-"
    for i in labels:
        print(f"{i:^15}",end="")
    print(f"\n{divider*60}")
    for key in transactions:
        note = transactions[key]["note"]
        category = transactions[key]["category"]
        date = transactions[key]["date"]
        amount = transactions[key]["amount"]
        print(f"{note:^15}{category:^15}{date:^15}{amount:^15}")
    print()

def view_summary(): # Read
    amount = 0
    for key in transactions:
        amount += transactions[key]["amount"]
    print(f"\nBalance: {amount:.2f}\n")

def edit_transaction(): # Update
    print()
    selected_transaction = get_transaction(transactions)
    info = selected_transaction["info"]
    print()
    display_menu("Edit Transaction", ("Edit Note", "Edit Category", "Edit Date", "Edit Amount"))
    edit_choice = get_valid_input("Choose an Option", True, False, 1, 4)
    print()
    match edit_choice:
        case 1:
            info["note"] = input("Enter a note: ")
        case 2:
            info["category"] = get_category() # Might make a category selection menu
        case 3:
            info["date"] = get_date()
        case 4:
            info["amount"] = get_valid_input("Enter the amount", True, True)
    print()

def delete_transaction(): # Delete
    print()
    selected_transaction = get_transaction(transactions)
    info = selected_transaction["info"]
    id_num = selected_transaction["id"]
    note = info["note"]
    print(f"You are about to delete '{note}'. Would you like to continue?")
    choice = input("(Y/N): ").lower()
    while True:
        match choice:
            case "y":
                transactions.pop(id_num)
                break
            case "n":
                break
            case _:
                print("Invalid input. Do you want to delete this item?")
                choice = input("(Y/N): ").lower
    renum_keys = {}
    i = 0
    for key, value in transactions.items():  # Fixed use of .items()
        new_key = str(i)  # Corrected typo
        renum_keys[new_key] = value
        i += 1
    transactions.clear()
    transactions.update(renum_keys)
    print("Transaction Deleted!\n")

# Input handling funcs

def get_transaction(transactions):
    i = 1
    for key in transactions:
        note = transactions[key]["note"]
        print(f"{i}. {note}")
        i += 1
    transaction_id = str(get_valid_input("Enter the number of the desired transaction", True, False, 1, len(transactions))-1)
    if transaction_id in transactions.keys():
        return {
            "info": transactions[transaction_id],
            "id": transaction_id
        }
    else:
        print(f"Transaction ID {transaction_id} doesn't exist.")

def get_date():
    year = get_valid_input("Enter a year", True, False, 1, 9999)
    month = get_valid_input("Enter a month", True, False, 1, 12)
    months_with_31_days = (1, 3, 5, 6, 7, 10, 12)
    months_with_30_days = (4, 8, 9, 11)
    if month in months_with_31_days:
        day = get_valid_input("Enter a day", True, False, 1, 31)
    elif month in months_with_30_days:
        day = get_valid_input("Enter a day", True, False, 1, 30)
    else:
        if year % 4 == 0:
            day = get_valid_input("Enter a day", True, False, 1, 29)
        else:
            day = get_valid_input("Enter a day", True, False, 1, 28)
    if len(str(month)) == 1:
        if len(str(day)) == 1:
            return f"0{month}-0{day}-{year}"
        else:
            return f"0{month}-{day}-{year}"
    else:
        return f"{month}-{day}-{year}"

def get_category():
    categories = ("Income", "Food", "Gas", "Recreation", "Gift", "Personal", "Misc")
    for i in categories:
        print(f"{categories.index(i)+1}. {i}")
    choice = get_valid_input("Select a category", True, False, 1, len(categories))
    return categories[choice - 1]

# Main func

def transaction_menu(): # CRUD operation names will go here as my own note
    while True:
        
        menu_options = ("Add Transaction", "Display Transaction History", "View Spending Summary", "Edit Transaction", "Delete Transaction", "Exit")
        display_menu("Menu", menu_options)
        menu_choice = get_valid_input("Enter a choice", True, False, 1, len(menu_options))
        match menu_choice:

            case 1:
                add_transaction()

            case 2:
                view_transactions()

            case 3:
                view_summary()

            case 4:
                if transactions != {}:
                    edit_transaction()
                else:
                    print("No transactions to edit.")

            case 5:
                if transactions != {}:
                    delete_transaction()
                else:
                    print("No transactions to delete.")

            case 6:
                with open(transactions_path, "w") as file:
                    json.dump(transactions, file, indent=4)
                break

            case _:
                print("Invalid selection.")