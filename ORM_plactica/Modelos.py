from sqlalchemy import Integer, String, CheckConstraint #variables para la cracion clase
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column #definir lo que estara en la adentro la columna y donde se guia

class Base(DeclarativeBase): # clase madre, este nos genera no que estara endentro de la tabla suele estar vacia
    pass

class Libro(Base):
    __tablename__ = "libro" # el nombre de la tabla
    __table_args__ = ( # esto genera variables o reglas de complir con check
        CheckConstraint("ano > 0", name="ck_libro_ano"), #name= es lo que se vera representado
        CheckConstraint("disponible >= 0", name="ck_libro_disponibles")
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    autor: Mapped[str] = mapped_column( String(100), nullable=False)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[str] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self):
        return (
        f"libro(id={self.id})",
        f"titulo ={self.titulo!r}",
        f"autor ={self.autor!r}",
        f"ano ={self.ano}",
        f"disponible= {self.disponible}"
        )
        