from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the Google Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Model and get responses
model = genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemeni_response(question):
    response = chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Gemini QA Chatbot")

st.header("Gemini Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask your query")

if submit and input:
    response=get_gemeni_response(input)
    st.session_state['chat_history'].append(("You",input))
    st.subheader("Response:")
    for chunk in response: #Because we wrote stream=True
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))

    st.subheader("The Chat history is:")

for role,message in st.session_state['chat_history']:
    
    st.write(f"{role}: {message}")




