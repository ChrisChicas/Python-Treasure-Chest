from flask import (Blueprint, render_template, request, redirect, session)
import bcrypt
from . import models

bp = Blueprint("login", __name__, url_prefix="/login")

@bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = models.User.query.filter_by(username=username).first()
        if user:
            if bcrypt.checkpw(password.encode("utf-8"), user.password):
                session["logged_in"] = True
                session["user"] = {"user_id": user.user_id, "username": user.username}
                return redirect("/dashboard")
            else:
                return render_template("authentication/login.html", error="Username or Password incorrect!")
        else:
            return render_template("authentication/login.html", error="Username or Password incorrect!")
    
    if session.get("logged_in"):
        return redirect("/dashboard")
        
    return render_template("authentication/login.html")