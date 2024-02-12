from langchain_openai import OpenAI
from dotenv import load_dotenv 
import streamlit as st
import os

# Load environment variables from .env file
load_dotenv()

def get_openai_response(question):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    llm = OpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    #llm = OpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo-0613", temperature=0.5)
    response = llm(question)
    return response

# Initializing the Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

# User input field
input_question = st.text_input("Input:", key="input")

# Button for submitting the question
submit = st.button("Ask the question")

# Handling button click
if submit and input_question:
    response = get_openai_response(input_question)
    st.subheader("The response is:")
    st.write(response)
elif submit and not input_question:
    st.warning("Please enter a question before submitting.") 
