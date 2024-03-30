'''
Private Keyword
Private members of a class can be accessed by other members within the class and are also available to their subclasses.

No other entity can access these members. In order to do so, they can inherit the parent class.
Python has a unique convention to make a member protected: Add a prefix _ (single underscore). 
This prevents its usage by outside entities unless it is a subclass.

'''

class Employee:

    def __init__(self):
        self.__a="hi"
        
    def __hi(self):
        print ("hi")
        

        
one=Employee()
#print (one.__a)
one.__hi()
        
