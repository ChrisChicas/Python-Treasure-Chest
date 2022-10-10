from flask import (Blueprint, render_template, request)
from . import models

bp = Blueprint("login", __name__, url_prefix="/login")

@bp.route("/", methods=["GET", "POST"])
def login():
    # if request.method == "POST":
    #     code to sign up and post data to db
    
    return render_template("login.html")