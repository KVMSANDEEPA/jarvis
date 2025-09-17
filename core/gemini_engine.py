import google.generativeai as genai
from config import GEMINI_API_KEY
from core.memory import save_conversation, recall_context

genai.configure(api_key=GEMINI_API_KEY)

def ask_gemini(prompt):
    try:
        past = recall_context()
        full_prompt = "\n".join([f"{p['role']}: {p['content']}" for p in past])
        full_prompt += f"\nUser: {prompt}\nAssistant:"
        model = genai.GenerativeModel("gemini-pro")
        resp = model.generate_content(full_prompt)
        reply = resp.text
        save_conversation("user", prompt)
        save_conversation("assistant", reply)
        return reply
    except Exception as e:
        return f"Gemini AI Error: {e}"
