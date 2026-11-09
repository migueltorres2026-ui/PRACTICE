from conexion import Session
from Modelos import Libro

def actualizar_libro(id_libro, titulo, autor, ano, disponibles):

    if type(id_libro) is not int or id_libro <= 0:
        raise ValueError("id no valido")

    titulo = titulo.strip()
    autor = autor.strip()

    if not titulo or len(titulo) > 150:
        raise ValueError("solo 150 carecteres")

    if not autor or len(autor) > 100:
        raise ValueError("solo 100 caracteres")
    
    if type(ano) is not int or ano <= 0:
        raise ValueError("mayor a cero")

    if type(disponibles) is not int or disponibles < 0:
        raise ValueError("no puede ser negativo")

    with Session.begin() as session:
        libro = session.get(Libro, id_libro)

        if libro is None:
            print("nada")
            return

        libro.titulo = titulo
        libro.autor = autor
        libro.ano =  ano
        libro.disponible = disponibles

    print("libros actualizado")