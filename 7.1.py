total_rainfall = 0
# Prints out what the program does and the current year. For this assignment,
# we are only focusing on one year.
print("This program will calculate total rainfall and average monthly rainfall for a period of years.")
print("Year number 1")
# Creating our list to store the months in the year.
months_list = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
# Creating an empty list that will store the rainfall statistics that the user
# inputs in the for loop below.
rainfall_per_month = []
# The for loop goes through the months in the list and asks the user for the rainfall
# of that month. The number is then appended into the rainfall_per_month list.
for month in months_list:
    monthly_rainfall = float(input("How much rain fell during the month of " + month + "? "))
    total_rainfall = total_rainfall + monthly_rainfall
    rainfall_per_month.append(monthly_rainfall)
num_months = 12
average_rainfall = total_rainfall / num_months
print("The total amount of rainfall was: " + format(total_rainfall, '.2f') + " inches")
print("The average monthly rainfall was: " + format(average_rainfall, '.2f') + " inches")

# Calculating our least and maximum inches of rainfall.
# Creating two variables that store the index number for the least and maximum
# amounts of rainfall for the month.
least_rainfall = min(rainfall_per_month)
max_rainfall = max(rainfall_per_month)
least_rainfall_index = rainfall_per_month.index(least_rainfall)
max_rainfall_index = rainfall_per_month.index(max_rainfall)

# Printing the results and using the index number from the rainfall_per_month list
# to determine the correct month that goes with the least and maximum amounts of rain.
print("The month of ", months_list[least_rainfall_index], " had the least amount of rain, with " + format(least_rainfall),
      " inches of rain.")
print("The month of ", months_list[max_rainfall_index], " had the maximum amount of rain, with " + format(max_rainfall),
      " inches of rain.")
