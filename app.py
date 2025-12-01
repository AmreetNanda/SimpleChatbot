from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate

from langchain_community.chat_models import ChatLlamaCpp
from langchain_community.chat_models import ChatOllama
from langchain_community.chat_models import ChatOpenAI

from langserve import add_routes

import uvicorn
import os

from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title = "Langchain Server",
    version = 1.0,
    description="A simple API server"
)

add_routes(app, ChatOllama(model='llama3'), path="/openai")

llm = Ollama(model="llama3")
prompt = ChatPromptTemplate.from_template("Write an essay about the topic {topic} with 300 words")

add_routes(app, prompt|llm, path='/essay')

if __name__ == "__main__":
    uvicorn.run(app, host ="localhost",port=8000)

