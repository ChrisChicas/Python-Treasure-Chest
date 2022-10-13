from flask import (Blueprint, render_template)
from flask_sqlalchemy import SQLAlchemy

bp = SQLAlchemy()

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.route("/")
def dashboard():
    return render_template("dashboard.html")