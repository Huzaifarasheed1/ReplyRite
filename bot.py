import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to initialize or get the chat session
def get_chat_session():
    # Initialize chat session if it doesn't exist
    if 'chat_session' not in st.session_state:
        model = genai.GenerativeModel("gemini-pro")
        st.session_state.chat_session = model.start_chat(history=[])
    return st.session_state.chat_session

# Function to get Gemini response
def get_gemini_response(question):
    chat = get_chat_session()
    response = chat.send_message(question, stream=True)
    return response

# Function to display chat history
def display_chat_history():
    # Initialize chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display existing chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

# Streamlit app main function
def main():
    # Set page configuration
    st.set_page_config(page_title="ReplyRite", page_icon="💬")
    
    # App title
    st.title("🤖 Chat with ReplyRite")
    
    # Display existing chat history
    display_chat_history()
    
    # Chat input
    if prompt := st.chat_input("Enter your message:"):
        # Add user message to chat history
        st.session_state.chat_history.append({
            'role': 'user', 
            'content': prompt
        })
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get and display bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response_stream = get_gemini_response(prompt)
                full_response = ""
                response_placeholder = st.empty()
                
                # Stream the response
                for chunk in response_stream:
                    full_response += chunk.text
                    response_placeholder.markdown(full_response)
        
        # Add bot response to chat history
        st.session_state.chat_history.append({
            'role': 'assistant', 
            'content': full_response
        })

# Run the app
if __name__ == "__main__":
    main()