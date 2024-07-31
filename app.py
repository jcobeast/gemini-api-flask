from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
import markdown2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure the generative AI API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Define the generation configuration for the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1, 
    "top_k": 1, 
    "max_output_tokens": 1000,
}

# Define the safety settings for content generation
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

# Create an instance of the generative model
model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        question = data.get('question', '')

        if not question:
            return jsonify({'error': 'No question provided'}), 400

        # Prepare the prompt parts for content generation
        prompt_parts = [question]
        
        # Generate the response using the model
        response = model.generate_content(prompt_parts)
        
        # Extract the generated text (assuming it's in 'text' attribute)
        generated_text = response.text
        
        # Format the response into HTML
        formatted_response = markdown2.markdown(generated_text)
        
        # Return the response as JSON
        return jsonify({'response': formatted_response})
    except Exception as e:
        app.logger.error(f"Error generating response: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
    

if __name__ == '__main__':
    app.run(debug=True, port=9000)
