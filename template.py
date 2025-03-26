import os

import logging

from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] :%(message)s:')

files_to_create = [
    "genai_lab/__init__.py",

    "genai_lab/basic_chatbots/00_simple_chatbot.ipynb",
    "genai_lab/basic_chatbots/01_advanced_chatbot.ipynb",
    "genai_lab/basic_chatbots/README.md",

    "genai_lab/key_extraction/02_Key_Data_Extraction.ipynb",
    "genai_lab/key_extraction/03_Sentiment_Analysis.ipynb",
    "genai_lab/key_extraction/README.md",

    "genai_lab/rag_components/02_Data_loader_rag_demo.ipynb",
    "genai_lab/rag_components/03_Rag_components.ipynb",
    "genai_lab/rag_components/04_Basic_RAG_implementation.ipynb",
    "genai_lab/rag_components/05_Memory_langchain.ipynb",
    "genai_lab/rag_components/README.md",

    "genai_lab/langchain_lcel/06_LCEL.ipynb",
    "genai_lab/langchain_lcel/07_LCEL.ipynb",
    "genai_lab/langchain_lcel/08_LCEL.ipynb",
    "genai_lab/langchain_lcel/README.md",

    "genai_lab/langchain_apps/09_LangServe_demo.ipynb",
    "genai_lab/langchain_apps/10_LangGraph.ipynb",
    "genai_lab/langchain_apps/11_LangSmith.ipynb",
    "genai_lab/langchain_apps/README.md",

    "genai_lab/retriever_apps/06_Retriever_App.ipynb",
    "genai_lab/retriever_apps/README.md",

    "genai_lab/qa_apps/04_Qa_From_Sql.ipynb",
    "genai_lab/qa_apps/05_Qa_From_Pdf.ipynb",
    "genai_lab/qa_apps/README.md",

    "Data/.gitkeep",               
    "notebooks/.gitkeep",          

    "requirements.txt",
    "pyproject.toml",
    ".gitignore",
    "README.md"
]


for file_path in files_to_create:
    file_path = Path(file_path)
    filedir , file_name = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory ; {filedir} for the filename {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file {file_path}")
    else:
        logging.info(f"{file_name} is ready")

print("? Project structure created successfully.")