import asyncio

from flask import Flask, jsonify
from flask import request
from rasa.core.agent import Agent
import os
from werkzeug.utils import secure_filename
import speech_recognition as sr
from git_functions import branch_management, commit_management

agent = Agent.load("./models/nlu.tar.gz")

app = Flask(__name__)

intent_activities = {
    'branch_creation': branch_management.branch_creation,
    'branch_status': branch_management.branch_status,
    'commit_list': commit_management.commit_list,
    'version': commit_management.version
}

intent_dialog_flow = {
    ''
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


@app.route('/intentRecognition', methods=['POST'])
def intent_recognition():
    type_ = request.args.get('type')
    print(type_)
    utterance = ''
    if type_ == 'text':
        utterance = request.json['message']
    else:
        utterance = 'onProof'
        # HERE IT GOES SPEECH RECOGNITION
    the_message = asyncio.run(agent.parse_message_using_nlu_interpreter(utterance))
    print(the_message)
    return jsonify({'id': 'commit_text', 'request': 'Escribe el mensaje de tu commit:', 'default': '', 'response': '',
                    'selection': False, 'list_id': -1})


@app.route('/intent/<intent_name>', methods=['POST'])
def taskAutomation(intent_name):
    intent_name = request.view_args['intent_name']
    response = jsonify(intent_activities[intent_name](request.json))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200


if __name__ == '__main__':
    app.run(debug=True)