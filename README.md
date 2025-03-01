# Simple-ChatBot-on-Locally-with-LLM-API
This project is a simple chatbot with a user-friendly interface built using Streamlit. It demonstrates how to interact with LLM (Large Language Model) APIs by making requests to external endpoints.

In this implementation, I have used the Llama model from Qroq, accessed via the Qroq API. The chatbot processes user queries and generates responses using the power of LLMs, providing a seamless conversational experience.

Here’s a clear step-by-step explanation of your **LangChain chatbot using Qroq models**:

---

# **LangChain Chatbot Using Qroq Models – Step-by-Step Breakdown**  

This chatbot leverages **LangChain** and **Qroq’s Llama model** to generate AI-powered responses. The backend is built with **FastAPI**, while the chatbot communicates with the Qroq API for responses.  

---

## **1️⃣ Loading Environment Variables**  
```python
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API Key from .env
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing in the .env file.")
```
✅ **What’s happening?**  
- The `.env` file is loaded using `load_dotenv()`, ensuring **sensitive data (API key)** is not hardcoded.  
- The **API key** is retrieved from environment variables (`GROQ_API_KEY`).  
- If the API key is missing, an error is raised to prevent failures.

---

## **2️⃣ Initializing the Qroq LLM (Llama Model)**  
```python
from langchain_groq import ChatGroq

# Initialize Groq LLM
llm = ChatGroq(
    api_key=api_key,  
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    max_retries=2,
)
```
✅ **What’s happening?**  
- The **Qroq Llama model** is initialized using `ChatGroq()`.  
- **Model Parameters:**
  - `api_key=api_key` → Authenticates requests.
  - `model="llama-3.3-70b-versatile"` → Specifies the model to use.
  - `temperature=0.0` → Ensures deterministic responses (lower randomness).
  - `max_retries=2` → Allows retrying requests in case of failures.

---

## **3️⃣ Creating a Conversation Message Chain**  
```python
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

message = [
    SystemMessage(content="You are a Math Teacher"),
    HumanMessage(content="Area under the curve")
]
```
✅ **What’s happening?**  
- **Message Types:**
  - `SystemMessage(content="You are a Math Teacher")` → Defines the **AI’s persona**.
  - `HumanMessage(content="Area under the curve")` → Represents the **user’s input/question**.

---

## **4️⃣ Sending the Message to the LLM**  
```python
response = llm.invoke(message)
print(response.content)
```
✅ **What’s happening?**  
- `invoke(message)` sends the user’s input to the **Llama model** via the Qroq API.
- The **AI-generated response** is returned and printed.

---

## **Final Output Example**
If the AI receives:
```
User: "Area under the curve"
```
It may respond with:
```
AI: "The area under the curve represents the integral of a function over a given interval..."
```

---

### **📌 Summary**
1. ✅ **Loads API key** securely from `.env` file.  
2. ✅ **Initializes the Qroq Llama model** with parameters.  
3. ✅ **Creates a message chain** (SystemMessage + HumanMessage).  
4. ✅ **Invokes the model** to generate a response.  
5. ✅ **Prints the AI’s reply** to the console.  

This chatbot can be **extended** by integrating it with a FastAPI backend and a Streamlit UI for interactive conversations! 🚀



Here’s a step-by-step breakdown of how your **Streamlit frontend** interacts with the **FastAPI backend** to create a **Math AI Assistant** chatbot.

---

# **Streamlit Frontend for Math AI Assistant – Step-by-Step Breakdown**  

This **frontend** is built using **Streamlit** and serves as a **UI for interacting** with the backend FastAPI server, which processes the user's math-related queries using the Qroq Llama model.

---

## **1️⃣ Importing Required Libraries**  
```python
import streamlit as st
import requests
```
✅ **What’s happening?**  
- `streamlit` is used to **build the web interface**.  
- `requests` is used to **send user input to the FastAPI backend** and retrieve responses.

---

## **2️⃣ Defining the Backend API URL**  
```python
# FastAPI server URL
FASTAPI_URL = "http://127.0.0.1:8000/message"
```
✅ **What’s happening?**  
- The **URL of the FastAPI backend** is stored in `FASTAPI_URL`.  
- This URL points to the local server running at `127.0.0.1:8000/message`.  
- This endpoint will process user queries and return AI-generated responses.

---

## **3️⃣ Creating the Streamlit UI**  
```python
st.title("Math AI Assistant")
st.write("Ask the AI anything about mathematics!")
```
✅ **What’s happening?**  
- `st.title("Math AI Assistant")` → Sets the **title** of the app.  
- `st.write("Ask the AI anything about mathematics!")` → Displays a **description** for users.

---

## **4️⃣ User Input Box**  
```python
user_input = st.text_input("Enter your question:")
```
✅ **What’s happening?**  
- `st.text_input()` creates a **textbox** where users can type their math-related questions.  
- The input is stored in `user_input`.

---

## **5️⃣ Sending the Query to FastAPI**  
```python
if st.button("Get Answer"):
    if user_input.strip() != "":
        # Send request to FastAPI
        response = requests.post(FASTAPI_URL, json={"message": user_input})
```
✅ **What’s happening?**  
- When the **"Get Answer" button** is clicked:
  - It first checks if `user_input` is **not empty**.
  - If valid, a **POST request** is sent to the FastAPI backend.
  - The user’s input is sent as a **JSON payload** (`{"message": user_input}`).

---

## **6️⃣ Handling the API Response**  
```python
if response.status_code == 200:
    st.write("### AI Response:")
    st.write(response.json()["response"])
else:
    st.error("Error: Unable to fetch response from backend.")
```
✅ **What’s happening?**  
- If the **FastAPI backend responds successfully (`200 OK`)**:
  - The **AI-generated answer** is extracted from `response.json()["response"]` and displayed.  
- If the API call **fails**, an error message is shown.

---

## **7️⃣ Handling Empty Input**  
```python
else:
    st.warning("Please enter a question.")
```
✅ **What’s happening?**  
- If the user clicks "Get Answer" **without entering a question**, a **warning** appears.

---

## **Running the Frontend**
To launch the frontend, run:
```
streamlit run frontend.py
```
✅ **What Happens?**
- A **web interface** opens in the browser.
- The **user enters a math question** and clicks **"Get Answer"**.
- The **question is sent to the FastAPI backend**.
- The **backend processes it** using the **Llama model** and returns a response.
- The **response is displayed** on the frontend.

---

## **📌 Summary of the Chatbot Workflow**
1. **User inputs a math question** in the Streamlit interface.  
2. **Streamlit sends the question** to the FastAPI backend.  
3. **FastAPI processes the input** and gets a response from the Qroq Llama model.  
4. **The response is sent back** to Streamlit.  
5. **Streamlit displays the AI-generated answer** to the user.  

---

