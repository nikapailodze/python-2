class Employee:
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@email.com"
        self.pay=pay
    def fullname(self):
        return "{}{}".format(self.first,self.last)
    def apply_rise(self):
        self.pay=int(self.pay*self.raise_amt)

class Developer(Employee):
    raise_amt=1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())
dev_1=Developer("nika","pail",50000,"python")
dev_2=Developer("vigac","vigacadze", 20000,"java")
print(dev_1.pay)
dev_1.apply_rise()
print(dev_1.pay)
mgr_1=Manager("suzana","smith",90000,[dev_1])
print(mgr_1.email)
mgr_1.print_emps()