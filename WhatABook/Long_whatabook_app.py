import sys
import mysql.connector
from mysql.connector import errorcode

#Configuration
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "long_whatabook",
    "raise_on_warnings": True
}
#Main Menu
def show_menu():
    print("\n  -- Main Menu --")
    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      Please enter your numbered selection: '))

        return choice
    except ValueError:
        print("\n  Invalid number, program terminated...\n")
        sys.exit(0)

def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book_fields")
    books = cursor.fetchall()
#
    print("\n  -- DISPLAYING BOOK LISTING --")
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[1], book[2], book[3]))

def show_locations(cursor):
    cursor.execute("SELECT store_id, locale from store_fields")
    locations = cursor.fetchall()
#
    print("\n  -- DISPLAYING STORE LOCATIONS --")
    for location in locations:
        print("  Locale: {}\n".format(location[1]))

#validate the users ID
def validate_user():
    try:
        user_id = int(input('\n      Enter a customer id < 1, 2, or 3>: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number, program terminated...\n")
        sys.exit(0)

#Show users account menu
def show_account_menu():
    try:
        print("\n      -- Customer Menu --")
        #Insert welcome message to user here
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        Please enter your numbered selection: '))

        return account_option
    except ValueError:
        print("\n  Invalid number, terminating program...\n")
        sys.exit(0)

#Show books added to the users wishlist
def show_wishlist(cursor, _user_id):
    cursor.execute("SELECT user_fields.user_id, user_fields.first_name, user_fields.last_name, book_fields.book_id, book_fields.book_name, book_fields.author " + 
                    "FROM wishlist_fields " + 
                    "INNER JOIN user_fields ON wishlist_fields.user_id = user_fields.user_id " + 
                    "INNER JOIN book_fields ON wishlist_fields.book_id = book_fields.book_id " + 
                    "WHERE user_fields.user_id = {}".format(_user_id))
    
    wishlist = cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")
    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))
###
###
###Query is currently printing after selection
###Review below and remove exposed query
###
###
#Show books available to add to wishlist
def show_books_to_add(cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book_fields "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist_fields WHERE user_id = {})".format(_user_id))

    cursor.execute(query)
    books_to_add = cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")
    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))
def add_book_to_wishlist(cursor, _user_id, _book_id):
    cursor.execute("INSERT INTO wishlist_fields(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#try/catch block for handling potential MySQL database errors
try:
#Connect to database
    db = mysql.connector.connect(**config)  
    cursor = db.cursor()
#Main Menu
    print("\n  Welcome to the Long_WhatABook Application! ")
    user_selection = show_menu()

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user selects option 3, call the validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the ID of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # commit the changes to the database 
                    db.commit() 
###
###Update next line to return book name, not ID
###
                    print("\n        Added Book ID: {} to your wishlist.".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid entry, please try again...")

                # show the account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        # show the main menu
        user_selection = show_menu()

    print("\n\n  Program terminated...")

#Error handling
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Error: Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  Error: The database is not accessible")
    else:
        print(err)
finally:
    """ Terminating connection to MySQL """

    db.close()