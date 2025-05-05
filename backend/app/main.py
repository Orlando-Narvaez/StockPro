from fastapi import FastAPI

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