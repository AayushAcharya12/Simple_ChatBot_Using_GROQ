import streamlit as st
from langchain_groq import ChatGroq
from langchain_classic.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

#Getting the GROQ API key
groq_api=os.getenv('GROQ_API')

#getting our llm model
llm=ChatGroq(model='llama-3.1-8b-instant',temperature=1,groq_api_key=groq_api)
st.title('Simple Q&A Chatbot Using GROQ 🤖')

input=st.text_input("Enter The Question.",placeholder="What is Machine Learning?")

if st.button("Submit"):
    prompt=ChatPromptTemplate.from_messages([
        ("system","""You are a helpful, knowledgeable, and friendly AI assistant. Provide accurate, concise, and easy-to-understand answers. 
         Explain complex concepts simply, use examples when helpful, and ask for clarification if the question is ambiguous. If you don't know something, admit it honestly rather than making up information."""),
        ("human",'{question}')
    ])
    chain=prompt|llm
    answer=chain.invoke({'question':input})
    st.write(answer.content)