import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="CampusMate AI",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.title {
    text-align: center;
    color: #38bdf8;
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 20px;
}

.user {
    background-color: #2563eb;
    color: white;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
    text-align: right;
    font-size: 18px;
}

.bot {
    background-color: #1e293b;
    color: #22c55e;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🤖 CampusMate AI</div>',
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

def chatbot_response(message):

    text = message.lower()

    if "hello" in text or "hi" in text:
        return random.choice([
            "Hello! Welcome to CampusMate AI.",
            "Hi! How can I help you today?",
            "Hey! Nice to see you."
        ])

    elif "how are you" in text:
        return "I am doing great. Thanks for asking."

    elif "your name" in text:
        return "My name is CampusMate AI."

    elif "time" in text:
        return "Current time is " + datetime.now().strftime("%I:%M %p")

    elif "date" in text:
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    elif "day" in text:
        return "Today is " + datetime.now().strftime("%A")

    elif "joke" in text:

        jokes = [
            "Why do programmers hate bugs? Because bugs hate debugging.",
            "Why was the computer cold? It left its Windows open.",
            "Why do Python developers wear glasses? Because they cannot C."
        ]

        return random.choice(jokes)

    elif "motivate" in text or "motivation" in text:
        return "Success comes from consistency and hard work."

    elif "sad" in text or "stress" in text:
        return "Take a small break and relax. Everything will be okay."

    elif "python" in text:
        return "Python is a powerful programming language."

    elif "java" in text:
        return "Java is widely used for software development."

    elif "html" in text:
        return "HTML is used to create webpages."

    elif "css" in text:
        return "CSS is used to style webpages beautifully."

    elif "javascript" in text:
        return "JavaScript makes websites interactive."

    elif "ai" in text:
        return "Artificial Intelligence allows machines to learn and think."

    elif "machine learning" in text:
        return "Machine Learning helps systems learn from data."

    elif "deep learning" in text:
        return "Deep Learning uses neural networks for AI tasks."

    elif "weather" in text:
        return "Today's weather is pleasant and sunny."

    elif "food" in text:
        return "Pizza and biryani are popular favorite foods."

    elif "movie" in text:
        return "Interstellar is a great science fiction movie."

    elif "music" in text:
        return "Music helps people relax and feel motivated."

    elif "study" in text:
        return "Daily practice and revision improve learning."

    elif "exam" in text:
        return "Practice previous papers and revise important concepts."

    elif "project" in text:
        return "AI and web projects are excellent for portfolios."

    elif "github" in text:
        return "GitHub is used to host and manage coding projects."

    elif "linkedin" in text:
        return "LinkedIn helps showcase your skills professionally."

    elif "bye" in text:
        return "Goodbye! Have a wonderful day."

    elif "thank you" in text:
        return "You are welcome."

    else:

        return random.choice([
            "Interesting question.",
            "Can you explain more?",
            "I am still learning that.",
            "Please ask another question.",
            "That sounds interesting."
        ])

user_input = st.chat_input("Type your message here...")

if user_input:

    st.session_state.messages.append(("user", user_input))

    response = chatbot_response(user_input)

    st.session_state.messages.append(("bot", response))

for sender, message in st.session_state.messages:

    if sender == "user":

        st.markdown(
            f'<div class="user">{message}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="bot">🤖 {message}</div>',
            unsafe_allow_html=True
        )
