from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

def search_knowledge_base(query: str) -> str:
    if "password reset" in query.lower():
        return "To reset your password, follow these steps: ..."
    return "No specific answer found. Contact support for assistance."

tools = [Tool(name="Knowledge Base Search", func=search_knowledge_base, description="Search Knowledge Base.")]
memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
    tools, 
    OpenAI(temperature=0),
    agent="conversational-react-description",
    verbose=True,
    memory=memory
)

customer_query = "How do I reset my account password?"
response = agent.run(customer_query)
print(response)