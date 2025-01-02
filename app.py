from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Azure OpenAI API configuration
GPT_API_KEY = "28JJPEFgA6uHLpAbUiT791H9L4cULayiOirmehOSo8Epu5IlQn1AJQQJ99BAACYeBjFXJ3w3AAABACOG9xsD"
GPT_ENDPOINT = "https://flask-heally-ai.openai.azure.com/"
GPT_DEPLOYMENT_NAME = "gpt-4o"
DALL_E_DEPLOYMENT_NAME = "dalle-2"

HEADERS = {
    "Content-Type": "application/json",
    "api-key": GPT_API_KEY
}

# Route for GPT-4 text generation
@app.route('/generate-text', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get("prompt", "")
    
    payload = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.7
    }
    
    url = f"{GPT_ENDPOINT}openai/deployments/{GPT_DEPLOYMENT_NAME}/completions?api-version=2024-11-20"
    response = requests.post(url, json=payload, headers=HEADERS)
    
    return jsonify(response.json())

# Route for DALL-E image generation
@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get("prompt", "")
    
    payload = {
        "prompt": prompt
    }
    
    url = f"{GPT_ENDPOINT}openai/deployments/{DALL_E_DEPLOYMENT_NAME}/images/generations:submit?api-version=2024-11-20"
    response = requests.post(url, json=payload, headers=HEADERS)
    
    return jsonify(response.json())

# Health Check
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"message": "Flask app is running with GPT-4 and DALL-E 2!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

