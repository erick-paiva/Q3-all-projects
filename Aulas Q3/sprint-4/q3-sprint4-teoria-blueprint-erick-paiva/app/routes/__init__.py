from app.routes.hello_route import hello_route
from app.routes.world_route import world_route


def init_app(app):
    hello_route(app)
    world_route(app)
