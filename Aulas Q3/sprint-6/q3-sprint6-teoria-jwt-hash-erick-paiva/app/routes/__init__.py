from flask import Flask


def init_app(app: Flask):
    from .user_view import bp_user
    app.register_blueprint(bp_user)

    from .login_view import bp_login
    app.register_blueprint(bp_login)

    # from .protected_view import bp_protected
    # app.register_blueprint(bp_protected)