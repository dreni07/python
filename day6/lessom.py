string_length = len("hello world")
list_length = len([1,2,3,4,5])
tupel_length = len((1,2,3,4,5))
print(string_length)
print(list_length)
print(tupel_length)

def add(x,y):
    return x+y

def contatinate(x,y):
    return str(x) + str(y)

def operate(operation,x,y):
    return operation(x,y)

print(operate(add,5,6))
print(operate(contatinate,2,22))

