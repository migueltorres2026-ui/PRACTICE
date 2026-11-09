from sqlalchemy.exc import SQLAlchemyError

from tabla import crear_tabla
from insertar import registrar_libro
from consultar import consultar_libro, buscar_libro
from actualizar import actualizar_libro
from delete import iliminar_libros
from prestamo import prestar_libro


def mostrar_menu():
    print("\n========== SISTEMA DE BIBLIOTECA ==========")
    print("1. Registrar libro")
    print("2. Consultar libros")
    print("3. Buscar libro por ID")
    print("4. Actualizar libro")
    print("5. Eliminar libro")
    print("6. Prestar libro")
    print("0. Salir")


def pedir_entero(mensaje):
    try:
        numero = int(input(mensaje))
    except ValueError:
        raise ValueError("Debes ingresar un número entero.") from None
    return numero


def pedir_id():
    id_libro = pedir_entero("Ingrese el ID del libro: ")
    if id_libro <= 0:
        raise ValueError("El ID debe ser mayor que cero.")
    return id_libro


def pedir_datos_libro():
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = pedir_entero("Año de publicación: ")
    disponible = pedir_entero("Ejemplares disponibles: ")
    return titulo, autor, ano, disponible


def mostrar_libro(libro):
    print("\n----------------------------------------")
    print("ID:", libro.id)
    print("Título:", libro.titulo)
    print("Autor:", libro.autor)
    print("Año:", libro.ano)
    print("Disponibles:", libro.disponible)
    print("----------------------------------------")


def main():
    try:
        crear_tabla()
    except SQLAlchemyError as error:
        print("No se pudo preparar la base de datos:", error)
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                print("\n=== REGISTRAR LIBRO ===")
                titulo, autor, ano, disponibles = pedir_datos_libro()
                libro = registrar_libro(titulo, autor, ano, disponibles)
                print("Libro registrado correctamente.")
                mostrar_libro(libro)

            elif opcion == "2":
                print("\n=== LISTADO DE LIBROS ===")
                libros = consultar_libro()
                if not libros:
                    print("No hay libros registrados.")
                else:
                    for libro in libros:
                        mostrar_libro(libro)

            elif opcion == "3":
                print("\n=== BUSCAR LIBRO ===")
                id_libro = pedir_id()
                libro = buscar_libro(id_libro)
                if libro is None:
                    print("Libro no encontrado.")
                else:
                    mostrar_libro(libro)

            elif opcion == "4":
                print("\n=== ACTUALIZAR LIBRO ===")
                id_libro = pedir_id()
                libro = buscar_libro(id_libro)
                if libro is None:
                    print("Libro no encontrado.")
                else:
                    print("Datos actuales:")
                    mostrar_libro(libro)
                    print("\nIngrese los nuevos datos:")
                    titulo, autor, anio, disponibles = pedir_datos_libro()
                    actualizado = actualizar_libro(
                        id_libro, titulo, autor, anio, disponibles
                    )
                    if actualizado:
                        print("Libro actualizado correctamente.")
                    else:
                        print("Libro no encontrado.")

            elif opcion == "5":
                print("\n=== ELIMINAR LIBRO ===")
                id_libro = pedir_id()
                eliminado = iliminar_libros(id_libro)
                if eliminado:
                    print("Libro eliminado correctamente.")
                else:
                    print("Libro no encontrado.")

            elif opcion == "6":
                print("\n=== PRESTAR LIBRO ===")
                id_libro = pedir_id()
                libro = prestar_libro(id_libro)
                print("Préstamo realizado correctamente.")
                print("Libro:", libro.titulo)
                print("Ejemplares disponibles:", libro.disponible)

            elif opcion == "0":
                print("Hasta luego.")
                break

            else:
                print("Opción inválida. Seleccione una opción del menú.")

        except ValueError as error:
            print("No se pudo completar la operación:", error)
        except SQLAlchemyError as error:
            print("Error de base de datos:", error)


if __name__ == "__main__":
    main()