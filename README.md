# 🛒 AI FAQ Agent for E-commerce

An intelligent AI-powered FAQ Agent designed to handle E-commerce related queries with human-like precision. Built with **Streamlit** for the front-end and powered by **Gemini API**, this agent provides sentiment-aware responses by understanding user intent and context. All FAQ entries are pre-embedded in a local vector database for fast and relevant retrieval.

---

## ✨ Features

- ✅ Answers E-commerce-related frequently asked questions
- 📁 Pre-embedded FAQs for efficient retrieval
- 🧠 Sentiment detection for contextual responses
- 🤖 Powered entirely by **Gemini API**
- 🌐 Interactive **Streamlit** interface
- ⚡ Fast and scalable for customer support

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) — Web Interface
- [Gemini API](https://ai.google.dev/) — LLM and Embedding provider
- [FAISS / ChromaDB / Vector DB] — (your vector DB) for storing embedded FAQs
- [Python](https://www.python.org/) — Core language

---

## 🧠 How It Works

1. **Embedding FAQs**:  
   At startup, all e-commerce FAQ entries are embedded using the Gemini API and stored in a local vector database.

2. **User Input**:  
   The user types a query in the Streamlit web interface.

3. **Semantic Search**:  
   The query is embedded and compared against the database to retrieve the most relevant FAQ.

4. **Sentiment Detection**:  
   Gemini analyzes the sentiment of the user query (e.g., frustration, confusion, neutrality).

5. **Response Generation**:  
   Based on the retrieved FAQ and the sentiment, Gemini generates a response that is empathetic and appropriate.

---

