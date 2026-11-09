from conexion import engine
from Modelos import Base

def crear_tabla():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    crear_tabla()
    print("tabla creadas correctamente")