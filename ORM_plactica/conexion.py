from sqlalchemy import create_engine #acceso a la base de datos
from sqlalchemy.orm import sessionmaker # generar sessiones para nuestra base de datos

engine = create_engine("sqlite:///biblioteca.db", echo=False)
Session = sessionmaker(bind=engine, expire_on_commit=False)



