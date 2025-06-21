import os 
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_completion(user_prompt):

    from openai import ChatCompletion
    response = ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model
        messages=[{"role": "user", "content": user_prompt}]
    )
    return response.choices[0].message.content.strip()

user_prompt = input("Enter a story prompt: ")

result = get_chat_completion(user_prompt)

print("Generated Response:", result)