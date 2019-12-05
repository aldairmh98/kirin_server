import asyncio

from flask import Flask, jsonify
from flask import request
from rasa.core.agent import Agent
import os
from werkzeug.utils import secure_filename
import speech_recognition as sr
from git_functions import branch_management, commit_management
from dialogflow import commit_dialogs

agent = Agent.load("./models/nlu.tar.gz")

app = Flask(__name__)

intent_activities = {
    'branch_creation': branch_management.branch_creation,
    'branch_status': branch_management.branch_status,
    'commit_list': commit_management.commit_list,
    'version': commit_management.version,
    'revert': commit_management.revert
}

intent_dialog_flow = {
    'version': commit_dialogs.commit_dialog
}

commit_management.revert(messageBody={'sha': '40fa5972138915e0f86d3d41fc884ec1a22b55c1'})

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
    utterance = ''
    if type_ == 'text':
        utterance = request.json['message']
    else:
        utterance = 'onProof'
        # HERE IT GOES SPEECH RECOGNITION
    the_message = asyncio.run(agent.parse_message_using_nlu_interpreter(utterance))
    return jsonify({'intent_name': the_message['intent']['name'], 'dialog_flow': intent_dialog_flow[the_message['intent']['name']]()}), 202


@app.route('/intent/<intent_name>', methods=['POST'])
def task_automation(intent_name):
    intent_name = request.view_args['intent_name']
    response = jsonify(intent_activities[intent_name](request.json))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200


if __name__ == '__main__':
    app.run(debug=True)