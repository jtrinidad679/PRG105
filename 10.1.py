"""
Lesson:
Design a class that holds the following personal data: name, address, age, and phone number.
Write appropriate accessor and mutator methods (get and set). Write a program that creates
three instances of the class. One instance should hold your information and the other two
should hold your friends or family members' information.  Just add information, don't get it
from the user.  Print the data from each object, make sure to format the output for clarity and
ease of reading.
"""
# Defining my class as PersonalInformation. Then defining the variables name, address, age, and phone to self.name,
# self.address, self.age, and self.phone. Then the personal_info function prints out those variables. Info_one/two/three
# all hold the information which is then passed into the __init__ function. I do not know a Karen or a Kyle, they are
# made up. Then, you simply call the functions to go through each info variable and print out their results.


class PersonalInformation:
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def personal_info(self):
        print(self.name)
        print(self.address)
        print(self.age)
        print(self.phone)


info_one = PersonalInformation("Jasmine", "2100 Aspen Drive", "18", "888-888-8888")
info_two = PersonalInformation("Karen", 'Walmart - Yelling at the employees: "LET ME SEE YOUR MANAGER!!"',
                               "60", "N/A - Karen believes cell phones are the devil.")
info_three = PersonalInformation("Kyle", "Monster Energy Drink HQ - Probably just punching the drywall.",
                                         "25", "999-999-9999")

info_one.personal_info()
print("-" * 70)
info_two.personal_info()
print("-" * 70)
info_three.personal_info()
