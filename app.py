import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/chat", methods=['POST'])
def chat():
    user_message = request.json.get("message")
    url = "https://ai.hackclub.com/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "messages": [
            {"role": "user", "content": f"dont mention <think> and </think> in the prompt and keep it short talk like a therapist: {user_message}"}
        ]
    }
    response = requests.post(url, json=data, headers=headers)
    ai_response = response.json()
    ai_message = ai_response.get("choices", [{}])[0].get("message", {}).get("content")
    print(ai_message)
    return jsonify({"ai_response": ai_message})

if __name__ == "__main__":
    app.run(debug=True)