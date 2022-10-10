from flask import (Blueprint, render_template, request)
from . import models

bp = Blueprint("signup", __name__, url_prefix="/signup")

@bp.route("/", methods=["GET", "POST"])
def signup():
    # if request.method == "POST":
    #     code to sign up and post data to db
    
    return render_template("signup.html")