class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        self.__age = new_age

studenti1 = Student('Dreni',17)
studenti1.age = 18
print(studenti1.age)
studenti1.name = 'DRENI'
print(studenti1.name)