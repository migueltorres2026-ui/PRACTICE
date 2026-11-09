from sqlalchemy import select
from conexion import Session
from Modelos import Libro

def consultar_libro():
    with Session() as session:
        consulta = select(Libro).order_by(Libro.id)
        libros = session.scalars(consulta).all()

        if not libros:
            print("No hay registro")
            return
        if libros in libros:
            print(libros)


def buscar_libro(id_libro):
    if type(id_libro) is not int or id_libro <= 0:
        raise ValueError("mayor a cero") 

    with Session() as session:
        libro = session.get(Libro, id_libro)

    return libro