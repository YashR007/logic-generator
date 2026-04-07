from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini API
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return jsonify({'message': 'Logic Circuit Generator Backend'})

@app.route('/api/generate', methods=['POST'])
def generate_circuit():
    """
    Generate logic circuit based on user requirements using Gemini AI.
    """
    try:
        data = request.json
        requirements = data.get('requirements', '')
        
        if not requirements:
            return jsonify({'error': 'Requirements not provided'}), 400
        
        # Create prompt for Gemini
        prompt = f"""You are an expert in digital logic circuits and Boolean algebra.
        Based on the following requirements, generate:
        1. A Boolean expression
        2. A truth table
        3. A circuit diagram description (in text format)
        4. Optimization suggestions
        
        Requirements: {requirements}
        
        Please provide the response in a structured JSON format."""
        
        # Call Gemini API
        response = model.generate_content(prompt)
        
        return jsonify({
            'status': 'success',
            'result': response.text
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)