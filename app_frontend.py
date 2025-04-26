import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="Deep Research Bot ",
    page_icon="🤖",
    layout="centered",  # Can be "centered" or "wide" layout
    initial_sidebar_state="collapsed"
)

# Add some styling with markdown
st.markdown(
    """
    <style>
        .big-font {
            font-size: 32px !important;
            color: #ff6347;
            font-weight: bold;
        }
        .header-font {
            font-size: 28px;
            color: #5f6368;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #555;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title and Introduction
st.title("🤖 Deep Research Bot")
st.subheader("Ask your questions and let the bot research the answers for you instantly!")

# Query Input Field
query = st.text_input("Ask a question to the bot:")

# When the user clicks "Ask"
if st.button("Ask"):
    if query:
        try:
            # Show spinner while the bot is processing the request
            with st.spinner('🤔 Bot is thinking...'):
                response = requests.post("http://127.0.0.1:5000/ask", json={"query": query})

            if response.status_code == 200:
                # Extract the response data
                data = response.json()
                content = data.get('answer', 'Sorry, I could not fetch an answer.')

                # Display the answer with success message
                st.success("✅ Here's what I found:")

                # Display the content in a clean and readable format
                st.markdown(content, unsafe_allow_html=True)  # Render markdown formatting
            else:
                st.error("❌ Error: Could not get a response from the bot. Please try again.")
        except Exception as e:
            st.error(f"⚠️ Exception occurred: {e}")
    else:
        st.warning("⚠️ Please enter a question to ask.")

# Footer Section
st.markdown("---")
st.markdown(
    """
    <div class="footer">
        Made with ❤️ by Harshika
    </div>
    """,
    unsafe_allow_html=True
)
