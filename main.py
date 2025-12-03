import os
import asyncio
import streamlit as st
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini-compatible provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Setup model and agent
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

agent = Agent(
    name="🍽️ Recipe/Cooking Assistant",
    instructions=(
        "You are a helpful assistant specialized in providing cooking tips, recipes, and culinary advice. "
        "Answer questions clearly and provide step-by-step instructions when needed. "
        "If the user asks a question not related to cooking, politely decline."
    ),
    model=model
)

# Streamlit App UI
st.set_page_config(page_title="Cooking Assistant 🍳", layout="centered")
st.title("🍽️ Recipe/Cooking AI Agent")
st.write("Ask me anything about cooking, recipes, or ingredients!")

user_input = st.text_input("Enter your cooking question:")

if st.button("Get Recipe"):
    if user_input.strip() == "":
        st.warning("Please enter a cooking question.")
    else:
        with st.spinner("Thinking... 🍲"):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            output = loop.run_until_complete(Runner().run(starting_agent=agent, input=user_input))
            st.success("Here's your answer:")
            st.write(output.final_output)

# Fixed footer with emoji, name, and image
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background: white;
        text-align: center;
        padding: 10px;
        font-weight: bold;
        color: #555;
        border-top: 1px solid #eee;
        z-index: 100;
    }
    .footer img {
        height: 20px;
        vertical-align: middle;
        margin-right: 8px;
        border-radius: 50%;
    }
    </style>
    <div class="footer">
        <img src="https://i.imgur.com/fxW7YJf.png" alt="Muhammad Maaz">
        👨‍🍳 Built with ❤️ by <span style="color:#ff4b4b;">Muhammad Maaz</span>
    </div>
    """,
    unsafe_allow_html=True
) 
