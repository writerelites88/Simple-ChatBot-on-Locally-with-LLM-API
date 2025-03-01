
#a simple langchain chatbot using qroq models
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
 
# Get API Key from .env , you must have pasted the key in your .env file in the same working directory 
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing in the .env file.")

# Initialize Groq LLM
llm = ChatGroq(
    api_key=api_key,  
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    max_retries=2,
)

message=[SystemMessage(content="you are Math Teacher "), HumanMessage(content="Area under the curve")]
response = llm.invoke(message)
print(response.content)
