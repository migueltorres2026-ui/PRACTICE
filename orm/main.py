from sqlalchemy.exc import SQLAlchemyError
from tabla import crear_tabla
from insertar import registro_llave
from consultar import consultar_hotel, buscar_hotel
from actualizar import actualizar_hotel
from eliminar import delete




def mostrar_menu():
    print("\n==== SISTEMA DE HOTELES ====")
    print("1. Resgistro hotel")
    print("2. Consultar hotel")
    print("3. buscar hotel")
    print("4. actualizar hotel")
    print("5. iliminar hotel")
    print("0. salir")


def pedir_entero(mensaje):
    try:
        numero = int(input(mensaje))
    except ValueError:
        raise ValueError("numero entero")
    return numero

def pedir_id():
    id_hotel = pedir_entero("ingrese ID del hotel: ")
    if id_hotel <= 0:
        raise ValueError("valor invalido")
    return id_hotel

def pedir_datos_hotel():
    llave = input("llave: ").strip()
    dueno = input("dueno: ").strip()
    habitacion = input("habitacion: ").strip()
    return llave, dueno, habitacion

def mostrar_hotel(hotel):
    print("\n------------------------")
    print("ID: ", hotel.id)
    print("llave: ", hotel.llave)
    print("dueno: ", hotel.dueno)
    print("habitacion: ", hotel.habitacion)
    print("------------------------")

def main():
    try:
        crear_tabla()
    except SQLAlchemyError as error:
        print("no se pudo, base de datos", error)
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                print("=== REGISTRO ===")
                llave, dueno, habitacion = pedir_datos_hotel()
                hotel = registro_llave(llave, dueno, habitacion)
                print("nuevo hotel")
                return hotel

            if opcion == "2":
                print("=== CONSULTA ===")
                hoteles = consultar_hotel()
                if not hotel:
                    print("no hay consulta")
                else:
                    for hotel in hoteles:
                        mostrar_hotel(hotel)

            if opcion == "3":
                print("=== buscar ===")
                id_hotel = pedir_id()
                hotel = buscar_hotel(id_hotel)
                if hotel is None:
                    ("no se encontro")
                else:
                    mostrar_hotel(hotel)

            if opcion == "4":
                print("=== actualizar ===")
                mostrar_hotel(hotel)
                print("\nIngrese nuevos valores: ")
                llave, dueno, habitacion = pedir_datos_hotel()
                actualizado = actualizar_hotel(
                    id_hotel, llave, dueno, habitacion
                )
                if actualizado:
                    print("hotel actualizado")
                else:
                    print("no encontrado")

            if opcion == "5":
                print("=== DELETE ===")
                id_hotel = pedir_id()
                eliminado = delete(id_hotel)
                if eliminado:
                    print("eliminado hotel")
                else:
                    print("no encontrado")

            if opcion == "0":
                print("chao")
                break
            else:
                ("opcion invalida")
        except ValueError as error:
            print("no se pudo: ", error)

        except SQLAlchemyError as error:
            print("no encontrado: ", error)

if __name__ == "__main__":
    main()