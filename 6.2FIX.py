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
# main is organizing the program and assigning
# variables to each line in the numbers.txt file
# so that we can add them together and find the total
# and average of the numbers. then we print the correct
# statements based on the results.


def main():
    total = 0
    counter = 0
    numbers_file = open('numbers.txt', 'r')

    for line in numbers_file:
        num = line.rstrip("\n")
        num = int(num)
        counter += 1
        total += num

    numbers_file.close()
    print("There were " + str(counter) + " numbers.")
    print("The total of all numbers was: " + format(total, ','))

    average = total / 18
    print("The average of the numbers was: " + format(average, '.2f'))


main()
