import eventlet
eventlet.monkey_patch()

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.threadlocal import get_current_request
from eventlet import sleep


def hello_world(request):
    sleep(5)

    threadlocal_request = get_current_request()
    if threadlocal_request is not request:
        raise ValueError("Incorrect request returned from threadlocal:\n{}\n{}"
                         .format(id(threadlocal_request), id(request)))

    return Response('ok')


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()
