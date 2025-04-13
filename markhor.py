import google.generativeai as genai
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("API_KEY")  # Ensure your API key is set in the environment variable

# --- Configuration ---
  # Replace with your Gemini API key
genai.configure(api_key=API_KEY)

# --- Load FAQ Data from a file path ---
faq_file = "Ecommerce_FAQ_Chatbot_dataset.json"  # Replace with your actual FAQ file path
with open(faq_file, "r") as f:
    faq_data = json.load(f)

# --- Embedding Generation ---
def generate_embedding(text):
    # Use 'models/embedding-001' as the embedding model for the task
    model = "models/embedding-001"  
    try:
        embedding = genai.embed_content(
            model=model,
            content=text,
            task_type="retrieval_document"  # This task type is appropriate for embeddings
        )
        return embedding['embedding']
    except Exception as e:
        print(f"Error generating embedding for the text: {e}")
        return []

# Generate embeddings for all FAQ questions
faq_embeddings = []
for item in faq_data['questions']:
    embedding = generate_embedding(item["question"])
    if embedding:
        faq_embeddings.append(embedding)

# Pair embeddings with their Q&A (with added error handling for empty embeddings)
faq_store = list(zip(faq_embeddings, faq_data['questions']))

# --- Sentiment Analysis using Gemini-2.0-Flash ---
def detect_sentiment_with_gemini(text):
    try:
        # Using gemini-2.0-flash for sentiment analysis
        response = genai.generate_content(
            model="models/gemini-2.0-flash",  # Updated to use gemini-2.0-flash
            contents=[{
                "parts": [{
                    "text": f"""Analyze the sentiment of this customer message and respond with ONLY one word:
                    - "positive" if happy/satisfied
                    - "negative" if unhappy/frustrated
                    - "neutral" if neither
                    
                    Message: "{text}"
                    """
                }]
            }],
            generation_config={
                "temperature": 0.3,
                "max_output_tokens": 1,  # We only want one word
                "top_p": 0.8,
                "top_k": 10
            }
        )
        
        # Get the response text and clean it
        sentiment = response.text.strip().lower()
        
        # Validate the response
        if sentiment in ["positive", "negative", "neutral"]:
            return sentiment
        else:
            print(f"Unexpected sentiment response: {sentiment}")
            return "neutral"
            
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return "neutral"

# --- FAQ Retrieval based on Query ---
def get_most_similar(query, threshold=0.7):
    query_embedding = generate_embedding(query)
    if not query_embedding:
        return "Sorry, I couldn't generate an embedding for that query."
    
    query_embedding = np.array(query_embedding).reshape(1, -1)
    
    stored_embeddings = np.array([item[0] for item in faq_store])
    similarities = cosine_similarity(query_embedding, stored_embeddings)
    
    best_match_idx = np.argmax(similarities)
    best_score = similarities[0][best_match_idx]
    
    if best_score >= threshold:
        return faq_store[best_match_idx][1]["answer"]
    else:
        return "Sorry, I couldn't find a relevant answer. Try rephrasing!"

# --- Response Generation ---
def generate_response(query, sentiment):
    if sentiment == "negative":
        return f"Sorry to hear you're having a problem. Let me assist you with that. Here's what I found: {get_most_similar(query)}"
    elif sentiment == "positive":
        return f"Great! I'm glad you're happy. Here's some information that might help: {get_most_similar(query)}"
    else:
        return f"Let me assist you with your query: {get_most_similar(query)}"

