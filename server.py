from flask import Flask, jsonify
from flask import request
import os
from werkzeug.utils import secure_filename
import speech_recognition as sr
from git_functions import branch_management, commit_management
app = Flask(__name__)

intent_activities = {
    'branch_creation': branch_management.branch_creation,
    'branch_status': branch_management.branch_status,
    'commit_list': commit_management.commit_list,
    'version': commit_management.version
}


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


@app.route('/intent/<intent_name>', methods=['POST'])
def taskAutomation(intent_name):
    intent_name = request.view_args['intent_name']
    response = jsonify(intent_activities[intent_name](request.json))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200


if __name__ == '__main__':
    app.run(debug=True)