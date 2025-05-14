import streamlit as st
import requests
import time
import json

# Streamlit page configuration
st.set_page_config(page_title="Intelligent Customer Support Chatbot", page_icon="🤖", layout="centered")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to fetch dataset or responses via API
def fetch_response_from_api(user_input, api_key):
    # Replace with your actual API endpoint
    api_url = "https://api.example.com/customer-support-data"  # Placeholder URL
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"query": user_input}
    
    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Assuming API returns a 'response' field; adjust based on actual API structure
            return data.get("response", "I'm sorry, I couldn't process that request.")
        else:
            return "Error: Unable to fetch response from API."
    except requests.RequestException:
        return "Error: API connection failed. Please check your API key or network."

# Streamlit UI
st.title("🤖 Intelligent Customer Support Chatbot")
st.markdown("Welcome to our automated assistant! Ask your questions below, and I'll assist you promptly.")

# API Key input
api_key = st.text_input("Enter your API Key", type="password")
if not api_key:
    st.warning("Please enter a valid API key to continue.")
    st.stop()

# Chat container
chat_container = st.container()

# Input for user message
with st.form(key="user_input_form", clear_on_submit=True):
    user_input = st.text_input("Type your question here...", key="user_input")
    submit_button = st.form_submit_button(label="Send")

# Process user input and display chat
if submit_button and user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Fetch response from API
    with st.spinner("Thinking..."):
        bot_response = fetch_response_from_api(user_input, api_key)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# Display chat history
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(f"*You*: {message['content']}")
        else:
            with st.chat_message("assistant"):
                st.markdown(f"*Assistant*: {message['content']}")

# Sidebar with project info
with st.sidebar:
    st.header("About the Project")
    st.markdown("""
    *Revolutionizing Customer Support with an Intelligent Chatbot*  
    This project delivers an automated assistant designed to streamline customer support. Powered by an API-driven dataset, the chatbot provides accurate and timely responses to user queries, enhancing efficiency and user experience.
    """)
    st.markdown("*Features*:")
    st.markdown("- Real-time chat interface")
    st.markdown("- API-based response generation")
    st.markdown("- Streamlit-powered web UI")
