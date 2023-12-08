from misskey import Misskey
import os


class MiAlgorithm:
    def __init__(self, domain, token=None):
        self.api = Misskey(domain, i=token or os.environ.get('TOKEN'))

    def run(self):
        pass
