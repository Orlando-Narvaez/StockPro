from pydantic import BaseModel, Field
from typing import Optional

class Producto(BaseModel):
    nombre: str = Field(..., description="Nombre del producto")
    descripcion: Optional[str] = Field(None, description="Descripción del producto")
    precio: float = Field(..., gt=0, description="Precio del producto, debe ser mayor que 0")
    cantidad: int = Field(..., ge=0, description="Cantidad en stock, no puede ser negativa")
    categoria: Optional[str] = Field(None, description="Categoría del producto")