from git import Repo
from git_functions.branch_management import branch_status
repo = Repo('C:/Users/aldai/desarrollo/assistant_kirin/tutorial1')


def commit_list(messageBody):
    commits =  list(repo.iter_commits(max_count=1))
    for c in commits:
        print(c)
    return [{'name': str(c.author), 'email': c.author.email, 'msg': c.message} for c in commits]


def version(messageBody):
    files_list = branch_status()
    modified_file_list = [_file['path'] for _file in files_list if _file['status'] != 'D']
    removed_file_list = [_file['path'] for _file in files_list if _file['status'] == 'D']
    repo.index.add(modified_file_list)
    repo.index.remove(removed_file_list, True, r=True)
    repo.index.commit(str(messageBody['message']))
    return
