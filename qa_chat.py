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

st.set_page_config


