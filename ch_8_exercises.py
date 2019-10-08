"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
print("=" * 10, "Section 8.1 string operations", "=" * 10)
# 1) Print all the characters from the name variable by accessing one character at a time
name = "John Jacob Jingleheimer Schmidt"
for ch in name:
    print(ch)

# 2) Use the index value to access and print the capital s in Schmidt from the variable name
print(name[24])

# 3) Use a negative index value to print the letters from the last name "Schmidt" in name
print(name[-1], name[-2], name[-3], name[-4], name[-5], name[-6], name[-7])


# TODO 8.2 String slicing
print("=" * 10, "Section 8.2 string slicing", "=" * 10)
# 1) Use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""
# 2) Print middle
middle = name[5:10]
print(middle)


# TODO 8.3 Testing, Searching, and manipulating strings
print("=" * 10, "Section 8.3 manipulating strings", "=" * 10)
# 1) Test to see if the string "Jacob" is in name, print the result
if "Jacob" in name:
    print('The name "Jacob" was found.')
else:
    print('The name "Jacob" was not found.')

# 2) Test to see if the string "Michael" is in name, print the result
if "Michael" in name:
    print('The name "Michael" was found.')
else:
    print('The name "Michael" was not found.')

# 3) Test to see if name contains a number, print the result
if name.isdigit():
    print(name, 'contains only digits.')
else:
    print(name, 'contains characters, not digits.')
# 4) Test to see if number contains a number, print the result
number = "42"
if number.isdigit():
    print(number, 'is a number!')
else:
    print(number, 'is not a number.')

# 5) Search for "J" in name, replace with "j" (lower case), print the result
#    Note: You can assign this to a variable first, or just print
letter = 'J'
if letter == 'J':
    new_letter = name.replace('J', 'j')
    print(new_letter)

# 6) Split the string name into the variable name_list, replace the "", print the result
name_list = ""
