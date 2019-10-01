"""
Lesson:
Download the file names.txt

Save it into the same project folder in PyCharm
that you are using for this project.

Your Python file will:

Read and Display the list of names from the file
Display the number of names that are read from the
file (You will need a variable to keep a count of
the number of items read from the file.)
"""
# assigning our main function to organize
# the program and read the lines within
# the names.txt file and print them.
# then printing the amount of names in
# the file using the counter variable.

counter = 22


def main():
    names_file = open('names.txt', 'r')
    for line in names_file:
        print(line)
    print("There were " + str(counter) + " names in the file.")


main()
