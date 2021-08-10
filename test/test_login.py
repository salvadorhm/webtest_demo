from webtest import TestApp as ta
from app import app as application

class TestLogin():
    def test_get(self):
        login = open('templates/login.html','r')
        
        middleware = []
        app = ta(application.wsgifunc(*middleware))

        response = app.get('/login')

        assert response.status_code == 200
        assert response.text == login.read()

    def test_post(self):
        login = open('templates/login.html','r')
        index = open('templates/index.html','r')

        middleware = []
        app = ta(application.wsgifunc(*middleware))

        # Login email y password correctos
        response = app.post('/login',{'email':'hola@email.com','password':'123456'})

        assert response.status_code == 200
        assert response.text == index.read()

        # Login email y password incorrectos
        response = app.post('/login',{'email':'hola@email.com','password':'1234567'})
        assert response.status_code == 200
        assert response.text == login.read()
