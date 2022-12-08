from sqlalchemy.dialects import postgresql
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    username = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.LargeBinary, nullable = False)
    role = db.Column(postgresql.ENUM("user", "admin", name="user_roles"), nullable = False, default = "user")
    chests = db.relationship("Chest", backref = "user")

class Chest(db.Model):
    __tablename__ = "chests"

    chest_id = db.Column(db.Integer, primary_key = True)
    chest_name = db.Column(db.String(100), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)
    treasures = db.relationship("Treasure", backref = "chest")

class Treasure(db.Model):
    __tablename__ = "treasures"

    treasure_id = db.Column(db.Integer, primary_key = True)
    treasure_title = db.Column(db.String(100), nullable = False)
    treasure_details = db.Column(db.Text, nullable = False)
    chest_id = db.Column(db.Integer, db.ForeignKey("chests.chest_id"), nullable = False)