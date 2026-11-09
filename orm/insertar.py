from conexion import Session
from modelo import Hotel

def registro_llave(llave, dueno, habitacion):
    dueno = dueno.strip()


    if not dueno or len(dueno) <= 0:
        raise ValueError("debe haber un dueño")
    if type(llave) is not int or llave <= 0:
        raise ValueError("debe ser mayor a cero")
    if type(habitacion) is not int or habitacion > 100:
        raise ValueError("debe ser mayor a cero")

    with Session.begin() as session:
        hotel = Hotel(
            dueno=dueno,
            llave=llave,
            habitacion=habitacion,
        )
        session.add(hotel)

    return hotel