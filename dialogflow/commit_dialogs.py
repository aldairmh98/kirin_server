from git_functions.branch_management import branch_status
from git_functions import commit_management


def FunctionName():
    print('Hi bro')
    return


def commit_dialog():
    return [{'id': 'commit_text', 'request': 'Dime el mensaje para guardar tu versión: ', 'default': 'None',
            'selection': False, 'response': ''}]


def commit_list():
    return []


def commit_back():
    return [{'selection': True, 'response': None, 'request': 'Selecciona el commit al que quiera regresar',
                    'default': None, 'id': 'commit_list', 'list': commit_management.commit_list({})}]
