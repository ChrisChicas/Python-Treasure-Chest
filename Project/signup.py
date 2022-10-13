from ftplib import error_reply
from flask import (Blueprint, render_template, request, redirect)
import bcrypt
from . import models

bp = Blueprint("signup", __name__, url_prefix="/signup")

@bp.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        username = request.form["username"]
        password = request.form["password"]
        new_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(12))

        if len(username) < 6 or len(password) < 6:
            return render_template("signup.html", error="Username and Password must be at least 6 characters!")

        user = models.User.query.filter_by(username=username).first()
        if user:
            return render_template("signup.html", error="Username already in use!")

        new_user = models.User(first_name=first_name, last_name=last_name, username=username, password=new_pass)
        models.db.session.add(new_user)
        models.db.session.commit()

        return redirect("/dashboard")
    
    return render_template("signup.html")