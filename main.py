import streamlit as st
import markhor

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

    # faq_answer = retrieve_faq(query)

    sentiment = markhor.detect_sentiment_with_gemini(query)
    response = markhor.generate_response(query, sentiment)

    # User message
    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: flex-end;
            margin-bottom: 15px;
        ">
            <div style="
                background-color: #000000;
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



    col1, col2 = st.columns([1, 2])

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