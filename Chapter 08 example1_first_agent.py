from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
serpapi = os.getenv("SERPAPI_API_KEY")
tools = load_tools(["serpapi"], llm=OpenAI(temperature=0))
#tools = load_tools(["serpapi", "llm-math"], llm=OpenAI(temperature=0))

prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Generate an engaging article about {topic}."
)

agent = initialize_agent(tools, OpenAI(temperature=0), agent="zero-shot-react-description", verbose=True)

user_prompt = "What is the revenue increase due to teh benefits of AI"
response = agent.run(prompt_template.format(topic=user_prompt))

print("Agent Response:")
print(response)