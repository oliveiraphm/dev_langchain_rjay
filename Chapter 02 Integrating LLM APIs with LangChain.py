from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")

prompt_template = PromptTemplate(
    input_variables = ["user_input"],
    template = "You are a helpful chatbot. User: {user_input} Response:"
)

chain = prompt_template | llm

user_prompt = input("Enter another story prompt: ")

response = chain.invoke(user_prompt)
print("Generated LangChain Response:", response)