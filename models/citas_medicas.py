from datetime import date
from sqlalchemy import Column, String, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from config.database import Base

class CitaMedica(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    paciente_dni = Column(String)
    medico_dni = Column(String)
    fecha = Column(Date, default=date.today)
    motivo = Column(String(20), nullable=False)
    estado = Column(String, default="pendiente", nullable=False)

