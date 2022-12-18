from flask import (Flask, render_template, session, redirect)
from flask_migrate import Migrate
from os import environ

def create_app():
    application = Flask(__name__)

    from . import (models, signup, login, dashboard)
    application.config["SQLALCHEMY_DATABASE_URI"] = environ.get("CONNECTION_STRING")
    application.config["SECRET_KEY"] = environ.get("SECRET_KEY")
    application.config["SOLALCHEMY_TRACK_MODIFICATIONS"] = True
    
    models.db.init_app(application)
    migrate = Migrate(application, models.db)

    @application.route("/")
    def home():
        if session.get("logged_in"):
            return redirect("/dashboard")
        
        return render_template("home.html")

    application.register_blueprint(signup.bp)
    application.register_blueprint(login.bp)
    application.register_blueprint(dashboard.bp)

    return application