from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv 
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo", temperature=0)

def generate_response(text):
    messages = [HumanMessage(content=text)]
    response = chat_model.invoke(messages)
    return response.content

while True:
    user_input = input("Enter a message (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    print("AI:", generate_response(user_input))