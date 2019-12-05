from git import Repo

repo = Repo('C:/Users/aldai/desarrollo/assistant_kirin/tutorial1')


def branch_creation(messageBody):
    print(messageBody)
    return


def branch_status(messageBody = {}):
    changed_files = [{'path': item.a_path, 'status': item.change_type} for item in repo.index.diff(None) if item.a_path[0] != '.']

    for item in repo.untracked_files:
        if item[0] is not '.':
            changed_files.append({'path': item, 'status': 'A'})
    return changed_files


def branch_list(messageBody):
    return


def branch_deletion(messageBody):
    return


def branch_change(messageBody):
    return


def branch_merge(messageBody):
    return


