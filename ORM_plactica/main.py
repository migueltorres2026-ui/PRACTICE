from sqlalchemy.exc import SQLAlchemyError

from tabla import crear_tabla
from insertar import registrar_libro
from consultar import consultar_libro, buscar_libro
from actualizar import actualizar_libro
from delete import iliminar_libros
from prestamo import prestar_libro

def mostrar_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. registrar libro")
    print("2. consultar libro")
    print("3. buscar libro por ID")
    print("4. Actualizar")
    print("5 eliminar libro")
    print("6. prestar libro")
    print("0. salir")

def pedir_entero(mensaje):
    try:
        numero = int(input(mensaje))
    except ValueError:
        raise ValueError("el ID debe ser mayor a cero") from None
    return numero

def pedir_id():
    id_libro = pedir_entero("Ingrese ID del Libro: ")
    if id_libro <= 0:
        raise ValueError("el id es invalido")
    return id_libro

def pedir_datos_libro():
    titulo = input("Titulo: ").strip()
    autor = input("Autor").strip()
    ano = input("Año de publicacion: ").strip()
    disponible = input("Ejemplares disponibles: ").strip()
    return titulo, autor, ano, disponible


def mostrar_libro(libro):
    print("\n-----------------------------------------")
    print("ID:", libro.id)
    print("Titulo:", libro.titulo)
    print("autor:", libro.autor)
    print("ano:", libro.ano)
    print("disponible:", libro.disponible)
    print("-------------------------------------------")

def main():
    try:
        crear_tabla()
    except SQLAlchemyError as error:
        print("no se pudo la base de datos", error)
        return

    while True:
        mostrar_menu()
        opcion = input("seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                print("=== REGISTRO LIBRO ===")
                titulo, autor, ano, disponible = pedir_datos_libro()
                libro = registrar_libro(titulo, autor, ano, disponible)
                print("libros registrados")
                mostrar_libro(libro)
            
            elif opcion == "2":
                print("=== LISTADO LIBRO ===")
                libros = consultar_libro()
                if not libros:
                    print("no hay registro")
                else:
                    for libro in libros:
                        mostrar_libro(libro)

            elif opcion == "3":
                print("=== LIBROS ID ===")
                id_libro = pedir_id()
                libro = buscar_libro(id_libro)
                if libro is None:
                    print("no hay registro")
                else:
                    buscar_libro(libro)

            elif opcion == "4":
                print("=== ACTUALIZAR ==")
                id_libro = pedir_id()
                libro = buscar_libro(id_libro)
                if libro in None:
                    print("libro no encontrado")
                else:
                    print("Datos Actuales:")
                    mostrar_libro(libro)
                    print("\nIngrese los nuevos datos:")
                    titulo, autor, ano, disponible = pedir_datos_libro()
                    actualizado = actualizar_libro(
                        id_libro, titulo, autor, ano, disponible
                    )
                    if actualizado:
                        print("libro actualizado")
                    else:
                        print("libro no encontrado")

            elif opcion == "5":
                print("\n=== ELIMINAR LIBRO ===")
                id_libro = pedir_id()
                eliminado = iliminar_libros(id_libro)
                if eliminado:
                    print("eliminado")
                else:
                    print("libro no encontrado")

            elif opcion == "6":
                print("=== prestar libro ===")
                id_libro = pedir_id()
                libro = prestar_libro(id_libro)
                print("prestamo realizado")
                print("libro:", libro.titulo)
                print("Ejemplares", libro.disponible)

            elif opcion == "0":
                print("chao")
                break

            else:
                print("opcion invalida")
        except ValueError as error:
            print("no se pudo completar operacion:", error)
        except SQLAlchemyError as error:
            print("error de base de datos.", error)

if __name__ == '__main__':
    main()