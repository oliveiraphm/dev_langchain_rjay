from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv 
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(temperature=0, openai_api_key=api_key)
template = """
You are an enthusiastic assistant that rewrites the user's text to sound more exciting.

User: {text}
Assistant:
"""

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are an enthusiastic assistant that rewrites the user's text to sound more exciting."
    ),
    HumanMessagePromptTemplate.from_template("{text}"),
])

user_input = input("Enter some text: ")

formatted_prompt = prompt.format_prompt(text=user_input)

print("\nFormatted Prompt:")
print(formatted_prompt.to_messages())

response = chat(formatted_prompt.to_messages())
print("\nAssistant's Response:")
print(response.content)