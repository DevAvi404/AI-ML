import streamlit as st

# title
st.set_page_config(page_title="Calculator", layout="centered")

with st.container():
    st.title("📱 Basic Calculator")

# markdoen
st.markdown("### Enter Values")

# colums
col1, col2, col3 = st.columns([4,1,4], gap="medium")

# input numbers
with col1:
    num1 = st.number_input("", placeholder="First Number", value=None)

with col2:
    # operation
    operation = st.selectbox(
        "",
        ["+", "-", "*", "/"]
    )

with col3:
    num2 = st.number_input("", placeholder="Second Number", value=None)

# calculate button
if st.button("Calculate", use_container_width=True):

    if num1 is None or num2 is None:
        st.write("Please Enter Both Numbers")

    else:
        # summation
        if operation == "+":
            result = num1 + num2

        # subtraction 
        elif operation == "-":
            result = num1 - num2
        
        # multiplication
        elif operation == "*":
            result = num1 * num2
        
        # divition 
        if operation == "/" and num2 == 0:
            
            st.error("Cannot Divided by Zero")
            result = None
        else:
            result = num1 / num2

        if result is not None:
            st.success(f"Result: {result}")