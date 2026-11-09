from conexion import Session
from Modelos import Libro

def prestar_libro(id_libro):
    if type(id_libro) is not int or id_libro <= 0:
        raise ValueError("id no valido")

    with Session.begin() as session:
        libro = session.get(Libro, id_libro)

        if libro is None:
            raise ValueError("no encontrado")

        if libro.disponible <= 0:
            raise ValueError("no hay ejemplares")

        libro.disponible -= 1

    return libro