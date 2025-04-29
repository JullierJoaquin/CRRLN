# backend/users/schemas.py

from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users import schemas
from sqlalchemy import Boolean, Column, Integer, String
from backend.db.database import Base  # Tu declarative_base()



# Modelo de base de datos
class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

# Esquema de creación (registro)
class UserCreate(schemas.BaseUserCreate):
    pass

# Esquema de lectura (response)
class UserRead(schemas.BaseUser[int]):
    pass

# Esquema de actualización
class UserUpdate(schemas.BaseUserUpdate):
    pass
