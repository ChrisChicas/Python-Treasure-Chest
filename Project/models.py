from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    username = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.LargeBinary, nullable = False)

# Add models for treasure chests (containers) and treasures (items)
# Look into how to make relationships between all tables