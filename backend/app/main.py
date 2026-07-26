from dotenv import load_dotenv
import os
from fastapi import FastAPI
from pydantic import BaseModel
from agent.config import chat
# from schema import chatFormat   
from pydantic import BaseModel
load_dotenv()  # Load environment variables from .env file
api_key=os.getenv("GEMINI_API_KEY")  # Retrieve the API key from environment variables

app = FastAPI()

@app.get("/")
def hello_world() -> str:
    return "hello world"




class ChatRequest(BaseModel):
    input_text: str


@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    response = chat(request.input_text)

    return {
        "response": response
    }


def main():
    print("hello")

if __name__ == "__main__":
    main()
