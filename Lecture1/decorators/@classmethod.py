# class Car():
#     def __init__(self, features):
#         self.features=features
#     def __str__(self):
#         return ', '.join(self.features)
    
#     @classmethod
#     def truck(cls):
#        return cls(['truck', '4x4', 'big'])
    
    
# newCar=Car.truck()
# print(newCar)

class Car:
    default_features = ['automatic transmission', 'GPS', 'sunroof']

    def __init__(self, features=None):
        if features is None:
            self.features = Car.default_features
        else:
            self.features = features

    def __str__(self):
        return ', '.join(self.features)

    @classmethod
    def set_default_features(cls, features):
        cls.default_features = features

# Example usage:
car1 = Car()
print("Car 1 Features:", car1)

# Changing the default features for all cars
Car.set_default_features(['manual transmission', 'Bluetooth',])

car2 = Car()
print("Car 2 Features:", car2)
