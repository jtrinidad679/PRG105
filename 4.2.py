# the time variable is holding the users number of days worked
# variables

day = 0
SALARY = 0.01
daily_income = 0
total_earned = 0

# asking user to input how many days they will work

time = int(input("How many days will you work for pennies a day? "))

# printing the header

print("Days Worked  |  Amount Earned That Day")
print("-" * 38)

# determining the amount they'll earn over the days they input and
# formatting it correctly to look good in the table

for day in range(1, time + 1):
    if day == 1:
        daily_income = SALARY
        print("          " + str(day) + "  |  $" "          " + format(daily_income))
    elif 1 < day <= 9:
        daily_income *= 2
        print("          " + str(day) + "  |  $" "          " + format(daily_income))
    elif day > 9:
        daily_income *= 2
        print("         " + str(day) + "  |  $" "          " + format(daily_income))
    total_earned += daily_income

print("Total earned over " + str(day) + " days is $" "     " + format(total_earned, '.2f'))
