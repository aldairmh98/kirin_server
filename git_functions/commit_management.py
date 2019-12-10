from git_functions.branch_management import branch_status
from datetime import datetime
from git import Repo
import sys

if len(sys.argv) < 2:
    exit()
else:
    directory = sys.argv[1].replace("\\", '/')
    try:
        repo = Repo(directory)
    except Exception:
        Repo.init(directory)
        repo = Repo(directory)


def commit_list(messageBody):
    commits = list(repo.iter_commits(max_count=10))
    return [{'id': c.__str__(), 'message': 'autor: '+str(c.author) + ' email: ' + c.author.email + ' description: ' + c.message} for c in commits]


def reset(messageBody):
    #Keep Changes
    repo.git.reset(messageBody['dialog_flow'][0]['response'], hard=True)
    return


def version(messageBody):
    """messageBody = {
    "dialog_flow": [
        {
        "default": "None",
        "id": "commit_text",
        "request": "Dime el mensaje para guardar tu versión: ",
        "response": "",
        "selection": false
        }
    ],
    "intent_name": "version"
    }"""
    message = ''
    for dialog in messageBody['dialog_flow']:
        message = dialog['response']
    files_list = branch_status()
    modified_file_list = [_file['id'] for _file in files_list if _file['status'] != 'D']
    removed_file_list = [_file['id'] for _file in files_list if _file['status'] == 'D']
    repo.index.add(modified_file_list)
    if len(removed_file_list) > 0:
        repo.index.remove(removed_file_list, True, r=True)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    repo.index.commit(str(message) + ' Versionado el: ' + dt_string)
    return
