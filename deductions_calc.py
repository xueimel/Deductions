from employee import Employee
import re

class Deductions_Calc:
"""
Provides the base for setting the calculations of the benefits deductions
for both individual employee as well as the entire array of employees.
Constructor allows for easy alterations to the payin amount or balance,
dependent payin amount and the employees paycheck amount.
"""
    def __init__(self, base_pay, payin_amount, dep_payin_amount):
        self.base_pay = base_pay
        self.payin_amount = payin_amount
        self.dep_payin_amount = dep_payin_amount
        self.both_names_apply = True # If first and last names both count for deductions


    def set_balance(self, emp):
        f_name, l_name = emp.get_name().split(" ")
        deduction = self.name_deduction(f_name, l_name)
        print(deduction)
        if deduction:
            emp.balance = self.payin_amount - (self.payin_amount * .1)
        else:
            emp.balance = self.payin_amount


    def update_balance(self, emp):
        if emp.num_deps > 0:
            deduct_count = 0
            for dep in emp.deps:
                deduction = self.name_deduction(dep[0], dep[1])
                if deduction:
                    emp.balance += emp.balance + self.dep_payin_amount + (self.dep_payin_amount * .1)
                else:
                    emp.balance += emp.balance + self.dep_payin_amount


    def name_deduction(self, f_name, l_name):
        pattern = re.compile(r'[A | a].*')
        if re.findall(pattern, f_name):
            return True
            if both_names_apply:
                if re.findall(pattern, l_name):
                    return True
        return False


    def get_individual_weekly(self, emp):
        return emp.balance / emp.weeks


    def calc_all_weekly(self, list_of_emps):
        total = 0
        for emp in list_of_emps:
            total += get_individual_weekly(emp)
        return total



    #
