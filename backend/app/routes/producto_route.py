from fastapi import APIRouter, HTTPException
from app.models.producto_model import Producto
from app.database import base_de_datos
from bson import ObjectId

router = APIRouter()
coleccion_productos = base_de_datos["productos"]

@router.post("/productos", response_model=Producto)
async def crear_producto(producto: Producto):
    resultado = await coleccion_productos.insert_one(producto.dict())
    if resultado.inserted_id:
        return producto
    raise HTTPException(status_code=500, detail="No se pudo crear el producto")

@router.get("/productos", response_model=list[Producto])
async def obtener_productos():
    productos = []
    async for producto in coleccion_productos.find():
        producto["_id"] = str(producto["_id"])
        productos.append(Producto(**producto))
    return productos