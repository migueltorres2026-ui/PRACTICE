from conexion import engine
from Model import Base

def crear_tabla():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    crear_tabla()