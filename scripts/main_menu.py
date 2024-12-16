# import sys
# import os

# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.append(parent_dir) # Adds parent folder to module import paths

# from utils import get_valid_input, display_menu
from utils.get_valid_input import get_valid_input
from utils.display_menu import display_menu

def main_menu():
    # View Data
    # Transactions
    # Profile
    # Exit
    display_menu("Main Menu", ("View Data", "Transactions", "Profiles", "Exit"))
    menu_choice = get_valid_input("Enter a choice", True, False, 1, 4)


