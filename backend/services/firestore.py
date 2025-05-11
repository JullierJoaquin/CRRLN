
from firebase_admin import firestore
from backend.models.presupuesto import Presupuesto

def guardar_presupuesto(presupuesto: Presupuesto):
    db = firestore.client()
    ref = db.collection("presupuestos").document(presupuesto.usuario_id)
    ref.set({
        "materiales": [item.dict() for item in presupuesto.materiales],
        "actualizado": presupuesto.actualizado
    })
