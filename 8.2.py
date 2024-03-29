"""
Lesson:
Many companies use telephone numbers like 555-GET-FOOD so the number is
easier for their customers to remember. On a standard telephone the alphabetic
letters are mapped to numbers in the following fashion:

A, B, C = 2

D, E, F = 3

G, H, I = 4

J, K, L = 5

M, N, O = 6

P, Q, R, S = 7

T,U, V, = 8

W, X, Y, Z = 9

Write a program that asks the user to enter a 10-character telephone number in the
format XXX-XXX-XXXX. The application should display the telephone number with any
alphabetic characters that appeared in the original translated to their numeric equivalent.
"""
# I used the supplied alpha and digits variables for this exercise. Created the variable
# phone_number to hold the users input. Then created an empty variable, converted_number, to
# eventually store the phone_number's matched alpha to numerical values. The for loops then
# determine for each letter in phone_number whether they are alpha, and for the alpha items,
# finds their index and converts them to numbers which are then concatenated with converted_number.


def main():
    alpha = ['0', '1', '2', 'A', 'B', 'C', '3', 'D', 'E', 'F', '4', 'G', 'H', 'I', '5', 'J', 'K', 'L', '6', 'M', 'N',
             'O', '7', 'P', 'Q', 'R', 'S', '8', 'T', 'U', 'V', '9', 'W', 'X', 'Y', 'Z', '-']

    digits = ['0', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5',
              '6', '6', '6', '6', '7', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '9', '-']
    phone_number = input("Please enter the phone number that you would like to convert to numbers: ")

    converted_number = ""
    for letter in phone_number:
        for item in range(0, len(alpha)):
            if letter.upper() == alpha[item]:
                converted_number += (digits[item] + "")
    print(converted_number, "is the converted number!")


main()
