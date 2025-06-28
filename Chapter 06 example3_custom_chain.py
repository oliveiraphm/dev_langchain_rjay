from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=api_key, temperature=0.9)

# Define the prompt template
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?"
)

# Create the custom chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.run("smartphone")
print(result)