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
a=Employee("Nikolozi","Pailodze",100)
print(a.first)
print(a.pay)
print(a.raise_amt)
print(a.fullname())
print(a.email)
a.apply_rise()
print(a.pay)