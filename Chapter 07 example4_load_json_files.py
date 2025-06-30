from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="products.json",
    jq_schema=".products[]",
    text_content=False
)
data = loader.load()

# Print loaded data
for item in data:
    print(f"Content: {item.page_content}\n")
    print(f"Metadata: {item.metadata}\n")
    print("---")

# Working with JSON Lines
#jsonl_loader = JSONLoader(
#    file_path="products.json",
#    jq_schema=".content",
#    text_content=False,
#    json_lines=True
#)
#json_data = jsonl_loader.load()
print(data)