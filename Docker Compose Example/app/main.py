import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"))

st.title("Simple LLM Chatbot")
prompt = st.text_area("Enter your prompt here:", "Explain how transformers work.")
if st.button("Send"):
    with st.spinner("Generating response..."):
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
        try:
            # Create a chat completion request
            response = client.chat.completions.create(
                model=os.getenv("MODEL"),
                messages=messages
            )
            st.success("Response generated successfully!")
            st.write(response.choices[0].message.content)  # Display the response content
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.stop()