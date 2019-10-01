"""
Lesson:
Use the numbers.txt file for this assignment.

Write a program that uses the numbers.txt file,
which contains a series of integers. Your program
 will calculate the average of all of the numbers
 stored in the file and display the total on the
 screen. Format to show a maximum of two numbers
 to the right of the decimal point.
"""
# setting counter to 18 because that's how many
# lines are in the numbers.txt file
counter = 18


# main is organizing the program and assigning
# variables to each line in the numbers.txt file
# so that we can add them together and find the total
# and average of the numbers. then we print the correct
# statements based on the results.
def main():
    numbers_file = open('numbers.txt', 'r')

    num1 = int(numbers_file.readline())
    num2 = int(numbers_file.readline())
    num3 = int(numbers_file.readline())
    num4 = int(numbers_file.readline())
    num5 = int(numbers_file.readline())
    num6 = int(numbers_file.readline())
    num7 = int(numbers_file.readline())
    num8 = int(numbers_file.readline())
    num9 = int(numbers_file.readline())
    num10 = int(numbers_file.readline())
    num11 = int(numbers_file.readline())
    num12 = int(numbers_file.readline())
    num13 = int(numbers_file.readline())
    num14 = int(numbers_file.readline())
    num15 = int(numbers_file.readline())
    num16 = int(numbers_file.readline())
    num17 = int(numbers_file.readline())
    num18 = int(numbers_file.readline())

    numbers_file.close()

    total = (num1 + num2 + num3 + num4 + num5 + num6 + num7
             + num8 + num9 + num10 + num11 + num12 + num13
             + num14 + num15 + num16 + num17 + num18)

    print("There were " + str(counter) + " numbers.")
    print("The total of all numbers was: " + format(total, ','))

    average = total / 18
    print("The average of the numbers was: " + format(average, '.2f'))


main()
