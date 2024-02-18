class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        self.d = 'kkkkkk'

emp_1 = Employee('Corey', 'Shafer',  500000,)
emp_2 = Employee('Test', 'User',  60000,)

print(emp_1.d) 


