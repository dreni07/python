class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.__height = height
        self.__weight = weight

    def calculate_bmi(self):
        pass

    def get_bmi_category(self):
        pass

    def print_info(self):
        pass

    @property
    def the_height(self):
        return self.__height

    @the_height.setter
    def the_height(self,new_height):
        self.__height = new_height

    @property
    def the_weight(self):
        return self.__weight

    @the_weight.setter
    def the_weight(self,new_weight):
        self.__weight = new_weight

class Adult(Person):

    def calculate_bmi(self):
        the_bmi_calculation = self.the_weight/(self.the_height**2)
        return the_bmi_calculation

    def get_bmi_category(self):
        saving_the_bmi = self.calculate_bmi()
        if saving_the_bmi < 18.5:
            return 'you are underweight',saving_the_bmi
        elif 18.5 <= saving_the_bmi < 24.9:
            return 'you have normal weight',saving_the_bmi
        elif 24.9 <= saving_the_bmi < 29.9:
            return 'you are overweight',saving_the_bmi
        elif saving_the_bmi > 29.9:
            return 'you are just obese',saving_the_bmi

    def print_info(self):
        print(f'Hello {self.name} your bmi is {self.calculate_bmi()} and your category is {self.get_bmi_category()}')



class Child(Person):
    def calculate_bmi(self):
        the_bmi_calculation = self.the_weight/(self.the_height**2) * 1.3
        return the_bmi_calculation

    def get_bmi_category(self):
        saving_the_bmi = self.calculate_bmi()
        if saving_the_bmi < 14:
            return 'underweight'
        elif 14<=saving_the_bmi<18:
            return 'you have normal weight'
        elif 18<=saving_the_bmi<24:
            return 'you are overweight'
        elif saving_the_bmi >=24:
            return 'you are obese'


    def print_info(self):
        print(f'Hello {self.name} your bmi is {self.calculate_bmi()} and your category is {self.get_bmi_category()}')


class BMIApp:
    def __init__(self):
        self.persons = []

    def add_person(self,person):
        self.persons.append(person)

    def collect_user_data(self):
        input_name = input('Enter Your Name:')
        input_age = input('Enter Your Age')
        input_height = int(input('Enter Your Height:'))
        input_weight = int(input('Enter Your Weight:'))
        if input_age.isnumeric():
            input_age = int(input_age)
        else:
           while True:
               input_age = input('Enter Your Age Again')
               if input_age.isnumeric():
                   input_age = int(input_age)
                   break
               else:
                   continue
        if input_age >= 18:
            new_instance = Adult(input_name,input_age,input_height,input_weight)
            self.add_person(new_instance)
        else:
            new_instance = Child(input_name,input_age,input_height,input_weight)
            self.add_person(new_instance)

    def run(self):
        while True:
            self.collect_user_data()
            asking = input('Would You Like To Add Another Person:')
            if asking == 'yes':
                continue
            elif asking == 'no':
                break

        all_persons = self.persons
        for person in all_persons:
            print(person.print_info())

bmi_instance = BMIApp()
bmi_instance.run()



