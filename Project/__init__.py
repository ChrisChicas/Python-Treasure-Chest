from flask import (Flask, render_template)
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    from . import (_config, models, signup, login, dashboard)
    app.config["SQLALCHEMY_DATABASE_URI"] = _config.connection_string
    app.config["SECRET_KEY"] = _config.secret_key
    app.config["SOLALCHEMY_TRACK_MODIFICATIONS"] = True
    

    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route("/")
    def home():
        return render_template("home.html")

    app.register_blueprint(signup.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(dashboard.bp)

    return app