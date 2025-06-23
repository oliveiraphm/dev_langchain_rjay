from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

from dotenv import load_dotenv 
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

prompt_template = PromptTemplate(
    input_variables = ["algorithm", "language"],
    template = """You are a seasoned software engineer. 
    Explain the following algorithm: {algorithm} in {language}.
    Describe its purpose, time complexity, and a common use case."""
)

llm = OpenAI(openai_api_key=api_key, temperature=0.7)

chain = LLMChain(llm=llm, prompt=prompt_template)

response = chain.run(algorithm="machine learning", language="French")
print(response)