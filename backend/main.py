
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from backend.db import crear_db
from backend.routers import materiales

from backend.routers import presupuestos

crear_db()  # crea las tablas al iniciar


load_dotenv()

app = FastAPI()

# CORS para permitir comunicación con frontend JS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción: usar solo tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(materiales.router)

# Archivos estáticos y plantillas
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend")

# Rutas HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
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

# API REST
app.include_router(presupuestos.router)