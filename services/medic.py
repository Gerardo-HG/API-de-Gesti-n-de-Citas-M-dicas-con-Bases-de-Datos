from models.medic import Medic as MedicModel
from schemas.medic import Medico

class MedicSerivce():

    def __init__(self, db) -> None:
        self.db = db

    def get_medics(self):
        result = self.db.query(MedicModel).all()
        return result

    def get_medic_by_dni(self, dni):
        resutl = self.db.query(MedicModel).filter(MedicModel.dni == dni).first()
        return resutl
    
    def create_medic(self, medic:Medico):
        new_medic = MedicModel(**medic.dict())
        self.db.add(new_medic)
        self.db.commit()
        return
    
    def update_medic(self, dni: str, data: Medico):
        medic = self.db.query(MedicModel).filter(MedicModel.dni == dni).first()
        medic.nombre = data.nombre
        medic.apellido = data.apellido
        medic.email = data.email
        medic.especialidad = data.especialidad
        medic.anios_experiencia = data.anios_experiencia
        self.db.commit()
        return

    def delete_medic(self, dni:str):
        medic = self.db.query(MedicModel).filter(MedicModel.dni == dni).first()
        self.db.delete(medic)
        self.db.commit()
        return

    def get_dnis(self):
        medics_dnis = self.db.query(MedicModel.dni).all()
        return [dni[0] for dni in medics_dnis]  
