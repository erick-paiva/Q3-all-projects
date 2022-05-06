from app.controllers import hello_controller


def hello_route(app):
    @app.get("/hello")
    def get_hello():
        return hello_controller.return_hello()
