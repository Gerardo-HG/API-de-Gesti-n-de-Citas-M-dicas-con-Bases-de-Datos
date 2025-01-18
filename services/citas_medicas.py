from models.citas_medicas import CitaMedica as CitaMedicaModel
from schemas.citas_medicas import CitaMedica
from fastapi import HTTPException

class CitaMedicaService:

    def __init__(self, db) -> None:
        self.db = db

    def get_appointments(self):
        result = self.db.query(CitaMedicaModel).all()
        return result
    
    def get_appointment_by_id(self,id: int):
        result = self.db.query(CitaMedicaModel).filter(CitaMedicaModel.id == id).first()
        if not result:
            raise HTTPException(status_code=404, detail="La cita médica no existe.")

        return result
    
    def create_appointment(self, appointment: CitaMedica):
        existing_appointment = self.db.query(CitaMedicaModel).filter(CitaMedicaModel.id == appointment.id).first()
        if existing_appointment:
            raise ValueError("La cita médica ya existe.")
        
        new_appointment = CitaMedicaModel(**appointment.dict())
        self.db.add(new_appointment)
        self.db.commit()
        return
    
    def update_appointment(self, id : int, data : CitaMedica):
        appointment = self.db.query(CitaMedicaModel).filter(CitaMedicaModel.id == id).first()
        if not appointment:
            raise HTTPException(status_code=404, detail="La cita médica no existe.")

        appointment.estado = data.estado        
        appointment.fecha = data.fecha
        appointment.motivo = data.motivo

        self.db.commit()
        return appointment
    
    def delete_appointment(self, id : int):
        appointmet = self.db.query(CitaMedicaModel).filter(CitaMedicaModel.id == id).first()
        if not appointmet:
            raise HTTPException(status_code=404, detail="La cita médica no existe.")
        
        self.db.delete(appointmet)
        self.db.commit()
        return
    