import streamlit as st
from streamlit_chat import message
from streamlit_extras.add_vertical_space import add_vertical_space
from dotenv import load_dotenv
from store import init_store
from query_engine import init_query_engine

load_dotenv(dotenv_path=".env")

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(_qa, query):
    result = _qa({"question": query})
    return result['answer']

def main():
    st.set_page_config(page_title="FreshChat - An LLM-powered Streamlit app", page_icon="💬")

    # Sidebar contents
    with st.sidebar:
        st.title('💬 Freshdesk Chatbot')
        st.markdown('''
        ## About
        This app is a Generative AI chatbot built using:
        - [Streamlit](https://streamlit.io/)
        - [LangChain](https://python.langchain.com/en/latest/index.html) Framework for developing apps with LLMs
        
        💡 Note: No API key required!
        ''')
        add_vertical_space(5)
        st.write('Made with ❤️ by Divya Venkataramani')

    retriever = init_store()
    qa = init_query_engine(retriever)
    
    # Generate empty lists for generated and past.
    ## generated stores AI generated responses
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["I'm FreshChat, How may I help you?"]
    ## past stores User's questions
    if 'past' not in st.session_state:
        st.session_state['past'] = ['Hi!']

    # Layout of input/response containers
    input_container = st.container()
    # colored_header(label='', description='', color_name='blue-30')
    response_container = st.container()

    ## Applying the user input box
    with input_container:
        user_input = get_text()

    ## Conditional display of AI generated responses as a function of user provided prompts
    with response_container:
        if user_input:
            response = generate_response(qa, user_input)
            st.session_state.past.append(user_input)
            st.session_state.generated.append(response)
            
        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state['past'][i], is_user=True, avatar_style="avataaars", key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))
                
if __name__ == "__main__":
    main()