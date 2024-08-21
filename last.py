class Klasa:
    def gjuhaProgramuese(self):
        pass


class Student(Klasa):
    def __init__(self,name,gjuha):
        self.name = name
        self.gjuha = gjuha

    def gjuhaprogramimit(self):
        return self.gjuha


class Teacher(Klasa):
    def __init__(self,name,gjuha):
        self.name = name
        self.gjuha = gjuha

    def gjuhaprogramimit(self):
        return self.gjuha


teacheri = Teacher('Alma',['html','css','js','c#','python'])
studenti = Student('Dren',['html','css','js','typescript','python','django'])

print(studenti.gjuha)