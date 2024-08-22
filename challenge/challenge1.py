# Shkolla Digitale Class as a Super Class
class DigitalSchool:
    def __init__(self,name,city,state,courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self.__courses = courses

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

    @property
    def get_courses(self):
        return self.__courses

    @get_courses.setter
    def get_courses(self,new_courses):
        self.__courses = new_courses

    # school info in an dictionarie
    def school_info(self):
        school_i = {
            'name':self.__name,
            'city':self.__city,
            'state':self.__state,
            'courses':self.__courses

        }

        return school_i

    def see_courses(self):
        user_input = input('Want To Watch Our Courses And Decide? ').lower()
        if user_input == 'yes':
            print(self.__courses)
            get_answer = input('Please Decide Now: ')
            get_actual_course = self.__courses[get_answer]
            print('Congrats You Choose The Course',get_actual_course)


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

digital_school = DigitalSchool('Shkolla Digjitale','Prishtine','Kosovo',school_courses)
digital_school.see_courses()
