from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

user_preferences_data = {
    "1234" : {"favorite-genres": ["Action", "Sci-Fi"], "favorite_actors":["Tom Cruise"]}
}

def user_preference_tool(user_id: str):
    return user_preferences_data.get(user_id, "No preferences found.")

def recommendation_tool(user_preferences):
    if not user_preferences:
        return "No preferences available for recommendations."
    return "Based on your preferences, we recommend 'Inception' and 'The MatriX'."

tools = [
    Tool(name="User Preferences", func=user_preference_tool, description="Retrieve user preferences."),
    Tool(name="Recommendation Generator", func=recommendation_tool, description="Generate recommendations.")
]

agent = initialize_agent(tools, OpenAI(temperature=0.7), agent="zero-shot-react-description", verbose=True)

user_id = "1234"
response = agent.run(f"Generate recommendations for user ID {user_id}.")
print(response)
