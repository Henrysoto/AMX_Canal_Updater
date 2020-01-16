import os
import cherrypy
from cherrypy.lib.static import serve_file
from fmt_csv import CSVFormatter

PROVIDERS = ['Canalsat', 'Bouygues', 'Orange', 'SFR']

class Updater(object):
    @cherrypy.expose
    def index(self):
        return '<a href="/get/canalsat/latest/csv">/get/canalsat/latest/csv</a>'

    @cherrypy.expose
    def get(self, provider, version='latest', fmt='csv'):
        try:
            if provider.capitalize() in PROVIDERS:
                if version == 'latest':
                    if fmt == 'csv':
                        res = CSVFormatter(version, provider)
                        path = res.parse_file()
                        return serve_file(path,
                            "application/x-download",
                            "attachment",
                            os.path.basename(path))
        except:
            raise cherrypy.HTTPError(404)
        #return f"<pre>Provider:\t{provider}\nVersion:\t{version}\nFormat:\t\t{fmt}</pre>"


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080
    })
    cherrypy.quickstart(Updater(), '/')
