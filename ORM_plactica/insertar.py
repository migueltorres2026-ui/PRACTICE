from conexion import Session
from Modelos import Libro

def registrar_libro(titulo, autor, ano, disponible):
    titulo = titulo.strip()
    autor = autor.strip()

    if not titulo or len(titulo) > 150:
        raise ValueError("error: titulo a 1 a 150")
    
    if not autor or len(autor) > 100:
        raise ValueError("error: autor a 1 a 100")
    
    if type(ano) is not int or ano <= 0:
        raise ValueError("error: mayor a cero")

    if type(disponible) is not int or disponible < 0:
        raise ValueError("error: no deve ser numeros negativos")

    with Session.begin() as session:
        libro = Libro(
            titulo= titulo,
            autor= autor,
            ano= ano,
            disponible= disponible,
        )

        session.add(libro)
    print("libro registrado")

    return libro