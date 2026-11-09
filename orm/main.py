from datetime import date
from sqlalchemy.exc import SQLAlchemyError

from tabla import crear_tabla
from registrar_sala import insertar_salas
from consultar_sala import consultar_sala
from registrar_reservas import registrar_reserva
from consulta_reservas import consultar_reservas
from cancelar_reserva import cancelar_reserva


def mostrar_menu():
    print("\n===== MENU Y PRUEBAS =====")
    print("1. Registrar sala")
    print("2. Consultar salas")
    print("3. Registrar reserva")
    print("4. Consultar reservas")
    print("5. Cancelar reserva")
    print("0. Salir")


def pedir_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError("Debes ingresar un número entero") from None


def pedir_id(mensaje):
    numero = pedir_entero(mensaje)

    if numero <= 0:
        raise ValueError("El ID debe ser mayor que cero")

    return numero


def pedir_fecha():
    texto = input("Fecha (AAAA-MM-DD): ").strip()

    try:
        return date.fromisoformat(texto)
    except ValueError:
        raise ValueError(
            "Fecha inválida. Usa AAAA-MM-DD, por ejemplo 2026-11-10"
        ) from None


def mostrar_sala(sala):
    print("\n-------------------------")
    print("ID:", sala.id)
    print("Nombre:", sala.nombre)
    print("Disponible:", "Sí" if sala.disponible else "No")
    print("-------------------------")


def mostrar_reserva(reserva):
    print("\n-------------------------")
    print("ID:", reserva.id)
    print("Estudiante:", reserva.estudiante)
    print("Sala:", reserva.sala.nombre)
    print("Fecha:", reserva.fecha)
    print("-------------------------")


def main():
    try:
        crear_tabla()
    except SQLAlchemyError as error:
        print("No se pudo preparar la base de datos:", error)
        return

    while True:
        mostrar_menu()

        try:
            opcion = pedir_entero("Seleccione una opción: ")

            if opcion == 1:
                print("\n=== REGISTRAR SALA ===")

                nombre = input("Nombre de la sala: ").strip()
                sala = insertar_salas(nombre)

                print("Sala registrada correctamente")
                mostrar_sala(sala)

            elif opcion == 2:
                print("\n=== CONSULTAR SALAS ===")

                salas = consultar_sala()

                if not salas:
                    print("No hay salas registradas")
                else:
                    for sala in salas:
                        mostrar_sala(sala)

            elif opcion == 3:
                print("\n=== REGISTRAR RESERVA ===")

                estudiante = input("Estudiante: ").strip()
                sala_id = pedir_id("ID de la sala: ")
                fecha = pedir_fecha()

                reserva = registrar_reserva(
                    estudiante, sala_id, fecha
                )

                print("Reserva registrada correctamente")
                print("ID de la reserva:", reserva.id)

            elif opcion == 4:
                print("\n=== CONSULTAR RESERVAS ===")

                reservas = consultar_reservas()

                if not reservas:
                    print("No hay reservas registradas")
                else:
                    for reserva in reservas:
                        mostrar_reserva(reserva)

            elif opcion == 5:
                print("\n=== CANCELAR RESERVA ===")

                id_reserva = pedir_id("ID de la reserva: ")
                cancelada = cancelar_reserva(id_reserva)

                if cancelada:
                    print("Reserva cancelada")
                    print("La sala quedó disponible")
                else:
                    print("La reserva no existe")

            elif opcion == 0:
                print("Hasta luego")
                break

            else:
                print("Opción inválida")

        except ValueError as error:
            print("No se pudo completar la operación:", error)

        except SQLAlchemyError as error:
            print("Error de base de datos:", error)


if __name__ == "__main__":
    main()