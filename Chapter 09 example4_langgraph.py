from typing import TypedDict
from langgraph.graph import StateGraph, END


class TravelState(TypedDict):
    input: str

def greet_user(state: TravelState) -> TravelState:
    print("Hello! How can I assist you with your travel plans today?")
    return state

def get_destination(state: TravelState) -> TravelState:
    destination = state["input"]
    print(f"{destination} sounds like a fantastic destination.")
    return state

def suggest_activities(state: TravelState) -> TravelState:
    print("Here are some activities: visiting museums, exploring nature trails.")
    return state


graph = StateGraph(TravelState)  
graph.add_node("GreetUser", greet_user)
graph.add_node("GetDestination", get_destination)
graph.add_node("SuggestActivities", suggest_activities)

graph.set_entry_point("GreetUser")
graph.add_edge("GreetUser", "GetDestination")
graph.add_edge("GetDestination", "SuggestActivities")
graph.add_edge("SuggestActivities", END)

compiled_graph = graph.compile()
compiled_graph.invoke({"input": "Hawaii"})