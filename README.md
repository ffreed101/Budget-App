# Budget-App

## Table of Contents
- [About](#about)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [Challenges & Lessons Learned](#challenges--lessons-learned)

## About
 A simple personal finance app focused on helping me learn key development concepts like CRUD, file handling, and input validation. This project will help me practice data persistence, file I/O, and error handling, while also building a strong foundation for larger applications.

## Features(MVP)
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
   - **Edit or Delete**: Modify or delete existing transactions.
3. All data is saved to a file (`transactions.json`) so it persists between sessions.

## 🔧 Installation
1. **Clone the repo**:
   ```bash
   git clone https://github.com/ffreed101/budget-app.git
   cd budget-app
2. Run the app:
   ```bash
   python main.py
   
## File Structure
 ```bash
 budget-app/ 
     ├── transactions.json # Where all transactions are stored 
     ├── main.py # Main Python script 
     ├── README.md # This readme file

