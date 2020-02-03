import os
import cherrypy
from cherrypy.lib.static import serve_file
from CSV import CSVFormatter
from Version import version_controller


class Updater(object):
    @cherrypy.expose
    def index(self):
        return '<a href="/get/canalsat/latest/csv">canalsat/latest/csv</a>'

    @cherrypy.expose
    def get(self, provider, version='latest', fmt='csv'):
        ver = version_controller(version, provider)
        if version == 'latest':
            fichier = f'{ver.version_to_file(ver.get_latest_version())}.{fmt}'
        else:
            fichier = f'{ver.version_to_file(version)}.{fmt}'
        if os.path.isfile(fichier):
            with open(fichier, 'rb') as fd:
                return fd.read()
        else:
            raise cherrypy.HTTPError(404)


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080
    })
    cherrypy.quickstart(Updater(), '/')
