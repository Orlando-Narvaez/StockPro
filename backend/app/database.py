from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener la URL de conexión a MongoDB desde la variable de entorno
MONGO_URL = os.getenv("MONGO_URL")

# Crear el cliente de MongoDB
cliente = AsyncIOMotorClient(MONGO_URL)

# Seleccionar la base de datos (puedes cambiar el nombre)
base_de_datos = cliente["stockpro_db"]