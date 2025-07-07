from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

prompt_template = PromptTemplate(
    input_variables = ["product"],
    template = "What are teh benefits of {product}?",
)

llm = OpenAI(temperature=0.9)

chain = LLMChain(llm=llm, prompt=prompt_template)

product_name = "Customer Service Chatbot"
response = chain.run(product_name)

print("Chain Response:")
print(response)