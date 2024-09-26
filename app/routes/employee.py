from flask import render_template, Blueprint, request

from app.models.base import Session
from app.models.position import Position
from app.models.employee import Employee


employee_blueprint = Blueprint("employees", __name__, url_prefix="/employees/")


@employee_blueprint.get("/")
@employee_blueprint.post("/")
def add_employee():
    with Session() as session:
        if request.method == "POST":
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            salary = request.form.get("salary")
            age = request.form.get("age")

            positions = request.form.getlist("positions")
            positions = session.query(Position).where(Position.id.in_(positions)).all()

            employee = Employee(first_name=first_name, last_name=last_name, age=age, salary=salary, positions=positions)
            session.add(employee)
            session.commit()

        employees = session.query(Employee).all()
        positions = session.query(Position).all()
        return render_template("employee/management.html", employees=employees, positions=positions, title="Управління працівниками")


@employee_blueprint.get("/<int:id>/")
def get_employee(id):
    with Session() as session:
        employee = session.query(Employee).where(Employee.id == id).first()
        return render_template("employee/info.html", employee=employee, title="Інформація про працівника")