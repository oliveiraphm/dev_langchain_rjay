from langchain import hub
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

tools = [TavilySearchResults(max_results=1)]

# Carrega o prompt corretamente do LangChain Hub
prompt = hub.pull("hwchase17/structured-chat-agent")

# Define o modelo LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

# Cria o agente estruturado
agent = create_structured_chat_agent(llm=llm, tools=tools, prompt=prompt)

# Cria o executor de agente
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Executa
response = agent_executor.invoke({
    "input": "What are the best ways to reduce operational costs?"
})

print(response)