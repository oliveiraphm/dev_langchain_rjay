from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

from dotenv import load_dotenv 
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
loader = TextLoader("your_data.txt")
documents = loader.load()

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)
llm = ChatOpenAI(api_key=api_key, model="gpt-3.5-turbo")

qa_chain = RetrievalQA.from_chain_type(
    llm = llm,
    chain_type = "stuff",
    retriever=vectorstore.as_retriever()
)

query = "What is the name of the character?"
result = qa_chain.invoke({"query": query})
print("Q&A Response:", result['result'])