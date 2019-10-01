"""
Lesson:
Copy your file from the previous exercise
(Average numbers) and modify it so that it
handles the following exceptions:

It should handle any IOError exceptions that
are raised when the file is opened and data is
read from it. It should handle any ValueError
exceptions that are raised when the items that
are read from the file are converted to a number.
NOTE:

You can test for IOErrors by temporarily changing
the name of your data file.You can test for ValueErrors
 by using this data file: numbers2.txt
"""
# setting counter to 18 because that's how many
# lines are in the numbers.txt file
counter = 18


# assigning main to open the file and then trying
# to read each line from the file and then add them
# together. with the numbers2.txt file, this will not
# work because there are 2 pieces of data that are not
# numbers. this then allows the ValueError to step in
# and alert the user that there was an error with the file.
def main():
    numbers_file = open('numbers2.txt', 'r')
    try:
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
    except IOError:
        print("An error occurred trying to read the file.")
    except ValueError:
        print("There was non-numeric data in the file." '\n'
              "Processing of the file has stopped.")


main()
