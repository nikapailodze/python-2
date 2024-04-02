class Friends(object):
    num_of_friends=0
    set_age=50
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        Friends.num_of_friends+=1

    def raise_age(self):
        self.age=self.set_age
    @classmethod
    def rise_set_age(cls,arg):
        cls.set_age=arg

    @property
    def fullname(self):
        return "{} {} {} years old".format(self.name,self.surname,self.age)
    

    @fullname.setter
    def fullname(self,str_fr):
        first,last=str_fr.split(" ")
        self.name= first
        self.surname=last 
    
    @fullname.deleter
    def fullname(self):
        self.name= None
        self.surname=None 


fr_1=Friends("Gia","Suramelashvili",19)
fr_2=Friends("Zaliko","Bergeri",19)

fr_1.fullname="nuki koshkelishvili"

# del fr_1.fullname
fr_1.raise_age()
fr_2.raise_age()

# print(fr_2.fullname)
# print(fr_1.fullname)
# print(Friends.num_of_friends)

Friends.rise_set_age(100)
fr_2.raise_age()

# print(fr_2.fullname)


# print(fr_2.fullname)
# print(fr_1.fullname)