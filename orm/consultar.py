from sqlalchemy import select
from conexion import Session
from modelo import Hotel


def consultar_hotel():
    with Session() as session:
        consulta = select(Hotel).order_by(Hotel.id)
        hotel = session.scalars(consulta).all()

    return hotel


def buscar_hotel(id_hotel):
    if type(id_hotel) is not int or id_hotel <= 0:
        raise ValueError("debe ser mayor a cero")

    with Session() as session:
        hotel = session.get(Hotel, id_hotel)

    return hotel