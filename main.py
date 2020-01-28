import os
import cherrypy
from cherrypy.lib.static import serve_file
from fmt_csv import CSVFormatter

PROVIDERS = ['Canalsat', 'Bouygues', 'Orange', 'SFR']


class Updater(object):
    @cherrypy.expose
    def index(self):
        return '<a href="/get/canalsat/latest/csv">canalsat/latest/csv</a>'

    @cherrypy.expose
    def get(self, provider, version='latest', fmt='csv'):
        pass


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080
    })
    cherrypy.quickstart(Updater(), '/')
