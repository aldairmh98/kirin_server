from flask import Flask, jsonify
from flask import request
import os
from werkzeug.utils import secure_filename
import speech_recognition as sr

app = Flask(__name__)


@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet', methods=['POST'])
def say_hello():
    audio = request.files['audio']
    audio.save('./audio.wav')
    r = sr.Recognizer()
    audiosound = sr.AudioFile('./audio.wav')
    with audiosound as source:
      r.adjust_for_ambient_noise(source)
      audiosound2 = r.record(source)
    print(r.recognize_google(audiosound2, language='es-MX'))
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    print('RECBIBIDO', audio.filename)
    return response


if __name__ == '__main__':
    app.run(debug=True)