from helper import get_logger
from os import environ
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


load_dotenv()
log = get_logger(__name__)

def init_query_engine(retriever):
    openai_api_key = environ['OPENAI_API_KEY']
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
    qa = ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory)
    log.info("Initialized all components ...")
    return qa
