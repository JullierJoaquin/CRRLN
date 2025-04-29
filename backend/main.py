# -----------------------------------
# IMPORTS
# -----------------------------------
from fastapi import FastAPI, Request, Form, Depends, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from backend.db.database import SessionLocal, Base, engine
from backend.db import models
from backend.auth import verify_password

from backend.users.schemas import User, UserCreate, UserRead, UserUpdate
from backend.users.manager import UserManager

from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from dotenv import load_dotenv
import os

# -----------------------------------
# CONFIGURACIÓN APP
# -----------------------------------
app = FastAPI(title="CRRLN")
load_dotenv()

# Plantillas y archivos estáticos
templates = Jinja2Templates(directory="backend/templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# -----------------------------------
# BASE DE DATOS
# -----------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_user_db():
    db = SessionLocal()
    yield SQLAlchemyUserDatabase(User, db)

# -----------------------------------
# AUTHENTICATION CONFIG
# -----------------------------------
SECRET = os.getenv("CRRLN_SECRET")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# -----------------------------------
# FASTAPI USERS
# -----------------------------------
fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [auth_backend],
)

# -----------------------------------
# ROUTERS
# -----------------------------------
# Auth - Login JWT
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

# Registro de usuarios
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# Información de usuario
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

# -----------------------------------
# FRONTEND ROUTES
# -----------------------------------
@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})

@app.get("/presupuestos", response_class=HTMLResponse)
async def presupuestos(request: Request):
    return templates.TemplateResponse("presupuestos.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and verify_password(password, user.hashed_password):
        return RedirectResponse(url="/presupuestos", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Usuario o contraseña incorrectos"})

@app.get("/register", response_class=HTMLResponse)
async def register_redirect(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})
