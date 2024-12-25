from dotenv import load_dotenv
load_dotenv()                    # Loading all the Environment variable.

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini_Pro model to Get response from user Query
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
        return response.text
    else:
        response = model.generate_content(image)
        return response.text
    
# initialize our streamlit App
st.set_page_config(page_title="Gemini Image DEMO")
st.header("GEMINI LLM Application")
input = st.text_input("Input Prompt :")
upload_file = st.file_uploader("Choose an Image File...", type=['jpg','jpeg','png'])
image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image,caption="Uploaded Image", use_container_width= True)

submit= st.button("Tell about the image")
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response is :")
    st.write(response)