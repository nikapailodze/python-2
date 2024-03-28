import random as rd
Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]
class Trapezoid(object):
    def __init__(self, digit):
        self.base1 = digit[0]
        self.base2 = digit[1]
        self.height = digit[2]
    def __str__(self):
        return "Base1: "+ str(self.base1)+" Base2: "+str(self.base2)+" Height: "+ str(self.height)
    def area(self):
        return (self.base1 + self.base2) / 2 * self.height
    def __le__(self,other):
        return self.area()<=other.area()
    def __mo__(self, other):
        return self.area()>=other.area()
    def __eq__(self,other):
        return self.area()==other.area()
    def __add__(self, other):
        new_base1 = self.base1 + other.base1
        new_base2 = self.base2 + other.base2
        new_height = self.height + other.height
        return Trapezoid([new_base1, new_base2, new_height])
    
    def __mul__(self, other):
        new_base1 = self.base1 * other.base1
        new_base2 = self.base2 * other.base2
        new_height = self.height * other.height
        return Trapezoid([new_base1, new_base2, new_height])
    
class Rectangles(Trapezoid):
    def __init__(self, digit):
        super().__init__(digit)
        self.height=None
    def __str__(self):
        return str(self.base1)+" "+ str(self.base2)
    def area(self):
        return self.base1 * self.base2

class Square(Rectangles):
    def __init__(self, digit):
        super().__init__(digit)
        self.base2=None
    def __str__(self):
        return str(self.base1)
    def area(self):
       return self.base1**2
    
    
    
    
trap1=Trapezoid(Digit_list[0])
trap2=Trapezoid(Digit_list[1])

print(trap1)

print(trap2)

# print(trap1.area())

# print(trap1 <= trap2)
# print(trap1 >= trap2)
# print(trap1==trap2)

# print(trap1+trap2)
# print(trap1*trap2)



rect1 = Rectangles(Digit_list[0])

rect2 = Rectangles(Digit_list[1])

print(rect1)  
print("Area:", rect1.area())  
print(rect1 <= rect2)


squ1=Square(Digit_list[0])
squ2=Square(Digit_list[1])

print(squ1)
print("Area:", squ1.area())  
print(squ1 >= squ2)