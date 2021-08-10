import web
import index

urls = (
    '/', 'index.Index',
    '/login','login.Login'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
