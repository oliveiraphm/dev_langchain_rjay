from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

tools = load_tools(["serpapi", "llm-math"], llm=OpenAI(temperature=0))

agent = initialize_agent(tools, OpenAI(temperature=0), agent="zero-shot-react-description", verbose=True)

query = "What is the capital of France? What is the population of that city?"
response = agent.run(query)
print(response)