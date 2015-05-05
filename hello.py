from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello world!')

def main():
    config = Configurator()
    config.add_route('hello', '/hello')
    config.add_view(hello_world, route_name='hello')
    config.add_route('hello_with_slash', '/hello/')
    config.add_view(hello_world, route_name='hello_with_slash')
    app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
