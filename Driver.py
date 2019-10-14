from employee import Employee
import time
from deductions_calc import Deductions_Calc


class Driver:
    """
    Combines the modules/classes employee and deductions_calc to
    form a cohesive app. This app allows the user to enter information
    about employees and see their estimated payments for benefit deductions.
    """
    def __init__(self):
        self.calc = Deductions_Calc(2000, 1000, 500)
        self.employees = []

    def enter_employee(self):
        name = str(input("Enter Employee's First and Last Names: "))
        name_split = name.split(" ")
        emp = Employee(name_split[0], name_split[1])

        self.calc.set_balance(emp)
        # set the balance and emp name in dict
        self.employees.append(emp)
        resp = str(input("Does the employee have any dependents (yes/no): "))

        while resp.lower() == 'yes':
            dep_name = str(input('Enter the dependents name:'))
            name_split = dep_name.split(" ")
            emp.add_dependent(name_split[0], name_split[1])
            self.calc.update_balance(emp)
            resp = str(input("Does the employee have any more dependents (yes/no): "))

        print(emp.get_name(), "would have a weekly balance of: {} ".format(emp.get_balance()))


    def add_dependent(self):
        name = str(input("Please Enter the First and Last Names of the Employee you'd like to add a dependent to: "))
        resp = 'yes' # just to get us into the while loop the first time
        while resp.lower() == 'yes':
            dep_name = str(input('Enter the dependents name:'))
            d_name_split = dep_name.split(" ")
            index = self.employees.index(name)
            if index > 0:
                self.employees[index].add_dependent(d_name_split[0], d_name_split[1])
            self.calc.update_balance(emp)
            resp = str(input("Does the employee have any more dependents (yes/no): "))
        print(emp.get_name(), "would have a weekly balance of: {} ".format(emp.get_balance()))


        def ind_total(self):
            name = str(input("Enter Employee's First and Last Names: "))
            emp = get_emp_helper(name)
            if emp is not None:
                print(emp.get_name(), "would have a weekly balance of: {} ".format())


        def remove_employee(self):
            resp = 'yes'
            while resp.lower() == 'yes':
                name = str(input("Who would you like to remove? "))
                emp = get_emp_helper(name)
                if emp is not None:
                    self.employees.remove(emp)
                    del d.employees[emp]
                    print(emp, "has been removed")
                else:
                    str(input("Sorry, I was unable to locate that employee. Would you like to try agian? (yes/no)"))

        def all_total(self):
            print("total for all employees: ", self.calc.calc_all_weekly(self.employees))

        def get_emp_helper(self, name):
            for emp in self.employees:
                if name == emp.get_name():
                    return emp


if __name__ == '__main__':
    d = Driver()
    while True:
        options = ['ADD EMPLOYEE', 'REMOVE EMPLOYEE', 'ADD DEPENDENT TO EMPLOYEE',
        'REMOVE DEPENDENT FROM EMPLOYEE', 'GET TOTAL FOR INDIVIDUAL EMPLOYEE',
        'GET TOTAL FOR ALL EMPLOYEES', 'EXIT']

        print('Please Select One of the Following options:')
        time.sleep(1)
        for option in options:
            print(option)
            time.sleep(.35)
        selection = str(input())

        if selection.lower() == "add employee":
            d.enter_employee()

        if selection.lower() == "remove employee":
            d.remove_employee()

        if selection.lower() == "add dependent to employee":
            d.add_dependent()

        if selection.lower() == "remove dependent from employee":
            pass # TODO: Implement functionality later

        if selection.lower() == "get total for individual employee":
            d.ind_total()

        if selection.lower() == "get total for all employees":
            d.all_total()
