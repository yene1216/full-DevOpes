from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool,tool
# from langgraph.prebuilt import create_agent
from langchain.agents import create_agent
from agent.tools.calculator import calculator 
from agent.tools.save_notes import save_notes
from agent.tools.say_may_name import say_my_name
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
api_key=os.getenv("GEMINI_API_KEY")  # Retrieve the API key from environment

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0,
    google_api_key=api_key

)


tools = [calculator, save_notes, say_my_name]
agent=create_agent(
    model=llm,
    tools=tools
)

def chat(input_text: str):
    response = agent.invoke(
        {
            "messages": [
                ("user", input_text),
            ]
        }
    )
    return response["messages"][-1].content[0]["text"]  


# input_text = input("Enter your question: ")
# response = agent.invoke(
#     {
#         "messages": [
#             ("user", input_text),
#         ]
#     }
# )
# print(response["messages"][-1].content[0]["text"])
