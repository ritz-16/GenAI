from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the Google Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(prompt):
    # Generate content using the Gemini Pro model
    response = model.generate_content(prompt)
    try:
        text = response.candidates[0].content.parts[0].text
        return text
    except (IndexError, AttributeError) as e:
        return f"Error accessing the response text: {e}"

# Initialize our Streamlit app
st.set_page_config(page_title="My Chat GPT")
st.header("Gemini LLM Applications")

input = st.text_input("Input : ", key="input")
submit = st.button("Enter your query")

# When the user submits their query
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is : ")
    st.write(response)
