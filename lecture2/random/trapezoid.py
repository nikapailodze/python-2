class Trapezoid(object):
    def __init__(self,base1,base2,height):
        # self.area=area
        self.base1=base1
        self.base2=base2
        self.height=height
    def __str__(self):
        return "Base1: "+ str(self.base1)+ " " + "Base2: "  + str(self.base2)+" "+ "Height: "+str(self.height)
    
    def area(self):
        return (self.base1+self.base2/2)*self.height
    def __le__(self,other):
        return self.area()>=other.area()
    def __eq__(self,other):
        return self.area()==other.area()
    
class Rectangle(Trapezoid):
    def __init__(self, side1, side2, base1, height):
        self.side1=side1
        self.side2=side2
        self.base1=base1
        self.height=height
    def area(self):
        return
        
        
a=Trapezoid(5,6,7)
b=Trapezoid(1,2,3)
print(a)
print(a.area())
print(b.area())
print(a.__le__(b))