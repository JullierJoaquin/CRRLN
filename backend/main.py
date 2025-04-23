from fastapi import FastAPI
from backend.api import materiales, presupuestos

app = FastAPI(title="Presupuestador de Obras")

app.include_router(materiales.router, prefix="/materiales", tags=["Materiales"])
app.include_router(presupuestos.router, prefix="/presupuestos", tags=["Presupuestos"])

@app.get("/")
def read_root():
    return {"message": "API del Presupuestador de Obras"}
