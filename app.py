from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# OpenAI API credentials
OPENAI_API_KEY = "9f21b067af4543849b5fb7b46ed344e4"  # Your actual OpenAI 
OPENAI_API_ENDPOINT = "https://eastus2.api.cognitive.microsoft.com"  # 
DEPLOYMENT_NAME = "gpt-4"  # Your deployment name

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask app is running with OpenAI integration!"})

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    url = f"https://eastus2.api.cognitive.microsoft.com/openai/deployments/gpt-4/completions?api-version=2023-05-15"
    headers = {"Content-Type": "application/json", "api-key": "9f21b067af4543849b5fb7b46ed344e4"}
    payload = {"prompt": prompt, "max_tokens": 100}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)  # Running on port 80 for 

