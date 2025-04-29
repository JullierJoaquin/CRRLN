from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean

# URL de la base de datos
# Para pruebas podés usar SQLite:
SQLALCHEMY_DATABASE_URL = "sqlite:///./crrln.db" # (Cuando subas a producción vas a cambiar esto a PostgreSQL)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
