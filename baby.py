import streamlit as st
import pickle
st.title("Survey")
st.header("Enter your details")

name =st.text_input("Name")
sex= st.radio("Female/Male",[0,1])
age= st.number_input("Age")

clicked=st.button("Submit Data")
if clicked==True:
    st.title("Dan, everytime i think about you ,i feel butterflies all over again. Everyday i am reminded of the ways you have transformed my life in the best possible way.The way you understand me, support me, and stand by my side whenever i need you makes me realise how fortunate i am to have found you.You illuminate even the darkest corners of my life. I am infinitely grateful for the privilege of loving you. Thank you for everything! Happy 5 months baby <3I am excited about what awaits us and the new memories waiting to be created. I love u so much")
