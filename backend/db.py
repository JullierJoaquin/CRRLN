from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./materiales.db"
engine = create_engine(DATABASE_URL, echo=True)

def crear_db():
    import backend.models.usuario
    import backend.models.presupuesto
    import backend.models.rubro
    import backend.models.material
    import backend.models.item_presupuesto

    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
