from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path="california_housing_test.csv")
data = loader.load()

for row in data:
    print(f"Content: {row.page_content}\n")
    print(f"Metadata: {row.metadata}\n")
    print("---")

custom_loader = CSVLoader(
    file_path="california_housing_test.csv",
    csv_args={"delimiter": ",", "quotechar": '"', "fieldnames": ["Team", "Payroll", "Wins"]}
)
custom_data = custom_loader.load()
print(custom_data)