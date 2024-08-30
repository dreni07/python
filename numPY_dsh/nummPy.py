import numpy as np
first_array = np.array([[1,2,3],[4,5,6]])
print(first_array[:2,:2])## two arrays and the first two elements
print(first_array[:1,:1])## only the first element

second_array = np.array([[1,2,3],[5,6,7],[8,9,10]])
print(second_array[1:3,:2]) # print only the second and third array
## ignore the first array
# and print only the two elements in them
the_sum = second_array.sum()
print(the_sum) # tells the sum of all the elements
sum_of = second_array[:2,:2].sum() # the sum of only the two first elements of the two first arrays
last_array_sum = second_array[2:3].sum() # sum of the last array
print(last_array_sum)
print(sum_of)
the_mean = second_array.mean()
print(round(the_mean,2))

print(second_array.ndim) # 2d array
print(second_array.shape) # the shape of the array rows and columns

# take the sum of the same index of each array
the_sum_index = np.sum(second_array,axis=0)
print(the_sum_index)
# print the sum of each array
the_sum_each = np.sum(second_array,axis=1)
print(the_sum_each)

last_array = np.array([['5','4','9','6','20']])
get_all = last_array[:1]

print(get_all)
for element in get_all:
    for second_element in element:
        if type(second_element) != int:
            second_element = int(second_element)
            print(type(second_element),second_element)


average_student_grade = np.array([[5,5,5,5,5,5,5,5,5,5,5,5,5,5],[4,4,3,4,5,2,3,5,5,5,5,5,5,4],[2,2,3,4,3,3,3,5,5,4,5,5,5,5],[5,5,5,5,5,5,5,5,5,5,5,5,5,5],[5,5,5,3,5,2,5,3,5,5,4,4,4,5]])
people_average = np.array([['Dren'],['Rion'],['Ylli'],['Leon'],['Elton']])
for i in range(len(average_student_grade)):
    with open('myAverage.txt','a') as file:
        file.write(f'{people_average[i][0]} {average_student_grade[i].mean()} \n')

my_str = [['DRENI']]