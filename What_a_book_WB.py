import sys
import mysql.connector
from mysql.connector import errorcode
from simple_colors import * 
   

# Configuration for connection to the Database
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


# Define a method for the user interface Menu
# Interface Requirements are View Books, Store Locations, and My Account (Added option to exit the program)
# Test users input for a number.
# If user provides invalid input, exit the program!
def show_menu(): 
    print("\n \n**", blue('WhatABook Main Menu', 'underlined'), '**')
    print("\n 1. View Available Books\n 2. View Our Store Locations\n 3. Access My Account", red("\n 4. Exit The Program"))

    try:
        user_choice = int(input('\nChoose an option by typing the corresponding number: '))
        return user_choice
    except ValueError:
        print('\n', red('Invalid number, the program is being terminated...'),'\n')
        sys.exit(0)
  

# Define a method for available books
# Pass a select query to access the book table and fetch the book fields
# Access results from the cursor object 
# Loop over the fetched data set and display the results
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()
    print('\n',"**", blue('DISPLAYING BOOK LISTING', 'underlined'),"**",'\n')

    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))


# Define a method for store locations
# Pass a select query to access the store table and fetch locale field 
# Access results from the cursor object
# Loop over the data set displaying the results 
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()
    print("\n", "**", blue('DISPLAYING STORE LOCATIONS', 'underlined'), "**", "\n")

    for location in locations:
        print(green("Locale: {}\n".format(location[1])))


# Define a method for validating a user
# Validate users input for a number range of users in the database (3 users)
# Test users input for a number
# If user provides invalid input, exit the program!
def validate_user():
    try:
        user_id = int(input('\n''Please enter a valid customer id: '))
        if user_id < 0 or user_id > 3:
            print('\n',  red('Invalid customer id, the program is being terminated...'),'\n')
            sys.exit(0)
        return user_id

    except ValueError:
        print("\n  Invalid number, program terminated...\n")
        sys.exit(0)


# Define a method for a validated users account 
# Give options for accessing wishlist, adding a book, or returning to main menu
# Test user input for a number
# If user provides invalid input, exit the program!
def show_account_menu():
    try:
        print("\n","**",blue('Account Main Menu', 'underlined'),"**")
        print("\n"           "1. Access Wishlist   \n2. Add a Book   \n3. Return to Main Menu")
        account_info = int(input("\n""Choose an option by typing the corresponding number: "))
        return account_info

    except ValueError:
        print("\n  Invalid number, program terminated...\n")
        sys.exit(0)


# Define a method for a users wishlist 
# Inner join query for a list of records in both user and book tables
# Test user input for a number
# Loop over the data set displaying the results
def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()
    print('\n',"**", blue('Displaying Items On Your Wishlist', 'underlined'),"**",'\n')

    for book in wishlist:
        print(green("Book Name: {}\nAuthor: {}\n".format(book[4], book[5])))


# Define a method for a users choice of book/books to add
# Query the database for a list of books not in the users wishlist
# Fetch the results from the query 
# Access results from the cursor object
# Loop over the data set displaying the results
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details " 
            "FROM book " 
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    _cursor.execute(query)
    books_to_add = _cursor.fetchall()
    print('\n',"**", blue('Displaying Available Books', 'underlined'),"**",'\n')

    for book in books_to_add:
        print(green("Book ID: {}\nBook Title: {}\n".format(book[0], book[1])))


# Define a method for a user to add a book to their wishlist
# Insert the the book into the users wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


# Connect to the WhatABook database 
# Define cursor variable for MySQL queries
# Display the main menu 
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor() 
    print("\n", blue("Welcome to the WhatABook Application!"))
    user_selection = show_menu() 


    # While loop for main menu choices 1-4
    # Option 1, calls the show_books method and display the books
    # Option 2, calls the show_locations method and display the configured locations
    # Option 3, calls the validate_user method to validate the entered user_id, call the show_account_menu() to show the account settings menu
    while user_selection != 4:
        if user_selection == 1:
            show_books(cursor)
        if user_selection == 2:
            show_locations(cursor)
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()


            # While account option does not equal 3
            # Option 1 calls the show_wishlist() method to show the current users
            # Option 2, calls the show_books_to_add function to show the user books not currently configured in the users wishlist
            # Gather the users entered book_id number
            # Add the selected book the users wishlist
            # Add the selected book the users wishlist
            # Commit to the database 
            while account_option != 3:
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)
                    book_id = int(input("\nEnter the id of the book you want to add: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    db.commit() 
                    print(green("\nBook id: {} was added to your wishlist!".format(book_id)))


                # If the selected option is less than 0 or greater than 3, display an invalid user selection 
                # Show the account menu
                # Display the account menu
                if account_option < 0 or account_option > 3:
                    print(red("\nInvalid option, please retry..."))
                account_option = show_account_menu()


        # If the user selection is less than 0 or greater than 4, display an invalid user selection
        # Display the main menu
        if user_selection < 0 or user_selection > 4:
            print(red("\nInvalid option, please retry..."))
        user_selection = show_menu()
    print("\n\n  Program terminated...")


# Connection error handler
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)


#Close connection 
finally:
    db.close()