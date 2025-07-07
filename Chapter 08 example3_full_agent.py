import openai
from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

chat_model = ChatOpenAI(model_name="gpt-4", temperature=0)

tools = load_tools(["serpapi", "llm-math"], llm=chat_model)

agent = initialize_agent(tools, chat_model, agent="zero-shot-react-description", verbose=True)

query = (
    "A software company is planning to develop a new mobile app. They estimate that the initial development cost "
    "will be $200,000, and the app will generate a monthly revenue of $15,000. The company wants to know how many "
    "months it will take to break even on their investment, assuming a monthly maintenance cost of $5,000. Can you "
    "help calculate the breakeven point?"
)
response = agent.run(query)

print("Agent Response:")
print(response)