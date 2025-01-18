from models.patient import Patient as PatientModel
from schemas.patient import Paciente

class PatientService():

    def __init__(self, db) -> None:
        self.db = db

    def get_patients(self):
        result = self.db.query(PatientModel).all()
        return result

    def get_patient_by_dni(self, dni : str):
        resutl = self.db.query(PatientModel).filter(PatientModel.dni == dni).first()
        return resutl
    
    def create_patient(self, patient:Paciente):
        new_patient = PatientModel(**patient.dict())
        self.db.add(new_patient)
        self.db.commit()
        return
    
    def update_patient(self, dni: str, data: Paciente):
        patient = self.db.query(PatientModel).filter(PatientModel.dni == dni).first()
        if patient: 
            patient.nombre = data.nombre
            patient.apellido = data.apellido
            patient.email = data.email
            patient.fecha_nacimiento = data.fecha_nacimiento
            self.db.commit()
        return None

    def delete_patient(self, dni:str):
        patient = self.db.query(PatientModel).filter(PatientModel.dni == dni).first()
        if patient:
            self.db.delete(patient)
            self.db.commit()
        return None
    

    def get_dnis(self):
        patients_dnis = self.db.query(PatientModel.dni).all()
        return [dni[0] for dni in patients_dnis]  
