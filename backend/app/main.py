from fastapi import FastAPI
from app.database import base_de_datos  # Importamos la base de datos

# Crear instancia de la aplicación FastAPI
aplicacion = FastAPI(
    title="StockPro API",
    description="API para la gestión de inventario con FastAPI y MongoDB",
    version="0.1.0"
)

# Ruta raíz para probar que el servidor funciona
@aplicacion.get("/")
def inicio():
    return {"mensaje": "Bienvenido a StockPro 🚀"}

@aplicacion.get("/ping-db")
async def ping_base_de_datos():
    try:
        # Realizamos una operación muy simple: listar las colecciones
        colecciones = await base_de_datos.list_collection_names()
        return {"estado": "conectado", "colecciones": colecciones}
    except Exception as error:
        return {"estado": "error", "detalle": str(error)}