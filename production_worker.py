# creating the class Employee and the subclass ProductionWorker


class Employee:
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number

    def set_employee_name(self, employee_name):
        self.employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number

    def get_employee_name(self):
        return self.employee_name

    def get_employee_number(self):
        return self.employee_number


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift, pay_rate):
        super().__init__(employee_name, employee_number)
        self.pay_rate = pay_rate
        self.shift = shift

    def set_pay_rate(self, pay_rate):
        self.pay_rate = pay_rate

    def set_shift(self, shift):
        self.shift = shift

    def get_pay_rate(self):
        return self.pay_rate

    def get_shift(self):
        return self.shift

    def __str__(self):
        return "Employee Name: " + self.employee_name + \
               "\nEmployee Number: " + self.employee_number + \
               "\nShift: " + self.shift + \
               "\nPay Rate: " + self.pay_rate
