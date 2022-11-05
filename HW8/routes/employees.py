from app import app
from models.models import Employee
from flask import render_template, request, redirect

@app.route("/add-employee")
def add_employee():
    return render_template("add_employee.html")

@app.route("/save-employee", methods=["POST"])
def save_employee():
    print(request.form)
    name = request.form.get("name")
    object_id = request.form.get("object_id")
    type_of_work = request.form.get("type_of_work")
    employee = Employee(name, object_id, type_of_work)
    employee.save()
    return redirect("/plants-employees")

@app.route("/delete-employee/<int:id>")
def delete_employee(id):
    Employee.delete(id)
    return redirect("/plants-employees")
