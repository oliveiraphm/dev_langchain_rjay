from pydantic import BaseModel, Field, ValidationError, field_validator
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

class Movie(BaseModel):
    title : str = Field(description="The title of the movie")
    director : str = Field(description="The director of the movie")
    year : int = Field(description="The release year of the movie")

    @field_validator("title")
    def title_must_be_capitalized(cls, value):
        if not value.istitle():
            raise ValueError("Movie title must be capitalized.")
        return value
    
parser = PydanticOutputParser(pydantic_object=Movie)

prompt = PromptTemplate(
    template="Please provide information about a movie in the following format:\n{format_instructions}\nQuestion:{query}",
    input_variables=["query"],
    partial_variables={"format_instructions" : parser.get_format_instructions()},
)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)

query = "Tell me about the movie 'Inception'."
human_message = HumanMessage(content=prompt.format(query=query))
response = llm([human_message])

try:
    parsed_movie = parser.parse(response.content)
    print(parsed_movie)
except ValidationError as e:
    print(f"Validation Error: {e}")