from app import app, db
from flask import render_template, request, redirect
from models.models import Plant, Employee


@app.route("/add-employee")
def add_employee():
    return render_template("add_employee.html")


@app.route("/save-employee", methods=["POST"])
def save_employee():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    employee = Employee(first_name=first_name, last_name=last_name, email=email)
    db.session.add(employee)
    db.session.commit()
    return redirect("/")


@app.route("/delete-employee/<int:id>")
def delete_employee(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect("/")
