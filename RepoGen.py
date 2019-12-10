from git import Repo

class RepoGen:
    __repo = None

    @staticmethod
    def create_repo(self, directory=''):
        if RepoGen.__repo is None:
            print('Hi')
            try:
                RepoGen.__repo = Repo(directory)
            except Exception:
                Repo.init(directory)
                RepoGen.__repo = Repo(directory)
        return RepoGen.__repo
