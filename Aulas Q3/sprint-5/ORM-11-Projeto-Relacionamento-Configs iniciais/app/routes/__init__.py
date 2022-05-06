from flask import Flask


def init_app(app: Flask):
    from .estado_blueprint import bp as bp_estados
    app.register_blueprint(bp_estados)
    
    from .capital_blueprint import bp as bp_capitais 
    app.register_blueprint(bp_capitais)
    from .regiao_blueprint import bp as bp_regioes
    app.register_blueprint(bp_regioes)
    from .bacia_hidro_blueprint import bp as bp_bacias
    app.register_blueprint(bp_bacias)
    