from flask import (Flask, render_template, session, redirect)
from flask_migrate import Migrate
from os import environ

def create_app():
    app = Flask(__name__)

    from . import (models, signup, login, dashboard)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("CONNECTION_STRING")
    app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
    app.config["SOLALCHEMY_TRACK_MODIFICATIONS"] = True
    
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route("/")
    def home():
        if session.get("logged_in"):
            return redirect("/dashboard")
        
        return render_template("home.html")

    app.register_blueprint(signup.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(dashboard.bp)

    return app