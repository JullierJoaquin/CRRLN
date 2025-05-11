from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class ItemPresupuesto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    presupuesto_id: int = Field(foreign_key="presupuesto.id")
    material_id: int = Field(foreign_key="material.id")
    cantidad: float
    subtotal: float

    presupuesto: "Presupuesto" = Relationship(back_populates="items")
