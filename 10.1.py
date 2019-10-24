"""
Lesson:
Design a class that holds the following personal data: name, address, age, and phone number.
Write appropriate accessor and mutator methods (get and set). Write a program that creates
three instances of the class. One instance should hold your information and the other two
should hold your friends or family members' information.  Just add information, don't get it
from the user.  Print the data from each object, make sure to format the output for clarity and
ease of reading.
"""


class PersonalInformation:
    def personal_info(self):
        print(self.name)
        print(self.address)
        print(self.age)
        print(self.phone)


self = PersonalInformation()
self.name = "Jasmine"
self.address = "2100 Aspen Drive"
self.age = "18"
self.phone = "888-888-8888"

self2 = PersonalInformation()
self2.name = "Karen"
self2.address = 'Walmart - Yelling at the employees: "LET ME SEE YOUR MANAGER!!"'
self2.age = "60"
self2.phone = "N/A - Karen believes cell phones are the devil."

self3 = PersonalInformation()
self3.name = "Kyle"
self3.address = "Monster Energy Drink HQ - Probably just punching the drywall."
self3.age = "25"
self3.phone = "999-999-9999"


self.personal_info()
print("-" * 70)
self2.personal_info()
print("-" * 70)
self3.personal_info()
