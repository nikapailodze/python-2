# -*- coding: utf-8 -*-
"""შენიშვნა. ქვემოთ მოყვანილი კოდი Digit_list სიმრავლეს ავსებს 200 ჩანაწერით """
import random as rd
Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]

"""        
    1. განსაზღვრეთ ტოლფერდა ტრაპეციის კლასი, რომელიც პარამეტრად მიიღებს ზემოთ
        მოყვანილი ტიპის სამეულს. კლასს უნდა ჰქონდეე სამი ატრიბუტი:
           ტრაპეციის ფუძეები და სიმაღლე
        და მეთოდები:
           კონსტრუქტორი, __str__() (რომელიც დააბრუნებს ტრაპეციის მონაცემებს), ტრაპეციის 
           ფართობის გამოსათვლელი, გადატვირთეთ ორი ტრაპეციის ფართობის მიხედვით შედარების 
           (<=, ==) შესაბამისი მეთოდი (__le__, __eq__).
        განსაზღვრეთ ტოლფერდა ტრაპეციის მემკვიდრე მართკუთხედების კლასი, და მართკუთხედების
        კლასის მემკვიდრე კვადრატების კლასი და თითოეულ მათგანში გადატვირთეთ შესაბამისი მეთოდები.       
"""
import random as rd
Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]
class Trapecia:
    def __init__(self, digit):
        self.fudze1 = digit[0]
        self.fudze2 = digit[1]
        self.simagle = digit[2]
    def __str__(self):
        return str(self.fudze1)+" "+str(self.fudze2)+" "+ str(self.simagle)
    def fartobi(self):
        return (self.fudze1 + self.fudze2) / 2 * self.simagle
    def __le__(self, other):
        return self.fartobi() <= other.fartobi()
    def __eq__(self, other):
        return self.fartobi() == other.fartobi()
class Martkutxedi(Trapecia):
    def __init__(self, digit):
        super().__init__(digit)
        self.simagle=None
    def __str__(self):
        return str(self.fudze1)+" "+ str(self.fudze2)
    def fartobi(self):
        return self.fudze1 * self.fudze2
class Kvadrati(Martkutxedi):
    def __init__(self, digit):
        super().__init__(digit)
        self.fudze2=None
    def __str__(self):
        return str(self.fudze1)
    def fartobi(self):
       return self.fudze1**2

def trap():
    trapecia1=Trapecia(Digit_list[0])
    trapecia2=Trapecia(Digit_list[1])
    print(trapecia1)
    print(trapecia2)
    print(trapecia1.fartobi())
    print(trapecia2.fartobi())
    print(trapecia1<=trapecia2)
    print(trapecia1==trapecia2)
def mark():
    martx1=Martkutxedi(Digit_list[0])
    print(martx1)
    martx2=Martkutxedi(Digit_list[1])
    print(martx2)
    print(martx1==martx2)







# trapecia1=Trapecia(Digit_list[0])
# trapecia2=Trapecia(Digit_list[1])
# print (trapecia1)
# print (trapecia2)
# print (trapecia1.fartobi())
# print (trapecia2.fartobi())
# print (trapecia1<=trapecia2)
# print (trapecia1==trapecia2)
# martx1=Martkutxedi(Digit_list[0])
# print(martx1)
# kvad1=Kvadrati(Digit_list[0])
# print (kvad1)
    