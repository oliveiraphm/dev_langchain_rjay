from langchain.chains.loading import load_chain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chain = load_chain("./Chapter 06 example2.yaml")

result = chain.invoke({"country": "France"})

print(result)