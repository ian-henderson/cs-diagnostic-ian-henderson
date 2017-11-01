# Problem 13: Object Oriented Programming
class Automobile():
    def __init__(self, color):
        self.color = color


class Car(Automobile):
    def __init__(self, color):
        Automobile.__init__(self, color)
        self.number_of_wheels = 4
        self.model = '3'
        self.make = 'Mazda'
        self.top_speed = 100

    def honk(self):
        print('Beep Beep!')

    def description(self):
        print(vars(self))

car0 = Car('blue')
car0.honk()
car0.description()


'''
Problem 14: Inheritance

In object-oriented programming, inheritance when an object is defined as an
extension of another class. The new class inherits the parent obeject's
attributes. The extended classes provide a more specific purpose to the object.

A classic example of this would be an Animal class and then specific species.
e.g. You can have a Dog class that is an extension of an Animal class.
     Every class detail that is specific to a dog would be in the Dog class
     definition and the more generic information would be defined in the Animal
     class definition.
'''

class Motorcycle(Automobile):
    def __init__(self, color):
        Automobile.__init__(self, color)
        self.number_of_wheels = 4
        self.model = 'The fast one'
        self.make = 'Harley'
        self.top_speed = 80

motorcycle0 = Motorcycle('black')


class Truck(Automobile):
    def __init__(self, color):
        Automobile.__init__(self, color)
        self.number_of_wheels = 4
        self.model = 'F-150'
        self.make = 'Ford'
        self.top_speed = 90

truck0 = Truck('orange')
