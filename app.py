from flask import Flask, request, jsonify
from main import DeepResearchSystem
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize your DeepResearchSystem with environment variables
system = DeepResearchSystem(
    tavily_api_key=os.getenv("TAVILY_API_KEY"),
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

@app.route('/')
def home():
    return "Welcome to the Deep Research Bot!"

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response for favicon requests

def format_answer(text):
    clean_text = text.strip()
    clean_text = clean_text.replace("\\n", "\n")  # Fix escaped newlines
    clean_text = clean_text.replace("\n\n", "\n")  # Clean double newlines
    return clean_text

@app.route('/ask', methods=['POST'])
def ask_bot():
    data = request.json
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'No Query Provided.'}), 400

    answer = system.run(query)
    return jsonify({'answer': format_answer(str(answer))})

if __name__ == '__main__':
    app.run(debug=True)
