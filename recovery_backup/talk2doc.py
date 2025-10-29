import streamlit as st

def app():
    st.title('Ask Queries')
    q = st.text_input('Ask a question for the virtual assistant')
    if q:
        st.write('You asked:', q)
import streamlit as st
import importlib
import os
from typing import Tuple


# Helper to safely get the Gemini API key
def get_gemini_api_key() -> str | None:
    """Try to read GEMINI_API_KEY from Streamlit secrets, then environment, else return None."""
    try:
        if hasattr(st, "secrets"):
            # st.secrets may be a dict-like object in many environments
            key = st.secrets.get("GEMINI_API_KEY") if isinstance(st.secrets, dict) else None
            if key:
                return key
    except Exception:
        # Don't crash the app if secrets aren't configured
        pass

    # Fallback to environment variable
    return os.environ.get("GEMINI_API_KEY")


# Globals that hold the dynamically imported client
genai = None
GEMINI_AVAILABLE = False


def configure_gemini(api_key: str) -> Tuple[bool, str]:
    """Try to import and configure google.generativeai. Return (success, message)."""
    global genai, GEMINI_AVAILABLE
    try:
        genai = importlib.import_module("google.generativeai")
    except Exception as e:
        genai = None
        GEMINI_AVAILABLE = False
        return False, f"google-generativeai package is not installed: {e}"

    try:
        genai.configure(api_key=api_key)
        GEMINI_AVAILABLE = True
        return True, "Gemini configured successfully for this session."
    except Exception as e:
        genai = None
        GEMINI_AVAILABLE = False
        return False, f"Failed to configure Gemini client: {e}"


# Try to configure from secrets/env at import time (non-fatal)
_initial_key = get_gemini_api_key()
if _initial_key:
    configure_gemini(_initial_key)


def ask_gemini(query: str) -> str:
    """Ask Gemini AI about diabetes. Raises RuntimeError if not available."""
    if not GEMINI_AVAILABLE or genai is None:
        raise RuntimeError(
            "Gemini client is not configured. Provide a valid GEMINI_API_KEY in Streamlit secrets, environment, or enter a key in the app to use the chatbot."
        )

    prompt = f"""
    You are a medical chatbot specialized in diabetes and its health implications.
    Answer only diabetes-related queries with medically accurate information.
    If a question is unrelated to diabetes, politely inform the user that you can only answer diabetes-related questions.

    **User's Question:** {query}

    Provide a clear, concise, and accurate medical response.
    """

    # Create a model and request content. Keep errors surfaced to the caller/UI.
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    # response may be an object; prefer .text if present
    return getattr(response, "text", str(response))


def app():
    st.title("🩺 Diabetes Medical Chatbot")
    from pathlib import Path
    images_dir = Path(__file__).resolve().parent.parent / 'images'
    st.image(str(images_dir / 'capsule.png'))
    st.success("Please ask your queries related to diabetes and its health implications.")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Allow user to supply an API key for this session if none configured
    configured_key = get_gemini_api_key() or st.session_state.get("GEMINI_API_KEY_temp")

    if not GEMINI_AVAILABLE:
        with st.expander("Connect to Gemini (optional)"):
            st.write(
                "If you have a Gemini API key you can paste it below to enable the chatbot for this Streamlit session. "
                "Keys entered here are used only for the running session and are not saved to Streamlit secrets."
            )
            temp_key = st.text_input("Paste GEMINI API Key (session only):", type="password")
            if st.button("Use this key for session"):
                if temp_key:
                    success, msg = configure_gemini(temp_key)
                    if success:
                        st.session_state["GEMINI_API_KEY_temp"] = temp_key
                        st.success(msg)
                    else:
                        st.error(msg)
                else:
                    st.warning("Please paste a non-empty API key to enable the chatbot for this session.")

    # User input for querying
    user_query = st.text_input("Ask your question about diabetes:")

    # Only show main action if Gemini is configured
    if GEMINI_AVAILABLE:
        if st.button("Get Answer"):
            if user_query:
                try:
                    response = ask_gemini(user_query)
                    st.session_state.chat_history.append(("You", user_query))
                    st.session_state.chat_history.append(("Chatbot", response))
                except Exception as e:
                    st.error(f"Error contacting Gemini API: {e}")
            else:
                st.info("Enter a question first.")
    else:
        # Non-blocking notice with useful next steps
        st.info(
            "Gemini API key not configured. Chatbot disabled until a valid key is provided via Streamlit secrets, environment variable, or the 'Connect to Gemini' expander above."
        )

    # Display chat history
    st.subheader("Chat History:")
    for role, message in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**🧑‍⚕️ {role}:** {message}")
        else:
            st.markdown(f"**🤖 {role}:** {message}")


if __name__ == "__main__":
    app()
