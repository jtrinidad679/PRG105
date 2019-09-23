"""
Write a program that asks the user to enter the monthly costs for the following expenses incurred
from operating his or her automobile: loan payment, insurance, gas, and maintenance. The program should
then display the total monthly cost of these expenses, and the total annual cost of these expenses.

Assign meaningful names to your functions and variables. Every function also needs a comment explaining what it does and what other function it works with.


Program Outline:

main():

calls the other functions
main is traditionally used as the first function in a program to organize the flow of the program logic
monthly():

Gather information from the user
Accumulate the total in a local variable
Print the monthly costs on screen, formatted appropriately for money
Pass the monthly cost to Function 2
yearly(monthly_total):

Accepts a float parameter
Calculates yearly cost by multiplying the monthly cost by 12
Displays the yearly cost on screen, formatted appropriately for money
"""

# the main function that's going to call monthly


def main():
    monthly()


# the monthly function calculates all of the payments and defines yearly?


def monthly():
    loan = float(input("Enter your monthly loan payment: "))
    insurance = float(input("Enter your monthly insurance payment: "))
    gas = float(input("Enter your monthly gas payment: "))
    maintenance = float(input("Enter your monthly maintenance payment: "))
    monthly_cost = loan + insurance + gas + maintenance
    print("Your total monthly costs are: " + format(monthly_cost, '.2f'))
    yearly(monthly_cost)


# yearly is defined in monthly so monthly calls
# yearly and then they're both taken to main


def yearly(monthly_cost):
    yearly_cost = monthly_cost * 12
    print("Your total yearly cost is: " + format(yearly_cost, '.2f'))


main()
