import pandas
import json

"""" Model classes """
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class subbox(db.Model):
    __tablename__ = 'subboxes'

    tag = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String)

    def __repr__(self):
        return f"<subbox title={self.title}"


# unsure how model.py operates at this time
def connect_to_db(app, db_name="lunchdb"):
    """Connect database to Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Connecting instance of SQLAlchemy to database & Flask
    db.app = app
    db.init_app(app)

    print("Connected to database!")

if __name__ == "__main__":
    # from flask import Flask
    from server import app 

    # app = Flask(__name__)
    connect_to_db(app) 


""" Seed database """
def load_data():
    # Load subbox data from JSON file
    with open("subbox_data.json") as f:
        subbox_data = json.loads(f.read())

    # Create items, store them in list so we can use them to create a bento
    subboxes_in_db = []
    for subbox in subbox_data:
        tag, title, ingredients = (
            subbox["tag"],
            subbox["title"],
            subbox["ingredients"],
        )

        db_subbox = subbox.create_subbox(tag, title, ingredients)
        subboxes_in_db.append(db_lunch)

    db.session.add_all(subboxes_in_db)
    db.session.commit()

def create_subbox(tag, title, ingredients):
    """ Create and return a new container filling. """
    subbox = subbox(tag=tag, 
                    title=title, 
                    ingredients=ingredients) 
    return subbox

def get_subboxes():
    """ Return all filling options. """
    return subbox.query.all()

def get_subbox_by_tag(tag):
    """ Return container filling by tag. """
    return subbox.query.get(tag)
