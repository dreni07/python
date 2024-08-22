# Shkolla Digitale Class as a Super Class
# question for quiz
questions = {
    'question1':'What CPU stands for?',
    'question2':'What GPU stands for?',
    'question3':'What HTML stands for? '
}

# answers for quiz
answers = {
    'answer1':'central processing unit',
    'answer2':'graphic processing unit',
    'answer3':'hypertext markup language'
}


question_list = list(questions.items()) # []
answers_list = list(answers.items())

# the class below is the superclass
class DigitalSchool:
    def __init__(self,name,city,state,courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self._courses = courses
        self._password = 'drenllazani'
        self._students = {}

    # we use the decorator property
    # and then then a get method to get any private property that we have
    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self,new_name):
        self.__name = new_name

    @property
    def get_city(self):
        return self.__city

    @get_city.setter
    def get_city(self,new_city):
        self.__city = new_city

    @property
    def get_state(self):
        return self.__state

    @get_state.setter
    def get_state(self,new_state):
        self.__state = new_state


    # school info in an dictionarie
    # all are methods to be overwriten in the subclass
    def _try_schoolarship(self):
        pass
    def register_to_course(self):
        pass
    def see_courses(self):
        pass
    def organize_hackathon(self):
        pass
    def school_info(self):
        school_i = {
            'name':self.__name,
            'city':self.__city,
            'state':self.__state,
            'courses':self._courses
        }

        return school_i

    def admin_part(self):
        admin_check = input('If You Are Admin Enter Password: ').lower()
        if admin_check == self._password:
            print(self._students)

# this is the subclass
class Register(DigitalSchool):
    # overwriten method
    def see_courses(self):
        user_input = input('Want To Watch Our Courses And Decide? ').lower()
        if user_input == 'yes':
            print(self._courses)
            get_answer = input('Please Decide Now: ').lower()
            while get_answer not in self._courses:
                get_answer = input('Enter Again Invalid Course: ').lower()
            get_actual_course = self._courses[get_answer]
            print('Congrats You Choose The Course', get_actual_course)
            asking = input('Want To Try Schoolarship?: ').lower()
            if asking == 'yes':
                self._try_scholarship(get_answer)

    #overwriten method
    def register_to_course(self,course_name):
        with_schoolarship = False
        user_name = input('Enter Your Name:')
        user_email = input('Enter Your Email:')
        user_phone = input('Enter Your Phone Number:')
        into_keys = list(self._students.keys())
        if len(into_keys) == 0:
            the_index = 0
        else:
            the_index = into_keys[len(into_keys) + 1]


        self._students[the_index] = {
            'name': user_name,
            'email': user_email,
            'phone_number': user_phone,
            'course': self._courses[course_name],
            'schoolarship':with_schoolarship
        }
        self.admin_part()


    # overwriten method
    def _try_scholarship(self,get_answer):
        right = 0
        wrong_ones = []
        info = input('You Have 3 Question If You Get All Of Them Right You Win The Schoolarship')
        for i in range(len(question_list)):
            question = input(question_list[i][1])
            if question == answers_list[i][1]:
                right += 1
            else:
                wrong_ones.append(question_list[i][1])
        print('You Finished Your Quiz With', right, 'Answers Right')
        if len(wrong_ones) > 0:
            for wrong_answer in wrong_ones:
                print(f'You Got Wrong " {wrong_answer} " ')
            print('So Sorry You Didnt Win Anyway Register There ')
            self.register_to_course(get_answer)

        else:
            print(f'Which Means 0 Wrong And You WIN THE SCHOOLARSHIPPPP for the course {get_answer}')
            self.register_to_course(get_answer)

    # this method below is organize_hackathon() which is an method writen
    # in superclass and now getting overwriten in subclass
    hack_members = {}
    def organize_hackathon(self):
        asking = input('Do you want to be part of our hackathon: ')
        if asking == 'yes':
            your_name = input('Enter Your Name?: ')
            your_email = input('We Need Your Email To Inform You: ')
            if your_name not in self.hack_members:
                self.hack_members[your_name] = your_email
            print('Thank You!!')






# DIGITAL SCHOOL SCHOOL COURSES
school_courses = {
    'Basic Level':{
        'Web':{
            'first_level':'HTML & CSS BASIC',
            'second_level':'JS BASIC'
        },
        'Python':'Python Basics'
    },
    'Advance Levels':{
        'Levels':{
            'first_level':'HTML&CSS&JS',
            'second_level':'PHP & MYSQL',
            'third_level':'WORDPRESS',
            'forth_level':'PYTHON',
            'last_level':'APP DEVELOPMENT WITH REACT NATIVE'
        }
    }
}
# AN INSTANCE OF THE SUBCLASS
digital_school = Register('Shkolla Digjitale','Prishtine','Kosovo',school_courses)
# digital_school.see_courses()
# digital_school.see_courses()



