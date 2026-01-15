class Employee:
    raise_amount = 1.5
    def __init__(self,first,pay,last):
        self.first = first
        self.last = last
        self.pay= pay
        self.email = first + '.'+last+'@company.com'

    def Fullname(self):
        return '{} {} {}'   .format(self.pay,self.first,self.last)

    def apply_raise(self):
         self.pay = int(self.pay *  self.raise_amount)
         return self.pay
class Developer(Employee):
    raise_amount = 2
    def __init__(self, first, pay, last, prog_lang):
        super().__init__(first, pay, last)
        self.prog_lang = prog_lang

    def __str__(self):
       return f"{self.first} {self.last} - {self.prog_lang}"

    def __repr__(self):
        return f"Developer('{self.first}', {self.pay}, '{self.last}', '{self.prog_lang}')"


class Manager(Employee):
    #raise_amount = 2
    def __init__(self, first, pay, last, employee):
        super().__init__(first, pay, last)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee
    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)
    def remove_emp(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)
    def show(self):
        print(self.employee)


dev1 = Developer('shiva',5000,'sai','python')

dev2 = Employee('shayma',5000,'begum')

mgr1 = Manager('Mani',8000,'marka',[dev1])
print(mgr1.show())
mgr1.add_emp(dev2)
print(mgr1.show())


#print(dev1.pay)
#dev1.apply_raise()
#print(dev1.pay)
#print(dev1.email)


