from flask import Blueprint, Flask

# bp_api = Blueprint("api", __name__, url_prefix="/aa")

def init_app(app: Flask):
    # app.register_blueprint(bp_api)
    from .categorie_blueprint import bp as bp_categories
    from .task_blueprint import bp as bp_tasks
    app.register_blueprint(bp_categories)
    app.register_blueprint(bp_tasks)
    