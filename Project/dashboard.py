from flask import (Blueprint, render_template, redirect, request, session)
from . import models

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.route("/")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/login")

    chests = models.Chest.query.filter_by(user_id=session["user"]["user_id"]).all()
    return render_template("dashboard.html", user=session.get("user"), chests=chests)

@bp.route("/chests", methods=["GET", "POST"])
def new_chest():
    if not session.get("logged_in"):
        return redirect("/login")

    if request.method == "POST":
        chest_name = request.form["chest_name"]

        new_chest = models.Chest(chest_name=chest_name, user_id=session["user"]["user_id"])
        models.db.session.add(new_chest)
        models.db.session.commit()

        return redirect("/dashboard")

@bp.route("/chests/<string:name>", methods=["GET", "POST"])
def show_chest(name):
    if not session.get("logged_in"):
        return redirect("/login")

    chest = models.Chest.query.filter_by(user_id=session["user"]["user_id"], chest_name=name).first()
    treasures = models.Treasure.query.filter_by(chest_id=chest.chest_id).all()

    if request.method == "POST": 
        method = request.form["method"]

        if method == "PUT":
            chest_name = request.form["chest_name"]

            chest.chest_name = chest_name
            models.db.session.commit()

            return redirect("/dashboard")
        elif method == "DELETE":
            models.db.session.delete(chest)
            models.db.session.commit()

            return redirect("/dashboard")  
    # Post method made to accomodate html forms

    return render_template("chests/show.html", chest=chest, treasures=treasures)

@bp.route("/chests/<string:name>/edit")
def edit_chest(name):
    if not session.get("logged_in"):
        return redirect("/login")

    chest = models.Chest.query.filter_by(user_id=session["user"]["user_id"], chest_name=name).first()

    return render_template("chests/edit.html", chest=chest)


@bp.route("/logout", methods=["POST"])
def logout():
    if not session.get("logged_in"):
        return redirect("/login")

    if request.method == "POST":
        session.clear()

        return redirect("/")