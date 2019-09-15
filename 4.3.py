# listing the variables

average_rainfall = 0
total_rainfall = 0

# the program

print("This program will calculate total rainfall and average monthly rainfall for a period of years.")
num_years = int(input("How many years would you like to collect data for? "))
for current_year in range(1, num_years + 1):
    print("Year number " + str(current_year))
    for month in ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"):
        monthly_rainfall = float(input("How much rain fell during the month of " + month + "? "))
        total_rainfall = total_rainfall + monthly_rainfall
months = 12 * num_years
average_rainfall = total_rainfall / months
print("The total amount of rainfall was: " + format(total_rainfall, '.2f') + " inches")
print("The average monthly rainfall was: " + format(average_rainfall, '.2f') + " inches")
