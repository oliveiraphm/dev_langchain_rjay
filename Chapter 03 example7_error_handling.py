from langchain_openai import ChatOpenAI
from openai import OpenAI
from openai import APIError, AuthenticationError, RateLimitError
from dotenv import load_dotenv 
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")

try:
    response = llm.invoke("Hello, how are you?")
    print("Response:", response)
except AuthenticationError as e:
    print("Rate limit exceeded. Try again later.")
except APIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Operation completed.")