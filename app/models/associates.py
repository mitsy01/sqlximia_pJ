from sqlalchemy import Table, Column, ForeignKey

from app.models.base import Base

position_employee_assoc_table = Table(
    "position_employee_assoc)table",
    Base.metadata,

    Column(
        "position_id",
        ForeignKey("positions.id"),
        primary_key=True,
    ),
    Column(
        "employee_id",
        ForeignKey("employees.id"),
        primary_key=True,
    ),
)