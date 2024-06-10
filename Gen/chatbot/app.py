import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from a .env file
load_dotenv()

# Set environment variables directly if they are not set in the .env file
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "Your openai Api Key")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "Your langchain Api key")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Debug: Print environment variables to ensure they are set correctly
# st.write(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")
# st.write(f"LANGCHAIN_API_KEY: {os.getenv('LANGCHAIN_API_KEY')}")

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit app
st.title('Personalized AI ChatBot')
input_text = st.text_input("Search the topic you want")

# Debug: Print input text to ensure it's being captured
st.write(f"Input text: {input_text}")

# LLM setup
llm = ChatOpenAI(model="gpt-3.5-turbo")
outputparser = StrOutputParser()
chain = prompt | llm | outputparser

# Process input and display output
if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)
