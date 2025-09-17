import google.generativeai as genai
from config import GEMINI_API_KEY
from core.memory import save_conversation, recall_context

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

def ask_gemini(user_input):
    try:
        # Get past context
        past_context = recall_context()

        # Build conversation history
        messages = []
        for item in past_context:
            messages.append(f"{item['role'].capitalize()}: {item['content']}")

        full_prompt = "\n".join(messages) + f"\nUser: {user_input}\nAssistant:"

        # Call Gemini
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(full_prompt)

        reply = response.text

        # Save conversation
        save_conversation("user", user_input)
        save_conversation("assistant", reply)

        return reply
    except Exception as e:
        return f"Error: {e}"
