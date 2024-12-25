from dotenv import load_dotenv
load_dotenv()                    # Loading all the Environment variable.

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini_Pro model to Get response from user Query
model = genai.GenerativeModel()
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# initialize our streamlit App
st.set_page_config(page_title="Question & Answer DEMO")
st.header("GEMINI LLM Application")
input = st.text_input("Ask the Question :")
submit= st.button("Ask the Question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is :")
    st.write(response)