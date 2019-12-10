import sys
from git import Repo

if len(sys.argv) < 2:
    exit()
else:
    directory = sys.argv[1].replace("\\", '/')
    try:
        repo = Repo(directory)
    except Exception:
        Repo.init(directory)
        repo = Repo(directory)


def branch_creation(messageBody):
    if len(branch_status(None)) > 0:
        raise Exception('Tiene cambios pendientes, debe guardarlos primero :)')
    repo.git.checkout(messageBody['dialog_flow'][0]['response'])
    try:
        repo.git.checkout('-b', messageBody['dialog_flow'][1]['response'])
    except Exception:
        raise Exception('Ya existe una rama con ese nombre :)')
    return


def branch_status(messageBody = {}):
    changed_files = [{'id': item.a_path,'status': item.change_type, 'message': item.a_path + ' status: '+ 'Modificado' if item.change_type == 'M' else 'Creado' if item.change_type == 'A' else 'Borrado' } for item in repo.index.diff(None) if item.a_path[0] != '.']

    for item in repo.untracked_files:
        if item[0] is not '.':
            changed_files.append({'id': item, 'status': 'A', 'message': item + ' status: Creado'})
    return changed_files


def branch_list(messageBody):
    current = repo.active_branch.name
    _branch_list = []
    _branch_list.append({'id': current, 'message': current + ' (ACTIVA)'})
    for branch in repo.branches:
        if current != branch.name:
            _branch_list.append({'id': branch.name, 'message': branch.name})
    return _branch_list


def branch_deletion(messageBody):
    current = repo.active_branch.name
    if current == messageBody['dialog_flow'][0]['response']:
        raise Exception('Está borrando una rama la cual está activa, primero cambie a otra rama')
    repo.delete_head(messageBody['dialog_flow'][0]['response'])
    return


def branch_change(messageBody):
    if len(branch_status(None)) > 0:
        raise Exception('Tiene cambios pendientes, debe guardarlos primero :)')
    repo.git.checkout(messageBody['dialog_flow'][0]['response'])
    return


def branch_merge(messageBody):
    return


