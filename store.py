from langchain.vectorstores import Vectara
from langchain.vectorstores.vectara import VectaraRetriever
from langchain.document_loaders import PyPDFDirectoryLoader
from helper import get_logger
import streamlit as st

log = get_logger(__name__)

@st.cache_data()
def init_store():
    loader = PyPDFDirectoryLoader("../../Archive")
    documents = loader.load()
    log.info("Loaded documents ...")
    vectorstore = Vectara.from_documents(documents, embedding=None)
    retriever = VectaraRetriever(vectorstore=vectorstore)
    return retriever
