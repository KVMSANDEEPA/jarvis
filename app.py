from flask import Flask, render_template, request, jsonify
from core.commands import execute_command
from core.memory import init_db

app = Flask(__name__)

# Initialize database
init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    user_input = data.get("message")
    if not user_input:
        return jsonify({"reply": "No input detected."})
    reply = execute_command(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
