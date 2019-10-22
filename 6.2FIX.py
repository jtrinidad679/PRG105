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
# Assigning the initial total and counter variables and setting them
# to 0. Opening the numbers.txt file. The for loop then reads the lines
# within the file and for each line, +1 will be added to the counter.
# After the for loop has read all of the lines, we close the file and
# print how many numbers were in the file, thanks to the counter, and
# calculate the average by dividing the total by counter.


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

    average = total / counter
    print("The average of the numbers was: " + format(average, '.2f'))


main()
