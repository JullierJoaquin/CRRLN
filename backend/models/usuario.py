from sqlmodel import SQLModel, Field
from typing import Optional

class Usuario(SQLModel, table=True):
    id: str = Field(primary_key=True)  # UID Firebase
    nombre: Optional[str] = None
