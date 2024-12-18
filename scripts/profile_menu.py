from utils.display_menu import display_menu
from utils.get_valid_input import get_valid_input
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def profile_menu():
    while True:
        display_menu("Profile Menu", ("Create New Profile", "View Profile", "Edit Profile", "Back"))
        choice = get_valid_input("Enter a choice", True, False, 1, 4)
        match choice:
            case 1:
                print("Not Implemented")
            case 2:
               print("Not Implemented")
            case 3:
                print("Not Implememnted")
            case 4:
                break
            case 5:
                print("Invalid input")