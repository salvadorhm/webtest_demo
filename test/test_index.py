from webtest import TestApp as ta
from app import app as application

class TestIndex():
    def test_get(self):
        index = open("templates/index.html","r")
        middleware = []
        app = ta(application.wsgifunc(*middleware))
        response = app.get('/')

        assert response.status_code == 200
        assert response.text == index.read()
