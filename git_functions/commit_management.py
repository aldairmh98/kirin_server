from git import Repo
from git_functions.branch_management import branch_status
repo = Repo('C:/Users/aldai/desarrollo/assistant_kirin/tutorial1')


def commit_list(messageBody):
    commits =  list(repo.iter_commits(max_count=1))
    for c in commits:
        print(c)
    return [{'name': str(c.author), 'email': c.author.email, 'msg': c.message} for c in commits]


def version(messageBody):
    repo.index.add(branch_status())
    repo.index.commit(str(messageBody['message']))
    return
