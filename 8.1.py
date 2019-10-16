"""
Lesson Objective(s):
Split a string into a list on spaces
Split specific letters from a string
Convert a string to upper case


Lesson:
Write a program that gets a string from the user containing a person's
first, middle, and last names and then displays their first, middle, and
last initials.  (Creating a new variable and concatenating each letter plus
a '.' is the easiest way to do this.)
"""
# We define everything in main. We get the users name in the variable user_name
# then transfer their split name into the name_list variable. Create an empty list
# named initials to store the initials in. The for loop goes through what is accepted
# and what isn't, and that provides the correct print statements.


def main():
    user_name = input("Please enter your name in the format First Middle Last: ")
    name_list = user_name.split()

    initials = []

    for name in name_list:
        name = (name[0].upper() + ". ")
        initials.append(name)
    try:
        print(initials[0][0] + '.', initials[1][0] + '.', initials[2][0] + '.')
    except IndexError:
        print(initials[0][0] + '.', initials[1][0] + '.')


main()
