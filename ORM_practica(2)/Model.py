from sqlalchemy import Integer, String, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class llavero(Base):
    __tablename__ = "llave"
    __table_args__ = (
        CheckConstraint("llave > 0", name="ck_llavero_llave")
    )

    id: Mapped[int] = mapped_column( Integer, primary_key=True)
    llave: Mapped[int] = mapped_column( Integer, nullable=False)
    dueño: Mapped[str] = mapped_column(String(100),nullable=False)
    Nhabitacion: Mapped[int] = mapped_column(Integer, nullable=False)


    def __repr__(self):
        return (
        f"llavero(id={self.id})",
        f"llave={self.llave}",
        f"dueño={self.dueño!r}",
        f"Nhabitacion={self.Nhabitacion}"
        )
