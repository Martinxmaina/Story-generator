import streamlit as st
import os
from mistralai import Mistral
from langchain import PromptTemplate
import warnings
warnings.filterwarnings("ignore")

st.title("Story Generator")
st.divider()

api_key = "xLioy62rKxl4M6IsqQKGBNG8tKdXpxYK" 
model = "mistral-small-latest"
client = Mistral(api_key=api_key)

topic=st.text_input("Enter a topic and the story will be generated using Mistral AI.")

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Write a short story about {topic}",
)

# Get the prompt from the template
prompt = prompt_template.format(topic=topic)
st.divider()
# Use the prompt with Mistral AI
if
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt, 
            },
        ]
    )
    st.write(chat_response.choices[0].message.content)
