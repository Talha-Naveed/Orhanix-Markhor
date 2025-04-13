import streamlit as st
from PIL import Image
import base64
import random


# Dummy functions to simulate model predictions
def classify_intent(query):
    if "refund" in query.lower():
        return "Refund"
    elif "delivery" in query.lower():
        return "Delivery Issue"
    elif "account" in query.lower():
        return "Account Problem"
    else:
        return "General Inquiry"


def retrieve_faq(query):
    # Dummy FAQ match
    faqs = {
        "Refund": "Please check our refund policy at example.com/refund. Refunds are typically processed within 3-5 business days.",
        "Delivery Issue": "We're sorry to hear about your delivery problem. Most orders arrive within 2-3 business days after shipping.",
        "Account Problem": "For account-related issues, you can reset your password or update your details in your account settings.",
        "General Inquiry": "Thanks for your question. Please provide more details so we can better assist you."
    }
    intent = classify_intent(query)
    return faqs[intent]


def generate_response(intent, faq_answer):
    return f"Thanks for reaching out regarding {intent.lower()}. {faq_answer}"


# Function to create a custom card-like container
def card(title, content, color="#4263EB"):
    st.markdown(
        f"""
        <div style="
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            border-left: 7px solid {color};
            margin-bottom: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        ">
            <h4 style="color: {color};">{title}</h4>
            <p>{content}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# Page configuration with custom CSS
st.set_page_config(
    page_title="AI Support Assistant",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
        padding: 20px;
    }
    .stButton button {
        background-color: #4263EB;
        color: white;
        border-radius: 20px;
        padding: 10px 20px;
        border: none;
        font-weight: bold;
    }
    .stTextInput input {
        border-radius: 20px;
        border: 2px solid #E2E8F0;
        padding: 10px 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    h1 {
        color: #4263EB;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 30px;
    }
    .feedback-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 20px 0;
    }
    .feedback-button {
        padding: 10px 20px;
        border-radius: 30px;
        text-align: center;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    .feedback-button:hover {
        transform: scale(1.05);
    }
    .positive-feedback {
        background-color: #4ade80;
        color: white;
    }
    .negative-feedback {
        background-color: #f87171;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Header with animation effect
st.markdown("""
<div style="text-align: center; animation: fadeIn 1s;">
    <h1>✨ AI Customer Support Assistant ✨</h1>
    <p style="font-size: 1.2rem; color: #4263EB; margin-bottom: 30px;">
        Get answers to your questions instantly
    </p>
</div>
""", unsafe_allow_html=True)

# User input section with enhanced styling
st.markdown("<h3 style='margin-bottom: 15px;'>How can I assist you today?</h3>", unsafe_allow_html=True)
query = st.text_input("", placeholder="Type your question here...", key="query_input")

# Chat interface
if query:
    intent = classify_intent(query)
    faq_answer = retrieve_faq(query)
    response = generate_response(intent, faq_answer)

    # User message
    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: flex-end;
            margin-bottom: 15px;
        ">
            <div style="
                background-color: #E2E8F0;
                padding: 15px;
                border-radius: 20px 20px 0 20px;
                max-width: 80%;
                box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            ">
                <p style="margin: 0;">{query}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Assistant response with typing animation effect
    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: flex-start;
            margin-bottom: 25px;
        ">
            <div style="
                background-color: #4263EB;
                color: white;
                padding: 15px;
                border-radius: 20px 20px 20px 0;
                max-width: 80%;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            ">
                <p style="margin: 0;">{response}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Intent detection card
    intent_colors = {
        "Refund": "#3b82f6",
        "Delivery Issue": "#8b5cf6",
        "Account Problem": "#ec4899",
        "General Inquiry": "#10b981"
    }

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(
            f"""
            <div style="
                background-color: white;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                margin-bottom: 20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            ">
                <h4 style="margin: 0; font-size: 0.9rem; color: #6B7280;">DETECTED INTENT</h4>
                <div style="
                    background-color: {intent_colors.get(intent, '#4263EB')};
                    color: white;
                    padding: 8px 15px;
                    border-radius: 20px;
                    display: inline-block;
                    margin-top: 10px;
                    font-weight: bold;
                ">
                    {intent}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Feedback section with enhanced UI
    st.markdown("<h3 style='margin: 30px 0 15px 0; text-align: center;'>Was this response helpful?</h3>",
                unsafe_allow_html=True)

    # Using columns for the feedback buttons
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        thumbs_up = st.button("👍 Helpful")

    with col3:
        thumbs_down = st.button("👎 Not Helpful")

    if thumbs_up or thumbs_down:
        feedback_type = "positive" if thumbs_up else "negative"

        # Animated thank you message
        st.markdown(
            f"""
            <div style="
                background-color: {'#4ade80' if feedback_type == 'positive' else '#f87171'};
                color: white;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                margin: 20px 0;
                animation: fadeIn 0.5s;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            ">
                <h3 style="margin: 0;">{'Thank you for your feedback!'}</h3>
                <p style="margin: 10px 0 0 0;">{'We appreciate your input and will use it to improve our responses.'}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Additional input for negative feedback
        if feedback_type == "negative":
            st.markdown("<p style='margin-top: 10px;'>Please tell us how we can improve:</p>", unsafe_allow_html=True)
            improvement_feedback = st.text_area("", placeholder="What would have been more helpful?",
                                                key="improvement_input")
            if improvement_feedback:
                st.success("Thank you for your suggestions! We'll work on improving our responses.")

# Footer
st.markdown(
    """
    <div style="
        border-top: 1px solid #E2E8F0;
        margin-top: 50px;
        padding-top: 20px;
        text-align: center;
        color: #6B7280;
    ">
        <p>© 2025 AI Customer Support | Powered by AI</p>
    </div>
    """,
    unsafe_allow_html=True
)