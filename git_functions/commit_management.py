from git import Repo
from git_functions.branch_management import branch_status
from datetime import datetime


repo = Repo('C:/Users/aldai/desarrollo/assistant_kirin/tutorial1')


def commit_list(messageBody):
    commits = list(repo.iter_commits(max_count=10))
    for c in commits:
        print(c)
    return [{'sha': c.__str__(), 'name': str(c.author), 'email': c.author.email, 'msg': c.message} for c in commits]

def revert(messageBody):
    repo.git.revert(messageBody['sha'], no_edit=True)
    return

def version(messageBody):
    files_list = branch_status()
    modified_file_list = [_file['path'] for _file in files_list if _file['status'] != 'D']
    removed_file_list = [_file['path'] for _file in files_list if _file['status'] == 'D']
    repo.index.add(modified_file_list)
    if len(removed_file_list) > 0:
        repo.index.remove(removed_file_list, True, r=True)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    repo.index.commit(str(messageBody['message']) + ' Versionado el: ' + dt_string)
    return
