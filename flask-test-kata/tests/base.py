from flask.testing import FlaskClient


class TestClient(FlaskClient):
    class Response(object):
        def __init__(self, status, body, headers):
            self.status_code, self.status_text = status.split(" ", 1)
            self.status_code = int(self.status_code)
            self.body = list(body)[0]
            self.headers = dict([(header[0], header[1]) for header in headers])

    def get(self, *args, **kwargs):
        resp = super(TestClient, self).get(*args, **kwargs)
        return TestClient.Response(resp[1], resp[0], resp[2])
