from flask import render_template, Blueprint, request

from app.models.base import Session
from app.models.position import Position


position_blueprint = Blueprint("positions", __name__, url_prefix="/positions/")


@position_blueprint.get("/")
@position_blueprint.post("/")
def add_position():
    with Session() as session:
        if request.method == "POST":
            name = request,form,get("name")
            position = Position(name=name)
            session.add(position)
            session.commit()
            
        positions = session.query(Position).all()
        return render_template("position.management.html", positions=positions, title="Управління списком посад")


@position_blueprint.get("/<int:id>/")
def get_position(id):
    with Session() as session:
        position = session.query(Position).where(Position.id == id).first()
        return render_template("position/info.html", position=position)