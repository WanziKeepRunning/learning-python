import sys


from router import Router
from httpserver import serve_forever
from web import render


def index():
    return '<title>Index</title><h1>It works</h1>'


def hello(username):
    # !! NOT SAFE !!
    return '<p>Nice to meet you <strong>{}</strong> !</p>'.format(username)


def about():
    return """It's just a very simple demo for web server"""


def greet():
    import time
    return render('greet.html', {'now': time.time()})


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    address = ('localhost', port)
    router = Router((
        ('/', index),
        ('/hello/(?P<username>\w+)', hello),
        ('/about', about),
        ('/greeting', greet),
        ))

    serve_forever(address, router)
