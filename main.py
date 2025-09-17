import sys
import os
import threading

# Ensure 'core' can be imported
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_ROOT)

from core.memory import init_db
from core.speech import listen, speak
from core.commands import execute_command
from flask import Flask, render_template, request, jsonify

# Initialize database
init_db()

# Flask app
app = Flask(__name__, template_folder="web/templates", static_folder="web/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    message = data.get("message", "")
    if not message:
        return jsonify({"reply": "Please type a command."})
    reply = execute_command(message)
    return jsonify({"reply": reply})

# Voice assistant loop
def voice_loop():
    speak("Hello, I am Jarvis. Ready for your command.")
    while True:
        cmd = listen()
        if not cmd:
            continue
        if "exit" in cmd or "quit" in cmd:
            speak("Goodbye!")
            break
        reply = execute_command(cmd)
        speak(reply)

# Run web + voice in parallel
if __name__ == "__main__":
    threading.Thread(target=voice_loop, daemon=True).start()
    app.run(debug=True, port=5000)
