from flask import (Blueprint, render_template, redirect, request, session)
from . import models

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.route("/")
def dashboard():
    if not session.get("logged_in"):
        return redirect("/login")

    chests = models.Chest.query.filter_by(user_id=session["user"]["user_id"]).all()
    return render_template("dashboard.html", user=session.get("user"), chests=chests)

@bp.route("/chests", methods=["POST"])
def new_chest():
    if not session.get("logged_in"):
        return redirect("/login")

    if request.method == "POST":
        chest_name = request.form["chest_name"]

        new_chest = models.Chest(chest_name=chest_name, user_id=session["user"]["user_id"])
        models.db.session.add(new_chest)
        models.db.session.commit()

        return redirect("/dashboard")

@bp.route("/chests/<int:chest_id>", methods=["GET", "POST"])
def show_and_edit_chest(chest_id):
    if not session.get("logged_in"):
        return redirect("/login")

    chest = models.Chest.query.filter_by(chest_id=chest_id).first()
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

@bp.route("/chests/<int:chest_id>/edit")
def edit_chest_page(chest_id):
    if not session.get("logged_in"):
        return redirect("/login")

    chest = models.Chest.query.filter_by(chest_id=chest_id).first()

    return render_template("chests/edit.html", chest=chest)

@bp.route("/chests/<int:chest_id>/treasures", methods=["POST"])
def new_treasure(chest_id):
    if not session.get("logged_in"):
        return redirect("/login")

    if request.method == "POST":
        treasure_title = request.form["treasure_title"]
        treasure_details = request.form["treasure_details"]

        new_treasure = models.Treasure(treasure_title=treasure_title, treasure_details=treasure_details, chest_id=chest_id)
        models.db.session.add(new_treasure)
        models.db.session.commit()

        return redirect(f"/dashboard/chests/{chest_id}")

@bp.route("/chests/<int:chest_id>/treasures/<int:treasure_id>", methods=["POST"])
def edit_treasure(chest_id, treasure_id):
    if not session.get("logged_in"):
        return redirect("/login")

    treasure = models.Treasure.query.filter_by(treasure_id=treasure_id).first()

    if request.method == "POST": 
        method = request.form["method"]

        if method == "PUT":
            treasure_title = request.form["treasure_title"]
            treasure_details = request.form["treasure_details"]

            treasure.treasure_title = treasure_title
            treasure.treasure_details = treasure_details
            models.db.session.commit()

            return redirect(f"/dashboard/chests/{chest_id}")
        elif method == "DELETE":
            models.db.session.delete(treasure)
            models.db.session.commit()

            return redirect(f"/dashboard/chests/{chest_id}")  
    # Post method made to accomodate html forms

@bp.route("/chests/<int:chest_id>/treasures/<int:treasure_id>/edit")
def edit_treasure_page(chest_id, treasure_id):
    if not session.get("logged_in"):
        return redirect("/login")

    treasure = models.Treasure.query.filter_by(treasure_id=treasure_id).first()

    return render_template("treasures/edit.html", treasure=treasure)

@bp.route("/logout", methods=["POST"])
def logout():
    if not session.get("logged_in"):
        return redirect("/login")

    if request.method == "POST":
        session.clear()

        return redirect("/")