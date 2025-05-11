from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Presupuesto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    usuario_id: str = Field(foreign_key="usuario.id")
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)

    items: List["ItemPresupuesto"] = Relationship(back_populates="presupuesto")
