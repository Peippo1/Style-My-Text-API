import streamlit as st
import requests
import os

# You can set DEBUG_MODE environment variable to "true" to show connection info

# Initialize 'dark_mode' in session state if it doesn't exist
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Sidebar checkbox to toggle dark mode, synced with session state
dark_toggle = st.sidebar.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = dark_toggle

# Apply dark mode CSS styles if dark mode is enabled
if dark_toggle:
    st.markdown(
        """
        <style>
            body { background-color: #0e1117; color: #cfcfcf; }
            textarea, .stTextInput, .stSelectbox, .stButton { background-color: #1c1e26 !important; color: #fff !important; }
        </style>
        """,
        unsafe_allow_html=True
    )

# API endpoint constant for styling service
API_URL = os.getenv("API_URL", "http://localhost:8000/style")

# Optionally show the API URL in debug mode
if os.getenv("DEBUG_MODE") == "true":
    st.markdown(f"*Using API URL: `{API_URL}`*")

# Configure the Streamlit page with a title and icon
st.set_page_config(page_title="Style My Text", page_icon="🎨")

# Main title and subtitle of the app
st.title("🎨 Style My Text")
st.subheader("Transform your text into fun styles!")

# Text area for user input
text_input = st.text_area("Enter your text", height=150)

# Dictionary mapping style keys to descriptive labels with emojis
styles = {
    "pirate": "🦜 Pirate (Ahoy matey!)",
    "sarcastic": "🙄 Sarcastic (LoOkS gReAt...)",
    "shakespeare": "🎭 Shakespearean (Thou art wise)",
    "emoji": "😄 Emoji (🔥❤️😎)",
    "reverse": "🔁 Reverse (txet desrever)",
    "shouty": "📢 Shouty (ALL CAPS)"
}

# Dropdown select box for choosing a style, showing descriptive labels
style = st.selectbox(
    "Choose a style (hover for description)",
    options=list(styles.keys()),
    format_func=lambda x: styles[x]
)

# When the "Style it!" button is pressed and input text is provided
if st.button("Style it!") and text_input:
    with st.spinner("Styling..."):
        try:
            response = requests.post(
                API_URL,
                data={"text": text_input, "style": style}
            )
            # If the API call is successful, display styled text and update history
            if response.ok:
                styled = response.json()["styled_text"]
                st.success("Here's your styled text:")
                st.code(styled, language="markdown")

                # Initialize history list in session state if not present
                if "history" not in st.session_state:
                    st.session_state.history = []

                # Append the current input, style, and output to history
                st.session_state.history.append((text_input, style, styled))
            else:
                # Show error message if API call fails
                st.error(f"Oops, something went wrong!\nStatus code: {response.status_code}")
                st.error(f"Oops, something went wrong!\n{response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to the styling service at {API_URL}. Please ensure the backend is running or set the API_URL environment variable correctly.")
            return

# Button to clear the app (rerun script)
if st.button("Clear"):
    st.experimental_rerun()

# Display the last 5 styling history entries if available
if st.session_state.get("history"):
    st.markdown("### 📜 Styling History")
    for original, s, output in reversed(st.session_state.history[-5:]):
        st.markdown(f"**Input** ({s}): {original}")
        st.code(output, language="markdown")