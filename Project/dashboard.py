from flask import (Blueprint, render_template, redirect, request, session)

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.route("/")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/login")

    return render_template("dashboard.html", user=session["user"]["username"])

@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")