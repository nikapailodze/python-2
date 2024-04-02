import random as rd

digit_ls=[[rd.randint(1,10),rd.randint(1,10),rd.randint(1,10)] for i in range(10)]


class Trapezoid():
    def __init__(self,digit):
        self.height=digit[0]
        self.base1=digit[1]
        self.base2=digit[2]

    def __str__(self):
        return "height= "+ str(self.height)+ f" base1= {self.base1} and base2= {self.base2}"
    
    def area(self):
        return (self.base1+self.base2)*self.height/2
    
    def __le__(self,other):
        return self.area() <=other.area()
class Triangle(Trapezoid):
    def __init__(self, digit):
        super().__init__(digit)
        self.base2=None
    def __str__(self):
        return "height= "+ str(self.height)+ f" base= {self.base1}"
    def area(self):
        return self.base1*self.height/2
        
# trap
Trap_1=Trapezoid(digit_ls[0])
Trap_2=Trapezoid(digit_ls[9])

# print(Trap_1)
# print(Trap_2)
# a=Trap_1.area()
# b=Trap_2.area()
# print(Trap_1<=Trap_2)
# print(Trap_1.area())

# Tri_1=Triangle(digit_ls[0])
# print(Tri_1)