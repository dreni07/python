# Shkolla Digitale Class as a Super Class
class DigitalSchool:
    def __init__(self,name,city,state,courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self._courses = courses
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
    def school_info(self):
        school_i = {
            'name':self.__name,
            'city':self.__city,
            'state':self.__state,
            'courses':self.__courses
        }

        return school_i

    def admin_part(self):
        password = 'drenllazani'
        admin_check = input('If You Are Admin Enter Password: ').lower()
        if admin_check == password:
            print(self._students)

class Register(DigitalSchool):
    def see_courses(self):
        user_input = input('Want To Watch Our Courses And Decide? ').lower()
        if user_input == 'yes':
            print(self._courses)
            get_answer = input('Please Decide Now: ')
            get_actual_course = self._courses[get_answer]
            print('Congrats You Choose The Course', get_actual_course)
            asking = input('Want To Get Registered Now? :').lower()
            if asking == 'yes':
                self.register_to_course(get_answer)
    def register_to_course(self,course_name):
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
            'course': self._courses[course_name]
        }
        self.admin_part()


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

digital_school = Register('Shkolla Digjitale','Prishtine','Kosovo',school_courses)
digital_school.see_courses()

