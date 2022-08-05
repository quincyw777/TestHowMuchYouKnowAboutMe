import streamlit as st
from PIL import Image


st.title('Test how much you know about me?')
image = Image.open('laugh.jpg')
image2 = Image.open('dog.jpg')
score = 0
name = st.text_input("Enter Your name", "")
button1 = st.button('Submit')
if button1:
    #result = name.title()
    st.write("Hello", name, "!!!")
status = st.selectbox("Are you ready?", ('Make a selection','Yes', 'No'))
if status == 'No':
    st.error('Ok...See you next time.')
if status == 'Yes':
    st.image(image, caption='jajajajaja', width=500)
    st.write('Question 1:')
    birthday = st.selectbox('My birthday month:', ('Make a selection', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    st.write('You selected', birthday, '!')
    if birthday == 'Jan':
        score +=1
    else:
        score +=0
    st.write('Question 2:')
    personality = st.radio("How do I describe myself:", ('sunshine boy', 'hardworker', 'talented guy', 'extremely handsome'))
    if personality == 'sunshine boy' or personality == 'talented guy':
        score += 1
    else: 
        score += 0
    st.write('Question 3:')
    weight = st.radio('My weight is:', ('less than 90lb', '90-110lb', '110-130lb', '130-150lb', '150-170lb', 'more than 170lb' ))
    st.write('You selected',weight, "!")
    if weight == '130-150lb':
        score +=1
    else:
        score +=0
    st.write('Question 4:')
    car = st.radio('My dream car brand:', ('Mercedes', 'BMW', 'Porsche', 'Bentley', 'Ferrari', 'Lamborghini'))
    st.write('You selected', car, "!")
    if car == "Ferrari":
        score +=1
    else: 
        score +=0
    st.write("Question 5:")
    color = st.multiselect('Choose my TWO favourite colors:', ['Yellow', 'Green', 'Red', 'Blue', 'Purple', 'White', 'Pink'])
    if len(color) == 1:
        st.write('Please select one more color!')
    else:
        st.write("You selected", len(color), 'colors.')
    if color == ['Red', 'Blue'] or color == ['Red', 'Green']:
        score+=1
    else:
        score+=0
    button2 = st.button('All done!! Click her to view your score!')
    if button2:
        st.image(image2, width=400)
        st.write('Congratulations!!! Your score is:', score*20, '!')
   

        


       
           

        

