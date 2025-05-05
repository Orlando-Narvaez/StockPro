from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import base_de_datos  # Importamos la base de datos
from app.routes import producto_route
from app.routes import cita_route

# Crear instancia de la aplicación FastAPI
aplicacion = FastAPI(
    title="StockPro API",
    description="API para la gestión de inventario y agendamiento de citas con FastAPI y MongoDB",
    version="1.0.0"
)

# Middleware CORS (permite conexiones desde el frontend)
aplicacion.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, reemplazar por el dominio del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta raíz para probar que el servidor funciona
@aplicacion.get("/")
def inicio():
    return {"mensaje": "Bienvenido a StockPro 🚀"}

# Ruta para comprobar la conexión con la base de datos
@aplicacion.get("/ping-db")
async def ping_base_de_datos():
    try:
        colecciones = await base_de_datos.list_collection_names()
        return {"estado": "conectado", "colecciones": colecciones}
    except Exception as error:
        return {"estado": "error", "detalle": str(error)}

# Rutas de la API
aplicacion.include_router(producto_route.router)
aplicacion.include_router(cita_route.router)