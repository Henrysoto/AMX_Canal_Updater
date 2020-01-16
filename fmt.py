import os


class Fmt:
    def __init__(self, version, provider):
        self.version = version
        self.provider = str(provider)

    def get_provider_dir(self):
        return os.path.join('.', 'channels', self.provider.capitalize(), '')
    
    def get_provider_file(self):
        path = self.get_provider_dir()
        return f"{path}{self.provider.lower()}_{self.version}"
