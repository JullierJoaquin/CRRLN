from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from backend.db import get_session
from backend.models.material import Material
from backend.models.rubro import Rubro

router = APIRouter()

@router.get("/api/materiales_completo")
def get_materiales(session: Session = Depends(get_session)):
    stmt = select(Material, Rubro.nombre).join(Rubro, Material.rubro_id == Rubro.id, isouter=True)
    results = session.exec(stmt).all()
    return [
        {
            "codigo": m.codigo,
            "descripcion": m.descripcion,
            "unidad": m.unidad,
            "costo_total": m.costo_total,
            "rubro_nombre": rubro,
            "fecha": m.fecha.isoformat() if m.fecha else None,
            "fuente": m.fuente
        }
        for m, rubro in results
    ]
