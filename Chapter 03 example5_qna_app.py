from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv 
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

output_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a wellness expert."),
    ("user", "{input}")
])

llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")
chain = prompt | llm | output_parser

output  = chain.invoke({"input" : "What are the benefits of walking a mile a day?"})
print("Wellness Q&A: ", output)
