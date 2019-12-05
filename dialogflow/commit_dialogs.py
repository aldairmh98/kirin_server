from git_functions.branch_management import branch_status

def FunctionName():
    print('Hi bro')
    return


def commit_dialog():
    data = {}
    data['id'] = 'commit_text'
    data['request'] = 'Dime el mensaje para guardar tu versión: '
    data['default'] = 'None'
    data['selection'] = False
    return [data]
