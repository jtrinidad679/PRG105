import production_worker
# importing the file with the classes


def main():
    # user input statements
    name = input("Enter Employee Name: ")
    employee_number = input("Enter Employee Number: ")
    pay_rate = input("Enter Pay Rate: ")
    shift = input("Enter Shift Number: ")
    # for some reason this doesn't work. if the user enters 1
    # it should display Morning as their shift or if the user
    # enters 2 it should display Night, but it doesn't do that.
    # It's probably an easy fix but I'm stumped. 
    if shift == 1:
        shift = 'Morning'
    elif shift == 2:
        shift = 'Night'
    employee_info = production_worker.ProductionWorker(name, employee_number, shift, pay_rate)
    print('-' * 20)
    print("Details of Employee:")
    print('-' * 20)
    print(employee_info)


main()
