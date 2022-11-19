from app import app
from flask import render_template
from models.models import Plant

@app.route("/")
def main():
    plants = Plant.query.all()
    # plants = Plant.query.filter(Plant.location == "st. Mariupol 1")
    # plants = Plant.query.order_by(Plant.id.desk()).all()
    return render_template("index.html", plants=plants)
