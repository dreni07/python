class Dog:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f'{self.name} Woof')


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f'{self.name} Meoow!')


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f'{self.name} Chirp')


dog_instance = Dog('Bob')
cat_instance = Cat('Buddy')
bird = Bird('Tuity')

for animal in (dog_instance,cat_instance,bird):
    animal.sound()

import math

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

circle = Circle(5)
triangle = Triangle(10,20)
rectangle = Rectangle(6,7)
roundi = round(circle.area(),2)
class Klasa:
    def __init__(self,role,name):
        self.role = role
        self.name = name

class Student(Klasa):
    def findRole(self):
        if self.role == 's':
            print(f'{self.name} is a student')
        elif self.role == 'i':
            print(f'{self.name} is an instructor')


class Module(Klasa):
    def __init__(self,module_name,role,name):
        self.module_name = module_name
        super().__init__(role,name)

    def findModule(self):
        if self.role == 's':
            print(f' {self.name} is learning {self.module_name}')
        elif self.role == 'i':
            print(f'{self.name} is teaching {self.module_name}')


last_instance = Module('python','s','Dren')
last_instance.findModule()
my_instance = Student('i','Alma')
my_instance.findRole()