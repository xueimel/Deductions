
class Employee:
"""
Creates an employee class that allows the user to store and keep information
of an employee for the runtime of the Driver class.
"""
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.num_deps = 0
        self.deps = []
        self.balance = 0
        self.weeks = 26

    def add_dependent(self, dep_f_name, dep_l_name):
        self.deps.append(dep_f_name + " " + dep_l_name)
        self.num_deps += 1

    def employee_info(self):
        ret_str = "Last Name: {}, First Name: {}, Balance: {}, Weeks Remaining: {}".format(
            self.l_name, self.f_name, self.balance,  self.weeks)
        return ret_str

    def get_name(self):
        return self.l_name +" "+ self.f_name

    def get_balance(self):
        return self.balance

    def dep_names(self):
        ret_str = ""
        for dep in self.deps:
            ret_str += dep
        return ret_str

    def balance(self):
        return self.balance

    def remaining_weeks(self):
        return self.weeks
