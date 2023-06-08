# Chatbot
Chatbot using Streamlit, OpenAI and LangChain to chat with your PDF documents

This chatbot reads from a directory of PDF files, converts them to vector embeddings using Langchain and Vectara and lets the user chat with his documents.

### Prerequisites
- Python 3.9+
- OpenAI API Key - (Paid account on https://platform.openai.com/account/api-keys)
- Vectara Corpus ID - (Free account using https://console.vectara.com/)
- Vectara Customer ID 
- Vectara API Key

### Steps to setup and run the project
- Run the command `pip install -r requirements.txt`
- Add the API keys in the .env file
- Run the command `streamlit run chatbot.py`
