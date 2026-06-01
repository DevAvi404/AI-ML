import streamlit as st

st.title("Basic I/O section.", anchor=False)
st.divider()
st.header("Input your information", divider=True)

# name
name = st.text_input("Enter your name", placeholder="Type your name...")
st.divider()
# age
age = st.number_input("Enter your age", value=None, placeholder="Type your age...")
st.divider()
# select profession
preofession = st.selectbox("Choose your profession",
             ("Student", "Employee", "Businessman"),
             index=None, placeholder="Choess an option",
             accept_new_options=True
             )
# mail
email = st.text_input("Enter your mail", placeholder="Type your mail...")
st.divider()
# password
password = st.text_input("Enter your password", type="password")
# submit
pressed = st.button("Submit", type="primary")

if pressed:
    st.write("Your name is: ", name)
    st.write("Your age is: ", age)
    st.write("Your mail is: ", email)
    st.write("Your profession is: ", preofession)
