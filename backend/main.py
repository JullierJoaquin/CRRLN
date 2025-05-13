from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from backend.db import crear_db
from backend.routers import materiales, presupuestos

# Crea la base de datos y las tablas al iniciar
crear_db()

# Cargar variables de entorno (Firebase, etc.)
load_dotenv()

# Inicializar FastAPI
app = FastAPI()

# Habilitar CORS (para conexión JS desde HTML local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ En producción usar ["https://tu-dominio.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar carpeta estática (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Plantillas HTML (Jinja2)
templates = Jinja2Templates(directory="frontend")

# Rutas HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    firebase_config = {
        "apiKey": os.getenv("FIREBASE_API_KEY"),
        "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
        "projectId": os.getenv("FIREBASE_PROJECT_ID"),
        "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
        "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
        "appId": os.getenv("FIREBASE_APP_ID")
    }
    return templates.TemplateResponse("login.html", {
        "request": request,
        "firebase_config": firebase_config
    })

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Routers para API REST
app.include_router(materiales.router, prefix="/api", tags=["materiales"])
app.include_router(presupuestos.router, prefix="/api", tags=["presupuestos"])
