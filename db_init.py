from datetime import datetime
from flask_script import Command
from flask import json
from app import db, create_app
from app.color import Color

COLORS_JSON = json.load(open("colors.json"))

app = create_app()
app.app_context().push()

def seed_things():

    db.session.bulk_insert_mappings(Color, COLORS_JSON)


class DataSeed():
    """ Seed the DB."""

    def run(self):
        print("Dropping tables...")
        db.drop_all()
        db.create_all()
        seed_things()
        db.session.commit()
        print("DB successfully seeded.")

kickoff = DataSeed().run()