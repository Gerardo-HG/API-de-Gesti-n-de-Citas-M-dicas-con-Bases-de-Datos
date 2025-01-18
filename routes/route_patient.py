from fastapi import APIRouter, Path, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.patient import Paciente
import json
from fastapi.responses import JSONResponse
from typing import Optional, List
from services.patient import PatientService
from services.medic import MedicSerivce
from models.patient import Patient as PatientModel
from config.database import Session



patient_router = APIRouter()

# Path Operations

## Pacientes

## Mostrar Pacientes
@patient_router.get(
    path="/pacientes",
    tags=['Paciente'],
    response_model=List[Paciente],
    status_code=200
)
def show_patients() -> List[Paciente]:
    try:
        db = Session()
        result = PatientService(db).get_patients()
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

    except Exception as e:
        return {"error" : "{e}"}

## Registrar Paciente
@patient_router.post(
    path="/pacientes",
    tags=['Paciente'],
    status_code=201    
)
def create_patient(patient : Paciente):

    try:
        with Session() as db:

            pacientes_dnis = PatientService(db).get_dnis()
            medicos_dnis = MedicSerivce(db).get_dnis()

            if patient.dni in pacientes_dnis:
                return JSONResponse(status_code=400,
                                    content={"message": f"DNI {patient.dni} ya está registrado como paciente."})
            
            if patient.dni in medicos_dnis:
                return JSONResponse(status_code=400, 
                                    content={"message": f"DNI {patient.dni} ya está registrado como médico."})

            PatientService(db).create_patient(patient)
            return JSONResponse(status_code=201, 
                                content={"message": "Se ha registrado el paciente"})
    
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)},404
    
## Obtener Paciente
@patient_router.get(
    path="/pacientes/{dni}",
    tags=['Paciente'],
    response_model=Paciente
)
def get_patient(dni: str =Path(description="DNI of a patient")) -> Paciente:
    try:
        with Session() as db:
            result = PatientService(db).get_patient_by_dni(dni)
            if not result:
                raise HTTPException(status_code=404, detail="Paciente no encontrado")
            
            return JSONResponse(status_code=200, content=jsonable_encoder(result))
        
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)}
    
## Eliminar Paciente
@patient_router.delete(
    path="/pacientes/{dni}",
    tags=['Paciente'],
    status_code=200
)
def delete_patient(dni: str = Path(description="DNI of a patient")):
    try:
        with Session() as db:
            result = PatientService(db).get_patient_by_dni(dni)
            if not result:
                raise HTTPException(status_code=404, detail="Paciente no encontrado")
            
            PatientService(db).delete_patient(dni)
            return JSONResponse(status_code=200, content={"message": "Se ha eliminado el paciente"})
        
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)}
    
## Actualizar Paciente
@patient_router.put(
    path="/pacientes/{dni}",
    tags=['Paciente'],
    status_code=200
    )
def update_patient(dni: str = Path(description="DNI of a patient"), patient_u: Paciente = Body(...)):
    try:
        with Session() as db:
            result = PatientService(db).get_patient_by_dni(dni)
            if not result:
                raise HTTPException(status_code=404, detail="Paciente no encontrado")
            
            PatientService(db).update_patient(dni, patient_u)
            return JSONResponse(status_code=200, content={"message": "Se ha modificado el paciente"})
        
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)}