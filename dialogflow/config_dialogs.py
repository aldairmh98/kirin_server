def show_user():
    return []

def show_url():
    return []

def change_user():
    return [{'selection': False, 'request': 'Ingrese el nombre del usuario', 'response': None, 'id': 'user_request',
             'default': None}, {
        'selection': False, 'request': 'Ingrese el email del usuario', 'response': None, 'id': 'email_request',
        'default': None
    }]


def change_url():
    return [{'selection': False, 'request': 'Ingrese el URL remoto', 'response': None, 'id': 'url_request',
             'default': None}]


def push():
    return []


def pull():
    return []

