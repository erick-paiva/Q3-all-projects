from app.controllers import world_controller


def world_route(app):
    @app.get("/world")
    def get_view():
        return world_controller.return_world()
