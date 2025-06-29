from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


loader = TextLoader("meus_documentos.txt")
docs = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
documents = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(openai_api_key=api_key)
db = FAISS.from_documents(documents, embeddings)
retriever = db.as_retriever()

llm = ChatOpenAI(temperature=0, openai_api_key=api_key)
compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_retriever=retriever,
    base_compressor=compressor
)

qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=compression_retriever)

chat_history = []
print("Start a conversation with the assistant. Type 'exit' to quit.")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    result = qa_chain({"question": user_input, "chat_history": chat_history})
    chat_history.append((user_input, result['answer']))
    print(f"Assistant: {result['answer']}")