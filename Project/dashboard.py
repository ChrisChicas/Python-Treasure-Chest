from flask import (Blueprint, render_template, redirect, request)
from . import pyjwt

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

# Add jwt or authentication check to see if logged in, else dashboard should be inaccessible and should simply re route to home page.

@bp.route("/")
def dashboard():
    print(request.headers)
    print(pyjwt.token_check())
    # if token == None:
    #     return redirect("/")

    return render_template("dashboard.html")