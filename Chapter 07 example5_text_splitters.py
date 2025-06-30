from langchain_text_splitters import CharacterTextSplitter

with open("The Art of Money Getting.txt") as f:
    document = f.read()

text_splitter = CharacterTextSplitter(
    separator="\n\n", chunk_size=1000, chunk_overlap=200, length_function=len
)

chunks = text_splitter.create_documents([document])

print(chunks[4])