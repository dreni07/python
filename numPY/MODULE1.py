import numpy as np
#2d array
# creating 2d array with numpy library
array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2d)
print(array_2d[1,1])#print a specific element in a 2d array

print(array_2d.ndim) # show how many dimensions an array has

print(array_2d.shape) # show the columns and the rows of the array
# like 3x3 array for example

print(array_2d.size) # total number of elements

array_sub = array_2d[:2,:2]
print(array_sub)
first_row = array_2d[:1]
print(first_row)

reverse_array = array_2d[-2:,-2:]
print(reverse_array)

# dsh find other manipulation with numpy

shuma = np.sum(array_2d)
print(shuma)
shuma2 = np.sum(array_2d[:1])
print(shuma2)

mean = np.mean(array_2d)
print(mean)

shuma3 = np.sum(array_2d,axis=0) # what this is doing is going to sum up the element with same index in the three
print(shuma3)

# if axis is equal to 0 we go and sum up the first element of the first array with the other first elements
# of other arrays
# and if axis is equal to 1 we go and find the sum of each array

# pandat kane dy data structures:series,dataframes
# series-array 1D
# data frames-
# me panda munem me marr ni dataset prej databazes ose prej ndonnje file te caktum
