import asyncio
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=api_key, temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?"
)

chain = LLMChain(llm=llm, prompt=prompt)

async def generate_names(product):
    return await chain.arun({"product": product})

products = ["smartphone", "laptop", "smartwatch"]

async def main():
    results = await asyncio.gather(*(generate_names(product) for product in products))
    for product, name in zip(products, results):
        print(f"Product: {product}, Name: {name}")

# Agora chamamos a coroutine corretamente
asyncio.run(main())