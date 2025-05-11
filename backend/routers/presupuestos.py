
from fastapi import APIRouter
from backend.models.presupuesto import Presupuesto
from backend.services.firestore import guardar_presupuesto

router = APIRouter(prefix="/presupuestos", tags=["presupuestos"])

@router.post("/guardar")
async def guardar_presupuesto_endpoint(presupuesto: Presupuesto):
    guardar_presupuesto(presupuesto)
    return {"mensaje": "Presupuesto guardado correctamente"}
