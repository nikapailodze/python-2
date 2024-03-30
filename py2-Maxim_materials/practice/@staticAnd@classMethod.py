import datetime
class Employee:
    nums_of_emps=0
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

    @classmethod
    def set_raise_amt(cls,amount):
        cls.rise_amt=amount

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or  day.weekday()==6 :
            return False
        return True


dev_1=Employee("Corey", "Schafer",50000)
dev_2=Employee("Nika","Pailodze",60000 )



my_date=datetime.date(2024,3,29)
print(Employee.is_workday(my_date))










# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'



# new_emp_1=Employee.from_string(emp_str_1)




# print(new_emp_1.email)
# print(new_emp_1.pay)
# print(new_emp_1.first)


# Employee.set_raise_amt(1.05)



# print(Employee.rise_amt)
# print(dev_1.rise_amt)
# print(dev_2.rise_amt)