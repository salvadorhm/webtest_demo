import web

render = web.template.render('templates/')

class Index():
    def GET(self):
        return render.index()
