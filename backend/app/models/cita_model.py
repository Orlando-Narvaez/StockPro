from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, time

class Cita(BaseModel):
    cliente: str = Field(..., description="Nombre del cliente")
    fecha: date = Field(..., description="Fecha de la cita en formato AAAA-MM-DD")
    hora: time = Field(..., description="Hora de la cita en formato HH:MM")
    lugar: str = Field(..., description="Lugar donde se realizará la cita")
    descripcion: Optional[str] = Field(None, description="Descripción o motivo de la cita")
    estado: str = Field(default="programada", description="Estado de la cita: programada, completada o cancelada")