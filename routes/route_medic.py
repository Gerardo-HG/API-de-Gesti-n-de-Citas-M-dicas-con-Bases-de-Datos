from fastapi import APIRouter, Path, Body, HTTPException
from schemas.patient import Paciente
import json
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.medic import Medico
from services.medic import MedicSerivce
from services.patient import PatientService
from config.database import Session
from models.medic import Medic as MedicModel

medic_router = APIRouter()

# Medicos

## Motrar Medicos
@medic_router.get(
        path="/medicos",
        tags=["Medico"],
        status_code=200
)
def show_medics():
    try:
        db = Session()
        result = MedicSerivce(db).get_medics()
        return JSONResponse(status_code=200, content=jsonable_encoder(result))

    except Exception as e:
        return {"error" : "{e}"}
    
## Registrar Medico
@medic_router.post(
    path="/medicos",
    tags=['Medico'],
    status_code=201    
)
def create_medic(medic : Medico):

    try:
        with Session() as db:

            pacientes_dnis = PatientService(db).get_dnis()
            medicos_dnis = MedicSerivce(db).get_dnis()

            if medic.dni in pacientes_dnis:
                return JSONResponse(status_code=400,
                                    content={"message": f"DNI {medic.dni} ya está registrado como paciente."})
            
            if medic.dni in medicos_dnis:
                return JSONResponse(status_code=400, 
                                    content={"message": f"DNI {medic.dni} ya está registrado como médico."})

            MedicSerivce(db).create_medic(medic)
            return JSONResponse(status_code=201, 
                                content={"message": "Se ha registrado el medico"})
    
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)},404
    
## Obtener Medico
@medic_router.get(
    path="/medicos/{dni}",
    tags=['Medico'],
    response_model=Medico
)
def get_medic(dni: str =Path(description="DNI of a medic")) -> Medico:
    try:
        with Session() as db:
            result = MedicSerivce(db).get_medic_by_dni(dni)
            if not result:
                raise HTTPException(status_code=404, detail="Medico no encontrado")
            
            return JSONResponse(status_code=200, content=jsonable_encoder(result))
        
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)}
    
    
## Eliminar Medico
@medic_router.delete(
    path="/medicos/{dni}",
    tags=['Medico'],
    status_code=200
)
def delete_medic(dni: str = Path(description="DNI of a medic")):
    try:
        with Session() as db:
            result = MedicSerivce(db).get_medic_by_dni(dni)
            if not result:
                raise HTTPException(status_code=404, detail="Medico no encontrado")
            
            MedicSerivce(db).delete_medic(dni)
            return JSONResponse(status_code=200, content={"message": "Se ha eliminado el medico"})
        
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)}
    
## Actualizar Medico
@medic_router.put(
    path="/medicos/{dni}",
    tags=['Medico'],
    status_code=200
    )
def update_medic(dni: str = Path(description="DNI of a medic"), medic_u: Medico = Body(...)):
    try:
        with Session() as db:
            result = MedicSerivce(db).get_medic_by_dni(dni)
            if not result:
                raise HTTPException(status_code=404, detail="Medico no encontrado")
            
            MedicSerivce(db).update_patient(dni, medic_u)
            return JSONResponse(status_code=200, content={"message": "Se ha modificado el medico"})
        
    except Exception as e:
        return {"error" : " Ha ocurrido un error : "+str(e)}
    