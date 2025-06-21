from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class technical documentation writer."),
    ("user", "{input}")
])

chain = LLMChain(llm=llm, prompt=prompt)

result = chain.invoke("Explain the concept of recursion in programming.")
print("Generated Response:", result)