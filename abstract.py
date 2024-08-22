from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length*self.length

    def perimeter(self):
        return self.length * 4


katrori = Rectangle(5)
print(katrori.area())
print(katrori.perimeter())


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self,name,author,year):
        self.name = name
        self.author = author
        self.year = year

    def print_info(self):
        print(f'Book {self.name} Author: {self.author} Year: {self.year}')

new_book = Book('The great gatby','F Scott FitzGerald',1700)
print(new_book.print_info())




## CHALLENGE
# DEFINE A BASE CLASS DIGITAL SCHOOL
# PRIVATE ATTRIBUTES NAME,CITY,STATE,COURSES
# GETTERS AND SETTERS FOR ALL ATTRIBUTES
## METHODS: SHOW SCHOOL INFO RETURNS A DICTIONARIE WITH SCHOOL INFO
## METHOD 2: ORGANIZE_HACKATHON() DEFINE A PLACEHOOLDER TO OVERRIDEN BY SUBCLASS

#