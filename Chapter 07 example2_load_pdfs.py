from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("1738080077503.pdf")


pages = loader.load_and_split()

print(f"Number of pages: {len(pages)}")
print(f"Content of the first page: {pages[0].page_content}")
print(f"Metadata of the 11th page: {pages[10].metadata}")
print(f"Characters in the first page: {len(pages[0].page_content)}")