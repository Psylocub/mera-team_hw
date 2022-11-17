from app import app
from flask import render_template
from models.models import Plant, Employee

@app.route("/")
def main():
    plants = Plant.get_data()
    return render_template("index.html", plants=plants)

@app.route("/plants-employees")
def plant_employees():
    plants = Plant.get_data()
    employees = Employee.get_data()
    return render_template("plants_employees.html", plants=plants, employees=employees)
