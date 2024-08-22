class Student:
    def __init__(self,name,age):
        self.__name = name ## this is an private attribute
        self.__age = age ## this is an private attribute
    # this is getter getting the data that are private
    def get_name(self):
        return self.__name

    def set_name(self,new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        self.__age = new_age

student1 = Student('Dren',17)
print(student1.get_name())

student1.set_name('Dren Llazani')

print(student1.get_name())
print(student1.get_age())
student1.set_age(18)
print(student1.get_age())
