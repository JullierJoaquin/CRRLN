from sqlmodel import Session, select
from backend.db import engine
from backend.models.material import Material

with Session(engine) as session:
    materiales = session.exec(select(Material)).all()
    print(f"Se encontraron {len(materiales)} materiales.")
    for m in materiales[:5]:
        print(m.descripcion, m.costo_total)
