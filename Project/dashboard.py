from flask import (Blueprint, render_template)
from flask_sqlalchemy import SQLAlchemy

bp = SQLAlchemy()

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

# Add jwt or authentication check to see if logged in, else dashboard should be inaccessible and should simply re route to home page.

@bp.route("/")
def dashboard():
    return render_template("dashboard.html")