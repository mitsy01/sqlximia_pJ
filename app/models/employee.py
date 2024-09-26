from typing import List

from sqlalchemy import String, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.models.base import Base
from app.models.position import Position
from app.models.associates import position_employee_assoc_table


class Employee(Base):
    __tablename__ = "employees"
    
    id: Mapped[int] = mapped_column("id", primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    salary: Mapped[float] = mapped_column(Float())
    age: Mapped[int] = mapped_column()
    positions: Mapped[List[Position]] = relationship(secondary=position_employee_assoc_table)
