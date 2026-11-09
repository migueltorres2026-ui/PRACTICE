from sqlalchemy import Integer, String, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Hotel(Base):
    __name__ = "hotel"
    __table_args__ = (
        CheckConstraint("llave > 0", name="CK_Hotel_llave"),
        CheckConstraint("habitacion > 0", name="CK_Hotel_habitacion")
    )

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    llave : Mapped[int] = mapped_column(Integer, nullable=False)
    dueno : Mapped[str] = mapped_column(String(100), nullable=False, default=1)
    habitacion : Mapped[str] = mapped_column(Integer, nullable=False)


    def __repr__(self):
        (
        f"hotel(id={self.id})",
        f"llave={self.llave}",
        f"dueno={self.dueno!r}",
        f"habitacion={self.habitacion}"
        )

