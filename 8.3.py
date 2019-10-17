"""
Lesson:
Write a program that lets the user enter a string and displays the
letter that appears most frequently in the string. Ignore spaces,
punctuation, and uppercase vs lowercase.



Hints:

Create a list to hold letters based on the length of the user input
Convert all letters to the same case
Use a loop to check for each letter in the alphabet (create an alphabet
list and step through it) Have a variable to hold the largest number of
times a letter appears, and replace the value when a higher number is found
"""
# Defining our initial variables, and creating the alphabet list that the
# for loop will cycle through. The for loop determines if the char/character
# in the user_phrase matches up with any letters from the alphabet. If it does, it
# will count how many times that letter or letters occurred.


def main():
    count = 0
    frequent_letter = []
    current = 0
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    user_phrase = input("Please enter a phrase (it can be anything): ")
    for letter in alphabet:
        for char in user_phrase.upper():
            if letter == char:
                count += 1
        if count > current:
            current = count
            frequent_letter = letter
            count = 0
        elif count == current:
            frequent_letter += letter
            count = 0
        else:
            count = 0

    print("The most common letter(s) found in your phrase: ", frequent_letter)
    print("This letter was used " + str(current), "times.")


main()
