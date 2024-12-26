from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        text = file.read().decode('utf-8')
        tts = gTTS(text=text, lang='en')
        
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
            audio_file_path = temp_file.name
            tts.save(audio_file_path)
        
        return send_file(audio_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)