# Streamlit App 
from google import genai 
import os 
from dotenv import load_dotenv
import streamlit as st 

# create .env file and put your API key, otherwise it will not works!
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = "gemini-3-flash-preview",
    contents = "Give me an idea of Gemini API in 50 words"
)

st.markdown(response.text)