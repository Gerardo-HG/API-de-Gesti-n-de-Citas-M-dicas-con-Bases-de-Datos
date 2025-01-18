from typing import Optional
from datetime import date
from uuid import UUID
from pydantic import BaseModel, Field, validator

class CitaMedica(BaseModel):
    id: int = Field(..., description="ID único de la cita médica")
    paciente_dni: str = Field(..., description="DNI del paciente")
    medico_dni: str = Field(..., description="DNI del médico")
    fecha: date = Field(default_factory=date.today, description="Fecha de la cita médica")
    motivo: str = Field(..., min_length=5, max_length=20, description="Motivo de la cita médica")
    estado: Optional[str] = Field(default="pendiente", description="Estado de la cita médica")

    @validator('estado')
    def validar_estado(cls, v):
        estados_validos = ['pendiente', 'confirmada', 'cancelada', 'realizada']
        if v not in estados_validos:
            raise ValueError(f"Estado no válido. Debe ser uno de: {', '.join(estados_validos)}")
        return v
