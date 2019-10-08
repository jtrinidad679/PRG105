total_rainfall = 0

print("This program will calculate total rainfall and average monthly rainfall for a period of years.")
print("Year number 1")

months_list = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
rainfall_per_month = []

for month in months_list:
    monthly_rainfall = float(input("How much rain fell during the month of " + month + "? "))
    total_rainfall = total_rainfall + monthly_rainfall
    rainfall_per_month.append(monthly_rainfall)
num_months = 12
average_rainfall = total_rainfall / num_months
print("The total amount of rainfall was: " + format(total_rainfall, '.2f') + " inches")
print("The average monthly rainfall was: " + format(average_rainfall, '.2f') + " inches")

least_rainfall = min(rainfall_per_month)
max_rainfall = max(rainfall_per_month)
least_rainfall_index = rainfall_per_month.index(least_rainfall)
max_rainfall_index = rainfall_per_month.index(max_rainfall)

print("The month of ", months_list[least_rainfall_index], " had the least amount of rain, with " + format(least_rainfall),
      " inches of rain.")
print("The month of ", months_list[max_rainfall_index], " had the maximum amount of rain, with " + format(max_rainfall),
      " inches of rain.")
