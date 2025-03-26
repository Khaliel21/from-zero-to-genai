import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from dotenv import load_dotenv, find_dotenv

from fastapi import FastAPI
from langserve import add_routes
import uvicorn

### Check on https://python.langchain.com/docs/langserve/

_ = load_dotenv(find_dotenv())
groq_api_key = os.environ['GROQ_API_KEY']
hf_token_api = os.environ['HF_TOKEN']
pinecone_api_key = os.environ['PINECONE_API_KEY']

## Call the Model

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

output_parser = StrOutputParser()


## Create the template 

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate([
    ('system', system_template),
    ('user', '{text}')
])

chain = prompt_template | llm | output_parser

## Fast API syntax

app = FastAPI(
    titel = 'SimpleTranslator',
    version= "1.0",
    description= 'A Simple API server using LangChain Runnable interface',
)

add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    uvicorn.run(app=app, host='localhost', port=8000)


