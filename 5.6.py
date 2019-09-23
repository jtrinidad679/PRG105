"""
Write a program that asks a user to enter five test scores.
You will need to create five variables to hold these scores.

The purpose of this assignment is to get practice passing information
between functions, this is not a good example of the way programs are
really written, but it will help you to understand how to pass parameters.

Hint: if you have your mouse pointer at the end of a line you would like
to copy, Ctrl + d on windows or cmd + d on a mac will duplicate the line.



Write the Following Functions:

main -

1) asks the user for each of the five test scores, stores them in separate variables (score1, score2, etc)
2) calls calc_average and passes the five variables, storing the result in a variable
average = calc_average(score1, score2, score....
3) calls determine_grade, passing it the average variable, storing the result in a variable
4) prints the letter grade

calc_average -
1) This function should accept the five test scores as arguments
2) returns the average of the scores.

determine_grade -
1) This function should accept the average of the test scores as an argument
2) returns a letter grade based on the following scale:
"""


def main():
    score1 = int(input("Please enter the test score: "))
    score2 = int(input("Please enter the test score: "))
    score3 = int(input("Please enter the test score: "))
    score4 = int(input("Please enter the test score: "))
    score5 = int(input("Please enter the test score: "))
    average = calc_average(score1, score2, score3, score4, score5)

    print("Your average score was " + str(average))

    letter = determine_grade(average)

    print("Which gives you a final grade of: " + str(letter))


def calc_average(one, two, three, four, five):
    average_score = (one + two + three + four + five) / 5
    return average_score


def determine_grade(ave_score):
    if ave_score < 60:
        return "F"
    elif ave_score < 70:
        return "D"
    elif ave_score < 80:
        return "C"
    elif ave_score < 90:
        return "B"
    elif ave_score <= 100:
        return "A"


main()
