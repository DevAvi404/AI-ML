import streamlit as st

st.title("My First Streamlit Project", anchor=False)

st.header("Contect 1", divider=True)
st.subheader("Content 1 Sub Header")

st.text("Hello World!")

st.markdown(":red[**Hello**] *world*")
st.markdown(":red-background[:green[**Hello**] *world*🌍]")