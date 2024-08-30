# create some data
# save them in a file
# and after that
# display them using series
import pandas as pd
school_students = {
    'DREN':[5,5,5,5,5,5,5],
    'DIOR':[5,5,5,5,5,5,5],
    'OLT':[4,4,4,5,3,4,5],
    'DRITERO':[4,5,5,5,5,5,5]
}

into_list = list(school_students.items())
for i in range(len(into_list)):
    get_grades = into_list[i][1]
    average_grade = 0
    for grade in get_grades:
        average_grade += grade
    average_grade = (average_grade / len(get_grades))
    with open('students.txt','r+') as f:
        get_lines = f.read()
        if into_list[i][0] not in get_lines:
            f.write(f'Student: {into_list[i][0]} Average Grade {round(average_grade,2)} \n')

# now display them with series

into_list_keys = list(school_students.keys())
into_list_values = list(school_students.values())
#full grades
displaying = pd.Series(into_list_values,index=into_list_keys)
print(displaying)

# data frames

data_frames = {
    'Usernames':['Dren','Dior','Yll'],
    'Emails':['drenllazani10@gmail.com','diormustafa@gmail.com','yllkelmendi@gmail.com'],
    'Passwords':['ineidehhtdephgn2efep4','deionsugenaiyefogne5','ufeogeinaovbn8']
}

dframes = pd.DataFrame(data_frames)
print(dframes)




