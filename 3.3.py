# first printing the available packages to the user
print("Mobile Phone Service Packages:")
print("Package A: For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.")
print("Package B: For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.")
print("Package C: For $69.99 per month unlimited minutes provided.")

# variables
total_cost = 0
additional_minutes = 0
package_price = 0

# what the user inputs to determine their package price
package = (input("Which package do you have? (A, B, or C) "))
minutes_used = int(input("How many minutes did you use this month? "))

# the code itself and how we get to our final results
if package == "A" or package == "a":
    package_price = 39.99
    if minutes_used > 450:
        additional_minutes = minutes_used - 450
        total_cost = package_price + (additional_minutes * 0.45)
    if minutes_used <= 450:
        total_cost = package_price
if package == "B" or package == "b":
    package_price = 59.99
    if minutes_used > 900:
        additional_minutes = minutes_used - 900
        total_cost = package_price + (additional_minutes * 0.40)
    if minutes_used <= 900:
        total_cost = package_price
if package == "C" or package == "c":
    package_price = 69.99
    total_cost = package_price

# printing our results either correctly or incorrectly as an error message
if package == "A" or package == "a" or package == "B" or package == "b" or package == "C" or package == "c":
    (print("With package " + package + " and " + str(minutes_used) + " minutes used, you owe: $" + str(format(total_cost, '.2f'))))
else:
    print("Error: You did not enter the correct information.")
