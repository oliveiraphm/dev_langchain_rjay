import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

st.title("ChatGPT-like Q&A App")
st.subheader("Interact with an AI to answer your questions.")

user_query = st.text_input("Enter your question:")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if st.session_state['chat_history']:
    st.markdown("### Chat History")
    for chat in st.session_state['chat_history']:
        st.write(f"**Q:** {chat['question']}")
        st.write(f"**A:** {chat['answer']}")
        st.write("---")

if user_query and st.button("Submit"):
    llm  = ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo')

    prompt = ChatPromptTemplate.from_messages([
       HumanMessagePromptTemplate.from_template("{query}")
       ])
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(query=user_query)

    st.session_state['chat_history'].append({"question": 
    user_query, "answer": response})
    st.write("Answer:")
    st.write(response)
else:
    st.write("Please enter a question and click Submit.")