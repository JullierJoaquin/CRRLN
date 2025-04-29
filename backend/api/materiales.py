from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from backend.db.database import SessionLocal
from backend.db import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/materiales/search")
def search_material(nombre: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    material = db.query(models.Material).filter(models.Material.nombre.ilike(f"%{nombre}%")).first()
    if material:
        return {
            "nombre": material.nombre,
            "unidad": material.unidad,
            "precio": material.precio
        }
    return {"error": "Material no encontrado"}
