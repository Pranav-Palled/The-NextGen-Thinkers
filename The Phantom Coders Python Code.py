from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Replace with your desired file upload directory
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/process', methods=['POST'])
def process_file():
  file = request.files['file']
  question = request.form['question']

  # Save the file to the upload folder
  filename = secure_filename(file.filename)
  file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

  # Process the file and answer the question (simplified example)
  # In reality, this would involve complex NLP techniques
  with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r') as f:
    text = f.read()

  # Use a simplified approach for now
  if "findings" in question:
    answer = "The main findings of the paper are..."  # Replace with actual extraction
  elif "data collection" in question:
    answer = "The data was collected through..."  # Replace with actual extraction
  else:
    answer = "I couldn't find a specific answer to that question."

  os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Delete the file

  return jsonify({'answer': answer})

if __name__ == '__main__':
  app.run(debug=True)