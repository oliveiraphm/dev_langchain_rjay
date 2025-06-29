from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


loader = TextLoader("meus_documentos.txt")
documents = loader.load()

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
split_docs = splitter.split_documents(documents)


llm = OpenAI(temperature=0.9, openai_api_key=api_key)

chain = load_summarize_chain(llm, chain_type="map_reduce")

result = chain.run(split_docs)

print(result)