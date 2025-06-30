from langchain_community.document_loaders import TextLoader

loader = TextLoader("meus_documentos.txt")

documents = loader.load()

for doc in documents:
    print(f"Content: {doc.page_content}\n")
    print(f"Metadata: {doc.metadata}\n")
    print("---")