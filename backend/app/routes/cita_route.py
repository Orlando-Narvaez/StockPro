from fastapi import APIRouter, HTTPException
from app.models.cita_model import Cita
from app.database import base_de_datos
from bson import ObjectId

router = APIRouter()

coleccion_citas = base_de_datos["citas"]

@router.post("/citas", response_model=Cita)
async def crear_cita(cita: Cita):
    # Convertir campos fecha y hora a string
    cita_dict = cita.dict()
    cita_dict["fecha"] = cita.fecha.isoformat()  # 'YYYY-MM-DD'
    cita_dict["hora"] = cita.hora.strftime("%H:%M")  # 'HH:MM'

    resultado = await coleccion_citas.insert_one(cita_dict)
    if resultado.inserted_id:
        return cita
    raise HTTPException(status_code=500, detail="No se pudo crear la cita")

@router.get("/citas", response_model=list[Cita])
async def obtener_citas():
    citas = []
    async for cita in coleccion_citas.find():
        cita["_id"] = str(cita["_id"])  # por si lo necesitas en el futuro
        citas.append(Cita(**cita))
    return citas