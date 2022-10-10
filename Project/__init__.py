from flask import (Flask, render_template, request)
import bcrypt

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("home.html")

    from . import (signup, login)
    app.register_blueprint(signup.bp)
    app.register_blueprint(login.bp)

    return app