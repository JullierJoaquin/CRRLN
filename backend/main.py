from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, auth

# Cargar variables de entorno
load_dotenv()

# Inicializar Firebase solo si no está inicializado
cred_path = "backend/firebase_credentials.json"
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Crear instancia de FastAPI
app = FastAPI()

# Agregar middleware de sesiones
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "dev"))

# Montar archivos estáticos y configurar templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Middleware para verificar el token de Firebase
def verify_firebase_token(request: Request):
    id_token = request.cookies.get("firebase_token")
    if not id_token:
        return None
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print("❌ Error verificando token:", e)
        return None

# Ruta para login
@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Ruta protegida para presupuestos
@app.get("/presupuestos", response_class=HTMLResponse)
async def presupuestos(request: Request):
    user = verify_firebase_token(request)
    if not user:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("presupuestos.html", {"request": request, "user": user})
