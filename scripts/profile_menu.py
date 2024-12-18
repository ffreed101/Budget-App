from utils.display_menu import display_menu
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def profile_menu():
    while True:
        display_menu("Profile Menu", ("Create New Profile", "View Profile", "Edit Profile", "Back"))