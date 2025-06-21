from langchain_core.language_models import BaseLLM
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv 
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")

response = llm.invoke("Tell me a joke about programming.")
print("LangChain Core Response:", response.content)