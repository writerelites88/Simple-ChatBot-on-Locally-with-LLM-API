import streamlit as st
import requests


# FastAPI server URL
FASTAPI_URL = "http://127.0.0.1:8000/message"

# Streamlit UI

st.title("Math AI Assistant")
st.write("Ask the AI anything about mathematics!")

# User input
user_input = st.text_input("Enter your question:")

# Button to get answer

if st.button("Get Answer"):
    if user_input.strip() != "":
        # Send request to FastAPI
        response = requests.post(FASTAPI_URL, json={"message": user_input})

        if response.status_code == 200:
            st.write("### AI Response:")
            st.write(response.json()["response"])
        else:
            st.error("Error: Unable to fetch response from backend.")
    else:
        st.warning("Please enter a question.")

#streamlit run frontend.py
