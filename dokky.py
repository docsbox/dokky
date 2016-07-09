import io
import json
import zipfile
import requests


class DocsboxError(Exception):

    def __init__(self, status_code, response, *args, **kwargs):
        message = "{0}: {1}".format(status_code, response.get("message"))
        super(DocsboxError, self).__init__(message, *args, **kwargs)

class RequestStatus(dict):

    def __init__(self, service, **kwargs):
        self.service = service
        super(RequestStatus, self).__init__(**kwargs)

    def get_status(self):
        url = "{0}{1}".format(self.service.api_url, self.id)
        response = self.service.session.get(url)
        response_json = response.json()
        if response.status_code != 200:
            raise DocsboxError(response.status_code, response_json)
        else:
            self.update(response_json)
            return response_json.get("status")

    def get_result(self):
        if self.status != "finished":
            raise ValueError("Invalid status: '{0}'".format(self.status))
        else:
            url = "{0}{1}".format(self.service.base_url, self.result_url)
            response = self.service.session.get(url)
            if response.status_code != 200:
                raise ValueError("Unknown result_url: {0}".format(self.result_url))
        return zipfile.ZipFile(io.BytesIO(response.content))
    def __getattr__(self, name):
        return self.get(name)

class Docsbox(object):

    def __init__(self, hostname=None, timeout=10):
        """
        @hostname: Docsbox hostname (localhost by default)
        @timeout: Requests timeout (10 seconds by default)
        """
        self.hostname = hostname or "localhost"
        self.session = requests.Session()

    @property
    def api_url(self):
        return "http://{0}/api/v1/".format(self.hostname)

    @property
    def base_url(self):
        return "http://{0}/".format(self.hostname)

    def proccess(self, fileobj, **options):
        """
        @fileobj: file-like object opened in 'rb' mode
        @options: dictionary with options that'll be passed to docsbox
        """
        response = self.session.post(self.api_url, files={
            "file": fileobj.read(),
        }, data={
            "options": json.dumps(options)
        })
        response_json = response.json()
        if response.status_code != 200:
            raise DocsboxError(response.status_code, response_json)
        else:
            return RequestStatus(self, **response_json)

    def __del__(self):
        self.session.close()
