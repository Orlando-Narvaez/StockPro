# StockPro 📦
Sistema de Gestión de Inventario construido con FastAPI y MongoDB.

## 🚀 Descripción
**StockPro** es una API RESTful que permite administrar productos, movimientos de inventario (entradas y salidas) y usuarios. Diseñada para pequeñas y medianas empresas que desean llevar control digital de su stock.

---

## 🛠️ Tecnologías utilizadas

### Backend
- 🐍 Python 3.10+
- ⚡ FastAPI
- 🛢️ MongoDB (Atlas)
- 🔐 JWT para autenticación
- 📦 Pydantic para validación
- 🔑 python-jose & passlib para seguridad

---

## ⚙️ Instalación y ejecución local

1. **Clona el repositorio**

```bash
git clone https://github.com/Orlando-Narvaez/StockPro.git
cd StockPro/backend
```

2. **Crea un entorno virtual**

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

3. **Instala dependencias**

pip install -r requirements.txt

4. **Configura tus variables de entorno en .env**

MONGO_URI=mongodb+srv://usuario:clave@cluster.mongodb.net/inventario
JWT_SECRET_KEY=una_clave_secreta_segura
JWT_ALGORITHM=HS256

5. **Ejecuta el servidor**

uvicorn app.main:app --reload

6. **Visita la documentación interactiva en:**

http://localhost:8000/docs

## ✅ Funcionalidades actuales

 - CRUD de productos
 - Registro e inicio de sesión de usuarios
 - Gestión de entradas/salidas de stock
 - Autenticación con JWT
 - Dashboard (próximamente)
 - Frontend con React (próximamente)

 ## 📦 Despliegue

 En el futuro se podrá desplegar en:
 - Backend: Railway o Render
 - Base de datos: MongoDB Atlas
 - Frontend: Vercel

 ## 📄 Licencia

Este proyecto está licenciado bajo la MIT License.

## 🙌 Autor

Desarrollado por: Orlando Narvaez Baracaldo