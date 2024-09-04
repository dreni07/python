import streamlit as st
if st.button('Click Me!'):
    st.write('Hello')

user_input = st.text_input('Enter a text')
if user_input:
    st.write('Hello ' + user_input)

age = st.number_input('Enter Your Age', min_value=1, max_value=100)
if age:
    st.write('Your Age Is: ', age)

the_area = st.text_area('Enter Details...')

if the_area:
    st.write(f'Details: {the_area}')

# RADIO Buttons
choice = st.radio('Best Club?:', ['Real Madrid', 'Barcelona'])
if choice == 'Real Madrid':
    st.write('Great')
else:
    st.write('Wrong')

if st.button("Clicked"):
    st.success('Operation Was Completed \n')

try:
    1/0
except Exception as e:
    print('Error ' + str(e))