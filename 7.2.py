"""
Lesson Objective(s):
Pass and return lists
use for loops for processing lists
Lesson:
Have a function that creates a list of 20 random integers between 1 and 100
(Assign them dynamically, store the list in a variable.)
Have a function get a number from the user that is between 1 and 100 (validate to ensure a
number between 1 and 100 was entered instead of text or something out of range using a try
and except statement). Pass both the list and the user's number to a function and have it
display all numbers in the list that is greater than the user's number. If there are not any,
display a message that explains there are no numbers in the list greater than the entered number.
"""
import random

# Creating an empty list to then append the random integers generated into.
# Then calling the display_num function.


def main():
    numbers_list = []
    for i in range(20):
        numbers_list.append(random.randint(1, 100))
    display_num(numbers_list, user_num_input())


# This function uses try and except statements to determine whether or not the
# user has input a valid integer. If not, then it prints the ValueError.


def user_num_input():
    user_num = int(input("Please enter a whole number between 0 and 100: "))
    while True:
        try:
            user_num = int(user_num)
            if 0 < user_num <= 100:
                return user_num
        except ValueError:
            print("Sorry, you did not enter a number between 0 and 100.")


def display_num(num_list, user_int):
    found = False
    for num in num_list:
        if num >= user_int:
            print(num)
            found = True
        if not found:
            print("There are no numbers greater than yours.")


""" 
This is where I'm having issues. This function (display_num) takes the values from the
numbers list and determines if they are greater than the number the user input. If the 
user number is greater than all numbers, then it should print one: "There are no numbers 
greater than yours." For some reason, it's printing it for each number. It's probably an 
easy fix, but I've been trying to fix it for AT LEAST 10 minutes and I'm stumped. (It's been longer)

Example:
Please enter a whole number between 0 and 100: 100
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.
There are no numbers greater than yours.

Process finished with exit code 0
"""


main()
