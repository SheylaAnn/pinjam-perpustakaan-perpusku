# pinjam-perpustakaan-perpusku
PERPUSKU is a Command Line Interface (CLI)-based library application built with Python. It simulates a simple book lending system for users and book management features for admins.

## Key Features (CRUD)
- **Create:** Add new books to the library
- **Read:** View book list & search by title, genre, author, etc
- **Update:** Add or reduce stock, Loan and return books
- **Delete:** Delete books to the recycle bin and permanently


## Additional Features
Role-based access: `admin` and `user`
**Admin**
- Add, delete, and edit book data
- Manage book stock
- Access to all book loan logbook
- Access to the recycle bin feature
**User**
- View and search for books
- Loan and return books
- Personal Loan Logbook
  
## Flowchart
The image below illustrates the flowchart of the program.
![Flowchart](FLOW1.svg)
![Flowchart](FLOW2.svg)

## How to run the program
1. Make sure Python is installed (version 3.9.6).
2. Run in the terminal / command prompt:
python main.py
3. Follow the instructions on the screen.

## Data Login
{
  'admin': {'password': '1', 'role': 'admin'},
  'usertest': {'password': 'user123', 'role': 'user'}
}

## Additional Modules
pip install tabulate

## Note:
- Data is stored only while the program is running (non-persistent).
- This project can be developed by adding a feature to check late book returns.

Author
------
Sheyla Annisyah
