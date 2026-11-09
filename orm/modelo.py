from __future__ import annotations
from sqlalchemy import Integer, String, Boolean,ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Sala(Base):
    __tablename__ = "sala"
    __table_args__ = (
    CheckConstraint("capacidad > 0", name="ck_sala_capacidad"),
)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return (
            f"Sala(id={self.id}, "
            f"nombre={self.nombre!r}, "
            f"capacidad={self.capacidad}, "
            f"disponible={self.disponible})"
        )
class Reserva(Base):
    __tablename__ = "reserva"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    estudiante: Mapped[str] = mapped_column(String, nullable=False)
    sala_id: Mapped[int] = mapped_column(Integer, ForeignKey("sala.id"))
    fecha: Mapped[str] = mapped_column(String(10), nullable=False, format="AAAA-MM-DD")

    def __repr__(self):
        return (
            f"Reserva (id={self.id}), "
            f"estudiante={self.estudiante}, "
            f"sala_id={self.sala_id}, "
            f"fecha={self.fecha}"
        )

