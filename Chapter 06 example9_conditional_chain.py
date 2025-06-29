from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=api_key)


positive_prompt = PromptTemplate(
    template="Respond positively to the following query: {query}", input_variables=["query"]
)
positive_chain = LLMChain(llm=llm, prompt=positive_prompt)

negative_prompt = PromptTemplate(
    template="Respond cautiously to the following query: {query}", input_variables=["query"]
)
negative_chain = LLMChain(llm=llm, prompt=negative_prompt)


sentiment_prompt = PromptTemplate(
    template="Classify the sentiment of this query as 'positive' or 'negative': {query}",
    input_variables=["query"]
)
sentiment_chain = LLMChain(llm=llm, prompt=sentiment_prompt)


def route_query_by_sentiment(query: str) -> str:
    sentiment = sentiment_chain.run({"query": query}).strip().lower()
    print(f"[DEBUG] Detected sentiment: {sentiment}")

    if "positive" in sentiment:
        return positive_chain.run({"query": query})
    elif "negative" in sentiment:
        return negative_chain.run({"query": query})
    else:
        return "Sentimento não identificado."


query = "I love your product!"
response = route_query_by_sentiment(query)
print("\nResposta:\n", response)