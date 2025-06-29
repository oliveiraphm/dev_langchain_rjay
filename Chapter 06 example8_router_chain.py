from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=api_key)


sales_prompt = PromptTemplate(
    template="Respond to this sales-related query: {input}", input_variables=["input"]
)
support_prompt = PromptTemplate(
    template="Respond to this support-related query: {input}", input_variables=["input"]
)

sales_chain = LLMChain(llm=llm, prompt=sales_prompt)
support_chain = LLMChain(llm=llm, prompt=support_prompt)

def route_query(query: str) -> str:
    query_lower = query.lower()
    if any(word in query_lower for word in ["price", "buy", "purchase", "quote", "plan"]):
        return sales_chain.run(query)
    elif any(word in query_lower for word in ["help", "bug", "issue", "problem", "error", "support"]):
        return support_chain.run(query)
    else:
        return "I'm not sure how to handle this query."


query = "I need help with a bug in the app"
response = route_query(query)
print("\nResposta:\n", response)