from conexion import Session
from Modelos import Libro

def iliminar_libros(id_libro):
        if type(id_libro) is not int or id_libro <= 0:
              raise ValueError("id no valido")

        with Session.begin() as session:
              libro = session.get(Libro, id_libro)
              if libro is None:
                print("no encontrado")

                session.delete(libro)

        return True