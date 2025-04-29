from sqlalchemy import Column, Integer, String, Float, Boolean
from backend.db.database import Base


class Material(Base):
    __tablename__ = "materiales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)
    unidad = Column(String, nullable=False)
    precio = Column(Float, nullable=False)