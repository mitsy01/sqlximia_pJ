from flask import Flask

from app.models.base import create_db
from app.models.employee import Employee
from app.models.position import Position
from app.routes.employee import employee_blueprint
from app.routes.position import position_blueprint


app = Flask(__name__)
app.register_blueprint(employee_blueprint)
app.register_blueprint(position_blueprint)

create_db()