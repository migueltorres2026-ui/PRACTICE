from conexion import Session
from modelo import Hotel


def delete(id_hotel):

    if type(id_hotel) is not int or id_hotel <=0:
        raise ValueError("mayot que cero")

    with Session.begin() as session:
        hotel = session.get(Hotel, id_hotel)
        if hotel is None:
            return False

        session.delete(hotel)

        return True