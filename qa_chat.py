from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini_Pro model to Get response from user Query
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_response(question):
    response = chat.send_message(question,stream=True)
    return response

# initialize our streamlit App
st.set_page_config(page_title="Q & A Demo")
st.header("Gemini LLM Application")

#Initialize When Chat Histoyr is doesn't Exist.!
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input", key = 'input')
submit = st.button("Ask the question")

if submit and input:
    response = get_response(input)
    # Add user Query and Bot response Save in chat session history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is :")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History: ")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
