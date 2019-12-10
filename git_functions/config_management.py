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

def show_user(messageBody= {}):
    user = 'email: ' + repo.config_reader().get_value('user', 'email') + ' nombre de usuario: ' \
           + repo.config_reader().get_value('user', 'name')
    raise Exception(user)
    return

def change_user(messageBody):
    user = messageBody['dialog_flow'][0]['response']
    email = messageBody['dialog_flow'][1]['response']
    with repo.config_writer() as wr:
        wr.set_value('user', 'email', email).release()
        wr.set_value('user', 'name', user).release()
    raise Exception('Usuario actualizado! :)')

def show_url(messageBody):
    if len(repo.remotes) == 0:
        raise Exception('No tiene url configurado')
    else:
        raise Exception(repo.remotes.origin.url)

def change_url(messageBody):
    if len(repo.remotes) == 0:
        repo.create_remote('origin', messageBody['dialog_flow'][0]['response'])
    else:
        repo.delete_remote('origin')
        repo.create_remote('origin', messageBody['dialog_flow'][0]['response'])
    return


def push(messageBody):
    repo.git.push('origin', repo.active_branch.name)
    return


def pull(messageBody):
    repo.git.pull('origin', repo.active_branch.name)
    return