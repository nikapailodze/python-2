class Employee:
    rise_amt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first + '.'+last+'@emial.com'
        self.pay=pay

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def applay_rise(self):
        self.pay = int(self.pay * self.rise_amt)


class Developer(Employee):
    rise_amt=1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)  # or Employee.__init__(self,first,last,pay)
        self.prog_lang=prog_lang
        



class Manager(Employee):
    
    def __init__(self,first,last,pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees= []
        else:
            self.employees=employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)  
    
    def remove_emp(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)   
    def print_emps(self):
        for emp in self.employees:
            print("-->",emp.fullname())

    


dev_1=Developer("Corey", "Schafer",50000, "Python")
dev_2=Developer("Nika","Pailodze",60000, "Java")


mrg_1= Manager("Sue","Smith",90000, [dev_1])

print(mrg_1.email)

mrg_1.add_emp(dev_2)


mrg_1.print_emps()

mrg_1.remove_emp(dev_1)
mrg_1.print_emps()



