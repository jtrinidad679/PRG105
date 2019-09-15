# variable
RATE = 4.2

for time in (10, 15, 20, 25, 30):
    calories_burned = RATE * time
    print("You burned " + str(calories_burned) + " calories in " + str(time) + " minutes")
