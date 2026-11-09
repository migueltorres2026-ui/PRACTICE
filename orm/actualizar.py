from conexion import Session
from modelo import Hotel


def actualizar_hotel(id_hotel, llave, dueno, habitacion):
    if type(id_hotel) is not int or id_hotel <= 0:
        raise ValueError("mayor a cero")

    dueno = dueno.sprip()

    if not dueno or len(dueno) <= 0:
        raise ValueError("debe haber un dueño")
    if type(llave) is not int or llave < 0:
        raise ValueError("debe ser mayor a cero")
    if type(habitacion) is not int or habitacion < 0:
        raise ValueError("debe ser mayor a cero")


    with Session.begin() as session:
        hotel = session.get(Hotel, id_hotel)
        if hotel is None:
            return False

        hotel.llave = llave
        hotel.dueno =  dueno
        hotel.habitacion = habitacion

    return True
