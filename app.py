import requests
from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)

@app.route("/chat", methods=['POST'])
def chat():
    user_message = request.json.get("message")
    url = "https://ai.hackclub.com/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
    "messages": [
        {
            "role": "user",
            "content": f"Reply as a therapist to: {user_message}. Use a friendly and supportive tone and keep it short",
        }
    ],
    "reasoning_format": "parsed"
}
    response = requests.post(url, json=data, headers=headers)
    ai_response = response.json()
    ai_message = ai_response.get("choices", [{}])[0].get("message", {}).get("content")
    print(ai_message)
    return jsonify({"ai_response": ai_message})

@app.route("/")
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
