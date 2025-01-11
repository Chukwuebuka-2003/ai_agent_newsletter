import streamlit as st
from main import NewsletterCrew # Import the ResearchCrew class from main.py
import os
import uuid

# Set up API keys
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["EXA_API_KEY"] = st.secrets["EXA_API_KEY"]

# Initialize session state for conversations if not already set
if "conversations" not in st.session_state:
    st.session_state.conversations = {}

# Function to load a conversation
def load_conversation(conversation_id):
    st.session_state.current_conversation = st.session_state.conversations[conversation_id]

# Sidebar: List previous conversations
st.sidebar.title("Previous Conversations")
if st.session_state.conversations:
    conversation_ids = list(st.session_state.conversations.keys())
    selected_conversation = st.sidebar.selectbox("Select a conversation:", conversation_ids)
    if st.sidebar.button("Load Conversation"):
        load_conversation(selected_conversation)
else:
    st.sidebar.write("No previous conversations.")

# Main chat interface
st.title("Team Geto Weekly AI Newsletter")
st.write("Welcome! Feel free to ask me anything about your research topics in machine learning, deep learning, or AI, and I'll be happy to assist you..")

# Display current conversation
if "current_conversation" not in st.session_state:
    st.session_state.current_conversation = []

for message in st.session_state.current_conversation:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Enter your research topic or question:"):
    # Add user message to current conversation
    st.session_state.current_conversation.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process user input
    inputs = "\n".join([msg["content"] for msg in st.session_state.current_conversation if msg["role"] == "user"])
    research_crew = NewsletterCrew(inputs)
    response = research_crew.run()

    # Add assistant response to conversation history
    st.session_state.current_conversation.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save conversation
    conversation_id = str(uuid.uuid4())
    st.session_state.conversations[conversation_id] = st.session_state.current_conversation
