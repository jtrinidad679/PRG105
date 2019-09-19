"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import random
import math


# TODO 5.2 - calling an existing function
print("=" * 10, "Section 5.2 call an existing function", "=" * 10)


# Beneath the following function, write the code to call it
# Remove the """ """ before testing
# Note: Python requires two blank lines before a function definition


def hello():
    print("Hello Sweetie!")


# Write the code to call the hello function on the next line
hello()

# TODO 5.2 - creating and calling a function
print("=" * 10, "Section 5.2 create and call an existing function", "=" * 10)


# Write a function called joke that prints a joke on the screen
# Call the function


def joke():
    print("Why didn't the undead cross the road?")
    print("He didn't have the guts.")


joke()

# TODO 5.3 designing a program in functions
print("=" * 10, "Section 5.3 design a program using functions", "=" * 10)


# Create a main function that will call separate functions that
# print each line in a knock knock joke. Make sure to call main
# as the last line of your code.


def main():
    #  Displaying our first line of the knock knock joke
    first_line()
    #  Displaying our second line of the knock knock joke
    second_line()
    #  Displaying our third line of the knock knock joke
    third_line()
    #  Displaying our fourth line of the knock knock joke
    fourth_line()
    #  Displaying our fifth and final line of the knock knock joke
    fifth_line()


#  Creating the definitions for our variables
def first_line():
    print("Knock Knock")


def second_line():
    print("Who's there?")


def third_line():
    print("Spell")


def fourth_line():
    print("Spell who?")


def fifth_line():
    print("W-H-O")


main()

# TODO 5.4 local variables
print("=" * 10, "Section 5.4 using local variables", "=" * 10)


# 1) Write a program with a main2 function. In main2, define a variable
#    called name and assign a name to it, then print hello
#    and the name variable. Have main2 call a second function get_name().
# 2) In the get_name function, ask the user for their name,
#    then greet them using a print statement.
# 3) Call the main2 function.
# Note - you would not normally have more than one main function
# in a program, we are just adding the number after main to allow
# us to write multiple short practice programs in a single file.


def main2():
    name()
    get_name()


def name():
    name_one = "Jasmine"
    print("Hello", name_one)


def get_name():
    name_two = input("Enter your name: ")
    print("Hello", name_two)


main2()

# TODO 5.5 passing arguments to Functions
print("=" * 10, "Section 5.5 passing arguments", "=" * 10)


# Complete the code below to pass the my_number variable value from
# main3() into square() using a parameter name of value.
# Remove the """ """ before testing


def main3():
    my_number = 7
    square(my_number)


def square(value):
    squared_value = value * value
    print(squared_value)


main3()

# TODO 5.5 passing multiple arguments
print("=" * 10, "Section 5.5 passing multiple arguments", "=" * 10)


# Complete the code below to pass the variables from main into
# parameters for add. Look at the code to determine the correct
# variable / parameter names. Remove the """ """


def main4():
    num_one = 5
    num_two = 7
    add(num_one, num_two)


def add(num1, num2):
    total = num1 + num2
    print(total)


main4()

# TODO 5.7 value returning functions
print("=" * 10, "Section 5.7 value returning functions", "=" * 10)
# import random - Add a statement importing the random library at the top of this file
# Add a global constant PI with a value of 3.14 before the main5 function definition
PI = 3.14


def main5():
    r = random.randint(1, 10)
    r2 = r * r
    area(r2)


def area(radius_squared):
    my_area = PI * radius_squared
    print(format(my_area, ",.2f"))


main5()

# TODO 5.8 value returning functions
print("=" * 10, "Section 5.8 value returning functions", "=" * 10)
# Complete the following program, remove the """  """ before testing


def main6():
    print("This program will calculate your BMI")
    height = float(input("What is your height in inches? "))
    weight = float(input("What is your weight in pounds? "))

    #  I'm assigning height and weight to the bmi function
    #  and assigning patient_bmi to whatever bmi equals
    patient_bmi = bmi(height, weight)

    #  Printing bmi result
    print("Your BMI is: " + format(patient_bmi, '.1f'))


def bmi(height_inches, weight_pounds):
    #  the answer here will return up to patient_bmi and be
    #  displayed in the final print function in main6
    answer = (weight_pounds / (height_inches * height_inches)) * 703
    return answer


main6()

# TODO 5.9 the math module
print("=" * 10, "Section 5.9 use the math module", "=" * 10)
# import math - Add the import math statement at the top of this file
# Write a statement that uses the ceil function on the following variable
# Display the result
number_to_round = 4.243
result = math.ceil(number_to_round)
print(result)
