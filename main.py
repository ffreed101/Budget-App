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
    new_key = str(len(transactions))
    print()
    date = get_date()
    category = input("Enter expense type: ") # Might make a category selection menu
    note = input("Enter a note: ")
    amount_spent = get_valid_input("Enter the amount spent", True, True)
    print()
    info = {
        "note": note,
        "category": category,
        "date": date,
        "amount_spent": amount_spent
    }
    
    transactions.update({new_key: info})
    
    return info

def view_transactions(): # Read
    print()
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
    print()

def view_summary(): # Read
    amount_spent = 0
    for key in transactions:
        amount_spent += transactions[key]["amount_spent"]
    print(f"\nTotal spent: {amount_spent:.2f}\n")

def edit_transaction(): # Update
    print()
    selected_transaction_id = get_transaction_id(transactions)
    selected_transaction = get_transaction(selected_transaction_id)
    print()
    display_menu("Edit Transaction", ("Edit Note", "Edit Category", "Edit Date", "Edit Amount Spent"))
    edit_choice = get_valid_input("Choose an Option", True, False, 1, 4)
    print()
    match edit_choice:
        case 1:
            selected_transaction["note"] = input("Enter a note: ")
        case 2:
            selected_transaction["category"] = input("Enter expense type: ") # Might make a category selection menu
        case 3:
            selected_transaction["date"] = get_date()
        case 4:
            selected_transaction["amount_spent"] = get_valid_input("Enter the amount spent", True, True)
    print()


def delete_transaction(): # Delete
    print()
    selected_transaction_id = get_transaction_id(transactions)
    selected_transaction = get_transaction(selected_transaction_id)
    note = selected_transaction["note"]
    print(f"You are about to delete '{note}'. Would you like to continue?")
    choice = input("(Y/N): ").lower()
    while True:
        match choice:
            case "y":
                transactions.pop(selected_transaction_id)
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

def get_transaction(transaction_id):
    return transactions[transaction_id]

def get_transaction_id(transactions):
    i = 1
    for key in transactions:
        note = transactions[key]["note"]
        print(f"{i}. {note}")
        i += 1
    transaction_id = str(get_valid_input("Enter the number of the desired transaction", True, False, 1, len(transactions))-1)
    if transaction_id in transactions.keys():
        return transaction_id
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
    

def get_valid_input(prompt, is_number=False, is_float=False, min_number=None, max_number=None, length=None):
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
                    print("Invalid input. Enter a decimal number.")

            else:
                print("Invalid input. Enter a number.")
                
            if min_number != None and max_number != None:
                if user_input in range(min_number, max_number+1):
                    isValid = True
                        
                else:
                    if isValid == True:
                        print(f"Invalid input. Enter a number from {min_number} to {max_number}.")
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