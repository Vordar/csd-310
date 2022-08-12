##Ryan Long | CYBR410-T301 | 8/12/2022
##This Python app should connect to long_whatabook DB
##This app should provide an interface to view Books, Store, and Account information
##Incorrect inputs should error and request another attempt, or terminate the program
##
##Referenced Code-
##Professor Krasso (Jul 27, 2020). buwebdev/csd-310/module_12 [Python Source Code]
##

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
#Print list of available books
    print("\n  -- DISPLAYING BOOK LISTING --")
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[1], book[2], book[3]))

def show_locations(cursor):
    cursor.execute("SELECT store_id, locale, time_open, time_close from store_fields")
    locations = cursor.fetchall()
#Print store locations and hours
    print("\n  -- DISPLAYING STORE LOCATIONS --")
    for location in locations:
        print("  Locale: {}\n  Open:  {}\n  Close: {}\n".format(location[1], location[2], location[3]))

#Validate the users ID
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
###
###Future Update, Insert welcome message to user here
###
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

        #Option 1, call show_books and display books
        if user_selection == 1:
            show_books(cursor)

        #Option 2, call show_locations and display locations data
        if user_selection == 2:
            show_locations(cursor)

        #Option 3, call validate_user method to validate the entered user_id 
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                #Option 1, call the show_wishlist() method to show the current users 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                #Option 2, call the show_books_to_add function to show the user 
                if account_option == 2:

                    #Show books currently not in users wishlist
                    show_books_to_add(cursor, my_user_id)

                    #get the entered book_id 
                    book_id = int(input("\n        Enter the ID of the book you want to add: "))
                    
                    #Add selection to users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    #Commit changes 
                    db.commit() 
###
###Future Update, next line to return book name not ID
###
                    print("\n        Added Book ID: {} to your wishlist.".format(book_id))

                #Display "Invalid Option" if user selection is less than 0 or greater than 3 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid entry, please retry...")

                #Account menu 
                account_option = show_account_menu()
        
        #Display "Invalid Option" if user selection is less than 0 or greater than 4
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid entry, please retry...")
            
        #Main menu
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