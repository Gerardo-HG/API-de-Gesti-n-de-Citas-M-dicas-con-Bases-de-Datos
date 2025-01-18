from fastapi import APIRouter, Path, Body, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.citas_medicas import CitaMedica
from middlewares.jwt_bearer import JWTBearer
from services.citas_medicas import CitaMedicaService
from config.database import Session
from services.medic import MedicSerivce
from services.patient import PatientService

cita_router = APIRouter()

## Mostrar todas las citas
@cita_router.get(
    path="/citas",
    tags=["Cita Medica"],
    status_code=200,
    dependencies=[Depends(JWTBearer())]
)
def show_appointments():
    try:
        db = Session()
        cita_service = CitaMedicaService(db)
        appointments = cita_service.get_appointments()
        return JSONResponse(status_code=200, content=jsonable_encoder(appointments))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener las citas: {str(e)}")

## Registrar una nueva cita
@cita_router.post(
    path="/citas",
    tags=['Cita Medica'],
    status_code=201,
    dependencies=[Depends(JWTBearer())]
)
def create_appointment(appointment: CitaMedica = Body(...)):
    try:
        with Session() as db:
            cita_service = CitaMedicaService(db)

            # Validación de DNI de paciente y médico
            pacientes_dnis = PatientService(db).get_dnis()
            medicos_dnis = MedicSerivce(db).get_dnis()

            if appointment.paciente_dni not in pacientes_dnis or not appointment.paciente_dni.isnumeric():
                raise HTTPException(status_code=400, detail="DNI del paciente no válido.")
            
            if appointment.medico_dni not in medicos_dnis or not appointment.medico_dni.isnumeric():
                raise HTTPException(status_code=400, detail="DNI del médico no válido.")
            
            # Crear la cita médica
            cita_service.create_appointment(appointment)
            return JSONResponse(status_code=201, content={"message": "Cita médica registrada con éxito"})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al registrar la cita: {str(e)}")

## Obtener una cita por ID
@cita_router.get(
    path="/citas/{id}",
    tags=['Cita Medica'],
    response_model=CitaMedica,
    status_code=200
)
def get_appointment(id: int = Path(..., description="ID único de la cita médica")):
    try:
        db = Session()
        cita_service = CitaMedicaService(db)
        appointment = cita_service.get_appointment_by_id(id)
        if not appointment:
            raise HTTPException(status_code=404, detail="Cita médica no encontrada")
        return JSONResponse(status_code=200, content=jsonable_encoder(appointment))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener la cita: {str(e)}")

## Actualizar una cita
@cita_router.put(
    path="/citas/{id}",
    tags=['Cita Medica'],
    status_code=200
)
def update_appointment(
    id: int = Path(..., description="ID único de la cita médica a actualizar"),
    appointment_u: CitaMedica = Body(...)
):
    try:
        db = Session()
        cita_service = CitaMedicaService(db)
        cita_service.update_appointment(id, appointment_u)
        return JSONResponse(status_code=200, content={"message": "Cita médica actualizada con éxito"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la cita: {str(e)}")

## Eliminar una cita
@cita_router.delete(
    path="/citas/{id}",
    tags=['Cita Medica'],
    status_code=200
)
def delete_appointment(
    id: int = Path(..., description="ID único de la cita médica a eliminar")
):
    try:
        db = Session()
        cita_service = CitaMedicaService(db)
        cita_service.delete_appointment(id)
        return JSONResponse(status_code=200, content={"message": "Cita médica eliminada con éxito"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la cita: {str(e)}")
