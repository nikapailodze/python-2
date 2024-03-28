class Employee:
    num_of_emps=0
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@email.com"
        self.pay=pay
        Employee.num_of_emps+=1
    def fullname(self):
        return "{}{}".format(self.first,self.last)
    def apply_rise(self):
        self.pay=int(self.pay*self.raise_amt)
    # def set_raise_amt(self,amount):
    #     self.raise_amt=amount
    
    
    
    
    
    # cls changes for the whole class
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount
#||       
    #crate new object with cls method
    @classmethod
    def form_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    
    
emp_str_1="John-Doe-70000"
emp_str_2="Steve-Smith-30000"
emp_str_3="Jane-Doe-90000"
first,last,pay=emp_str_1.split('-')    
new_emp_1=Employee.form_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

#||

    
    

        
# first=Employee("nikol","pailodze",100)
# second=Employee("maks","iavich",80)
# print(first.raise_amt)
# first.set_raise_amt(1.06)
# print(first.raise_amt)
# print(second.raise_amt)
# print(Employee.raise_amt)