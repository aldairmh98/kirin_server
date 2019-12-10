from git_functions import branch_management

def branch_status():
    return []


def branch_list():
    return []


def branch_creation():
    return [{
        'selection': True, 'response': None, 'request': 'Elija apartir de qué rama quiere crearla',
        'id': 'branch_one', 'default': None, 'list': branch_management.branch_list(None)},
        {
            'selection': False, 'response': None, 'request': 'Escriba el nombre de la nueva rama',
            'id': 'branch_two', 'default': None, 'list': []}]

def branch_deletion():
    _branch_list = branch_management.branch_list(None)
    return [{
        'selection': True, 'response': None, 'request': 'Elija la rama que desea borrar', 'id':'branch_deletion', 'default': None,
        'list': [branch for branch in _branch_list if branch['id'] not in('master', 'develop')]
    }]


def branch_change():
    return [{
        'selection': True, 'response': None, 'request': 'Elija la rama que desea borrar', 'id': 'branch_deletion',
        'default': None,
        'list': branch_management.branch_list(None)
    }]
