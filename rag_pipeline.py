from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import chatGroq
from langchain.chains import RetreivalQA
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
def create_vectorstorage(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectors = Chroma.from_documents(chunks, embeddings)
    return vectors
