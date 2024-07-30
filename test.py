from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
import markdown2

app = Flask(__name__)

# Configure the generative AI API key
genai.configure(api_key="AIzaSyA0eg75d9EhcCPkZ5KaewkEd8sbTgAL_9M")

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
    # Get the question from the form data
    question = 'Suggest 5 flask application ideas that are useful in a workplace environment.'
    
    # Prepare the prompt parts for content generation
    prompt_parts = [question]
    
    # Generate the response using the model
    response = model.generate_content(prompt_parts)
    
    res = markdown2.markdown(response.text)
    
    # Return the response as JSON
    return jsonify({'response': res})


if __name__ == '__main__':
    app.run(debug=True, port=9000)