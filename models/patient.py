from config.database import Base
from sqlalchemy import Column, Integer, String, DATE

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(String, unique=True)
    fecha_nacimiento = Column(DATE)
    email = Column(String)