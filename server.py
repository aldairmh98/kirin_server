import asyncio
import sys
from RepoGen import RepoGen
from git import Repo
from flask import Flask, jsonify
from flask import request, make_response
from rasa.core.agent import Agent

from git_functions import branch_management, commit_management, config_management
from dialogflow import commit_dialogs, branch_dialogs, config_dialogs
from flask_cors import CORS
import speech_rec_pruebas

repo = None
if len(sys.argv) < 2:
    exit()
else:
    directory = sys.argv[1].replace("\\", '/')
    try:
        repo = Repo(directory)
    except Exception:
        Repo.init(directory)
        repo = Repo(directory)

if __name__ == '__main__':

    agent = Agent.load("./models/nlu.tar.gz")

    app = Flask(__name__)

    CORS(app)

    intent_activities = {
        'branch_creation': branch_management.branch_creation,
        'branch_status': branch_management.branch_status,
        'commit_list': commit_management.commit_list,
        'version': commit_management.version,
        'commit_back': commit_management.reset,
        'branch_list': branch_management.branch_list,
        'branch_deletion': branch_management.branch_deletion,
        'branch_change': branch_management.branch_change,
        'show_user': config_management.show_user,
        'change_user': config_management.change_user,
        'show_url': config_management.show_url,
        'change_url': config_management.change_url,
        'push': config_management.push,
        'pull': config_management.pull
    }

    intent_dialog_flow = {
        'version': commit_dialogs.commit_dialog,
        'commit_list': commit_dialogs.commit_list,
        'commit_back': commit_dialogs.commit_back,
        'branch_status': branch_dialogs.branch_status,
        'branch_list': branch_dialogs.branch_list,
        'branch_creation': branch_dialogs.branch_creation,
        'branch_deletion': branch_dialogs.branch_deletion,
        'branch_change': branch_dialogs.branch_change,
        'show_user': config_dialogs.show_user,
        'change_user': config_dialogs.change_user,
        'show_url': config_dialogs.show_url,
        'change_url': config_dialogs.change_url,
        'push': config_dialogs.push,
        'pull': config_dialogs.pull
    }


    @app.route('/proof', methods=['POST'])
    def index():
        print(request.json)
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


    @app.route('/greet', methods=['POST'])
    def say_hello():
        audio = request.files['audio']
        #audio.save('audio.wav')
        response = jsonify({'text': speech_rec_pruebas.recognizer(audio=audio)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200


    @app.route('/intentRecognition', methods=['POST'])
    def intent_recognition():
        type_ = request.args.get('type')
        utterance = ''
        if type_ == 'text':
            print(request.json)
            utterance = request.json['message']
        else:
            utterance = 'onProof'
            # HERE IT GOES SPEECH RECOGNITION
        the_message = asyncio.run(agent.parse_message_using_nlu_interpreter(utterance))
        response = jsonify({'intent_name': the_message['intent']['name'],
                            'dialog_flow': intent_dialog_flow[the_message['intent']['name']]()})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response, 202


    @app.route('/intent/<intent_name>', methods=['POST'])
    def task_automation(intent_name):
        print(request.json)
        intent_name = request.view_args['intent_name']
        try:
            response = jsonify(intent_activities[intent_name](request.json))
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 200
        except Exception as error:
            response = jsonify({'message': error.__str__()})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 409
    app.run(host='0.0.0.0', debug=True)

