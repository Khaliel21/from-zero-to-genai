import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
groq_api_key = os.environ['GROQ_API_KEY']

from langchain_groq import ChatGroq
llmModel = ChatGroq()

for chunk in llmModel.stream(
    "Tell me one fun fact about the kennedy family . i need detail reponse"
):
    print(chunk, end="", flush=True)