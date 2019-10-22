"""
Lesson:
Write a program that keeps names and email addresses in a dictionary as key-value pairs.
The program should display a menu that lets the user look up a person's email address,
add a new name and email address, change an existing email address, and delete an existing
name and email address. The program should pickle the dictionary and save it to a file when
 the user exits the program. Each time the program starts, it should retrieve the dictionary
 from the file and unpickle it.
"""
import pickle
# Global constants for the menu the users will utilize to lookup, add, delete, change, etc.
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Main tries to open the file and load the customers data inside. If the file is not found,
# an error will display telling the user to add a customer which will then create the file.


def main():
    try:
        input_file = open('customers_file.dat', 'rb')
        customers_data = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        print("Sorry, the file you're looking for could not be found. "
              "Please add a customer and then quit to create the file.")
        customers_data = {}

    choice = 0
# Choice determines which number the users pick which will in turn
# display the proper function for that number.
    while choice != QUIT:
        choice = menu()

        if choice == LOOKUP:
            lookup(customers_data)
        elif choice == ADD:
            add(customers_data)
        elif choice == CHANGE:
            change(customers_data)
        elif choice == DELETE:
            delete(customers_data)
        elif choice == QUIT:
            save(customers_data)

# The menu function simply displays the title of the program, the numbers that will
# lookup, add, change, or delete customers, and then asks the user what they would like to do.
# If the user enters a number that isn't between 1 and 5, it will display an error message and
# ask them to reenter the correct number.


def menu():
    print("Customer Phone Lookup")
    print("-" * 18)
    print("1: Lookup a customer.")
    print("2: Add a new customer.")
    print("3: Change an existing phone number.")
    print("4: Delete an existing customer.")
    print("5: Quit the program\n")
    # Get choice from the user.
    choice = int(input("Enter the number you would like to proceed with: "))
    while choice < 1 or choice > 5:
        choice = int(input("Please enter a valid number: "))
    return choice

# The lookup function asks the user for their name and determines if that name is in
# the records and if it isn't then it will tell them that their name could not be found.


def lookup(customers_data):
    name = input("Please enter the customer name: ")
    print(customers_data.get(name, 'That name could not be found.'))

# The add function asks the user to add a name and phone number to the records. It will then see
# that the name is new and will add it to the customers_data dictionary I created in the main
# function. If the name and phone number entered already exist, it will display the error message.


def add(customers_data):
    name = input("Enter the name you would like to add: ")
    phone = input("Enter the phone number you want associated with that name: ")
    if name not in customers_data:
        customers_data[name] = phone
    else:
        print("That name and phone number already exist in our records.")

# The change function asks the user to enter the name that already exists in the records. If that
# name does exist, it will ask them to enter a new phone they want associated with that name. Then,
# it will add that phone number to the customers_data dictionary along with the name.


def change(customers_data):
    name = input("Enter the customer name: ")
    if name in customers_data:
        phone = input("Enter the new phone number you want associated with that name: ")
        customers_data[name] = phone
    else:
        print("That customer could not be found.")

# The delete function asks the user to enter their name.
# If that name exists in the dictionary, it will delete it.


def delete(customers_data):
    name = input("Enter the name you would like to delete: ")
    if name in customers_data:
        del customers_data[name]
    else:
        print("That customer could not be found.")

# The save function tells the user that the data file has been updated with their changes.


def save(customers_data):
    print("The data file has been updated with your changes.")
    save_file = open('customers_file.dat', 'wb')
    pickle.dump(customers_data, save_file)
    save_file.close()


main()
