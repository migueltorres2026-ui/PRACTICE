from modelo import Base
from conexion import engine


def crear_tabla():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    crear_tabla()