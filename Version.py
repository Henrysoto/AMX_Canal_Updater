import os
from configparser import ConfigParser
from datetime import datetime as dt


class version_controller:
    def __init__(self, version, provider):
        self.version = version
        self.provider = str(provider)
        path_exist = os.path.join('', 'providers', self.provider.capitalize())
        if os.path.isdir(path_exist):
            self.path_to_provider = os.path.join(
                '',
                'providers',
                self.provider.capitalize()
            )
            self.path_to_ini = os.path.join(
                '',
                'providers',
                self.provider.capitalize(),
                'version.ini'
            )
        else:
            self.path_to_ini = None
            self.path_to_provider = None
            raise Exception('__init__: Provider path not found!')

    def get_version_from_file(self, fichier):
        if os.path.isfile(os.path.join('', self.path_to_provider, fichier)):
            return dt.fromtimestamp(
                os.path.getmtime(os.path.join(self.path_to_provider, fichier))
            )
        else:
            raise Exception('get_version_from_file: File not found!')

    def get_latest_version(self):
        if os.path.isfile(self.path_to_ini):
            parser = ConfigParser()
            parser.read(self.path_to_ini)
            if parser.has_section('version'):
                try:
                    return parser['version']['latest']
                except ValueError:
                    raise Exception('get_latest_version: Error while reading'
                                    'version.ini')
            else:
                raise Exception(
                    'get_latest_version: Version section not found in'
                    'version.ini file!'
                )

    def get_specific_version(self, annee, mois, jour):
        pass

    def set_latest_version(self):
        if os.path.isfile(self.path_to_ini):
            parser = ConfigParser()
            parser.read(self.path_to_ini)
            if parser.has_section('version'):
                old = parser['version']['latest']
                new = dt.now().strftime('%d_%m_%Y')
                parser['version']['latest'] = new
                parser['version']['old'] = old
                with open(self.path_to_ini, 'w') as cf:
                    parser.write(cf)
        else:
            actual = self.get_version_from_file(
                f'{self.provider.lower()}_latest.txt'
            )

    def version_to_file(self, version):
        if version:
            return os.path.join(
                self.path_to_provider,
                f'{self.provider.lower()}_{version}'
            )
