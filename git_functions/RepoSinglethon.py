from git import Repo


class RepoSinglethon:
    instance = None

    class __RepoSinglethon:
        def __init__(self):
            return

        def __str__(self):
            return repr(self)

    def __init__(self):
        if not self.instance:
            try:
                self.instance = Repo('C:/Users/aldai/Desktop/Prueba_KIRIN')
            except Exception:
                print(Exception.__name__)
                Repo.init('C:/Users/aldai/Desktop/Prueba_KIRIN')
                self.instance = Repo('C:/Users/aldai/Desktop/Prueba_KIRIN')

    def __getattr__(self):
        getattr(self.instance)
