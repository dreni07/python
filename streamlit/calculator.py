import streamlit as st

def calculate(num1,num2,operator):
    the_result = None
    if operator == 'addition':
        the_result = num1 + num2
    elif operator == 'substraction':
        the_result = num1 * num2
    elif operator == 'multiplication':
        the_result = num1 * num2
    elif operator == 'divison':
        try:
            the_result = num1 / num2
        except ZeroDivisionError:
            the_result = 'Cannot Divide By Zero'
    else:
        the_result = 'Enter Valid Operator'

    return the_result


def main():
    st.title('Calculator App')
    number1 = st.number_input('Enter First Number',step=1)
    number2 = st.number_input('Enter Second Number',step=1)# step means by how much
    # the number is going to grow
    operation = st.radio('Choose Operation',['addition','substraction','multiplication','division'])
    if st.button('Calc'):
        the_result = calculate(number1,number2,operation)
        st.write(the_result)

if __name__ == '__main__':
    main()