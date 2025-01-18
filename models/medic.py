from config.database import Base
from sqlalchemy import Column, Integer, String

class Medic(Base):

    __tablename__ = "medics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(String, unique=True)
    especialidad = Column(String)
    anios_experiencia = Column(Integer)
    email = Column(String)