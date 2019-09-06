#  setting our variable
user_age = int(input("Please enter your age: "))
#  printing the results based on what the user input
if user_age <= 1:
    print('You are an infant.')
elif user_age < 13:
    print("You are a child.")
elif user_age < 20:
    print("You are a teenager.")
elif user_age >= 20:
    print("You are an adult.")
