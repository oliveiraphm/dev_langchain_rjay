from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


llm = OpenAI(openai_api_key=api_key)


topic_prompt = PromptTemplate(
    template="Generate relevant keywords for the topic: {topic}",
    input_variables=["topic"]
)
topic_chain = LLMChain(
    llm=llm,
    prompt=topic_prompt,
    output_key="keywords"
)


data_prompt = PromptTemplate(
    template="Fetch data related to the following keywords: {keywords}",
    input_variables=["keywords"]
)
data_chain = LLMChain(
    llm=llm,
    prompt=data_prompt,
    output_key="data"
)

summary_prompt = PromptTemplate(
    template="Summarize the following data: {data}",
    input_variables=["data"]
)
summary_chain = LLMChain(
    llm=llm,
    prompt=summary_prompt,
    output_key="summary"
)

sequential_chain = SequentialChain(
    chains=[topic_chain, data_chain, summary_chain],
    input_variables=["topic"],
    output_variables=["summary"],
    verbose=True
)

topic = "Artificial Intelligence"
result = sequential_chain({"topic": topic})
print("\nResumo final:\n", result["summary"])