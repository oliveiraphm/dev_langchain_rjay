from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

template = "What is the capital of {country}?"
prompt = PromptTemplate(template=template, input_variables=["country"])

llm = OpenAI(openai_api_key=api_key, temperature=0.9)

chain = LLMChain(llm=llm, prompt=prompt)

result = chain.invoke("France")
print(result)