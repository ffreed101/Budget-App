# Budget-App
 **Track income, expenses, and your financial balance — while building key development skills.**

## Table of Contents
- [About](#about)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [Challenges & Lessons Learned](#challenges-and-lessons-learned)

## About
 A simple personal finance app focused on helping me learn key development concepts like CRUD, file handling, and input validation. This project will help me practice data persistence, file I/O, and error handling, while also building a strong foundation for larger applications.

## Features(Minimum Viable Product)
- Add transactions for income and expenses.
- View all transactions in a table format.
- View a summary of total income, expenses, and current balance.
- Edit or delete transactions.
- Data is stored in a **JSON** file for persistence.

## How It Works
1. The user is presented with a simple menu.
2. The user can select from the following options: 
   - **Add Transaction**: Enter category, description, and amount.
   - **View Transactions**: View a list of past transactions.
   - **View Summary**: See total income, expenses, and balance.
   - **Edit Transactions**: Modify existing transactions.
   - **Delete Transactions**: Delete existing transactions.
3. All data is saved to a file (`transactions.json`) so it persists between sessions.

## Installation
### Requirements
- Python
1. **Clone the repo**:
   ```bash
   git clone https://github.com/ffreed101/budget-app.git
   cd budget-app
   ```
2. Set the command line to the app directory and run the app:
   ```bash
   cd C:/../Budget-App
   python main.py
   ```

## How to contribute
Since this is a personal learning project, contributions aren’t required. However, advice is welcome! If you have suggestions for:

 - Code improvements
 - Tech that I could learn to use
 - File handling tips
 - Ideas for new features
 ... I’m happy to hear them!


## File Structure
 ```bash
 budget-app/ 
     ├── transactions.json # Where all transactions are stored. Created on first startup.
     ├── main.py # Main Python script 
     ├── README.md # This readme file
     ├── utils # Utility functions
         ├── display_menu.py # Utility function I use for basic CLI menus
 ```
## Technologies
- **Language**: Python 3
- **Libraries**: 'json'

## Challenges and Lessons Learned
 - **Using JSON for save data**
   - I've never made a system with persisting data and I feel like I've made a substantial jump in my understanding of working with and parsing file data from this.
 - **Modifying dictionary keys**
   - This one was a challenge, but I found the best way to go about it in my case was to iterate over the dictionary, create a list of new values, and clear the old dictionary so you can update the old one with the refactored data. My use case was because I wanted to use dictionaries instead of arrays to practice using them, so I have to renumber all my dictionary keys in the right order, from 0 and up.
 - **Version Control/Git**
   - I learned a lot from having someone else clone my repo and try to open the app. Finding those verison control problems and solving them to make life easier for others is really important.
 - **Project Structuring**
   - Handling paths for data files and importing scripts is making sense to me. I feel like I am getting a pretty good handle on the good practices involving project structure.