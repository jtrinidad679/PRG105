"""
Lesson Objective(s):
Read files into lists
Strip \n from file values
Search for values in lists
Lesson:
The following two files contain names of popular Boy's names and popular Girl's names.
Download them and add them to your project file.

BoyNames.txtPreview the document

GirlNames.txtPreview the document

Then, write a program that reads the contents of the two files into two separate lists.
The user should be able to enter a boy's name or a girl's name. The application should
check both lists, and then display messages indicating whether the names were among the
most popular if the name was on one of the lists or that the name was not on the lists of popular names.
"""

# I don't think it's necessary but I assigned the lists of girl and boy names to
# the variables girl and boy. The main function processes the lists and returns the
# correct print statement based on the popularity of the name.


def main():
    girl = girl_names()
    boy = boy_names()

    user_name = input("Please enter a name: ")
    if user_name in boy or user_name in girl:
        print("The name " + user_name + " is a popular name!")
    else:
        print("The name " + user_name + " is not a popular name.")


# I assigned each function (girl_names and boy_names) to open the files
# and read them into their respective lists. The functions make it easier to read
# the code instead of it all being jumbled together. I stripped the \n inside the files
# and returned the boy and girl names to the main function.


def girl_names():
    girl_names_list = open('GirlNames.txt', 'r')
    girl_names_in_list = girl_names_list.readlines()
    girl_names_list.close()
    index = 0
    while index < len(girl_names_in_list):
        girl_names_in_list[index] = girl_names_in_list[index].rstrip('\n')
        index += 1
    return girl_names_in_list


def boy_names():
    boy_names_list = open('BoyNames.txt', 'r')
    boy_names_in_list = boy_names_list.readlines()
    boy_names_list.close()
    index = 0
    while index < len(boy_names_in_list):
        boy_names_in_list[index] = boy_names_in_list[index].rstrip('\n')
        index += 1
    return boy_names_in_list


# Calling main to complete the process.


main()
