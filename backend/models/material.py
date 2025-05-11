from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Material(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str
    descripcion: str
    unidad: str
    costo_material: float
    costo_ejecucion: float
    costo_total: float
    rubro_id: int = Field(foreign_key="rubro.id")
    fuente: Optional[str] = None
    fecha: Optional[date] = None
