class Employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property  
    def email(self):
        return "{}.{}@email.com".format(self.first,self.last)  
    @property 
    def fullname(self):
        return "{}{}".format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first=None
        self.last=None
        
first=Employee("Nika","paila")
print(first.email)
first.fullname="Saba Manjavidze"
print(first.email)