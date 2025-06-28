from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

examples = [
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the currency of Japan?", "answer": "Japanese yen"},
]

example_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template="Question: {question}\nAnswer: {answer}"
)

prompt_without_selector = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)

example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50
)

prompt_with_selector = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)

llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key, temperature=0.7)

print("Prompt Template without Example Selector:")
print(prompt_without_selector.format(input="What is the capital of Australia?"))

print("\nGenerated Answer:")
print(llm(prompt_without_selector.format(input="What is the capital of Australia?")))

print("\nPrompt Template with Example Selector:")
print(prompt_with_selector.format(input="Who sculpted the Statue of David?"))

print("\nGenerated Answer:")
print(llm(prompt_with_selector.format(input="Who sculpted the Statue of David?")))