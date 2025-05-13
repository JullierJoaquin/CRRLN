from sqlmodel import Session, select
from backend.db import engine
from backend.models.material import Material
from backend.models.rubro import Rubro

with Session(engine) as session:
    materiales = session.exec(select(Material).limit(5)).all()
    print("📦 Materiales:")
    for m in materiales:
        print(f"{m.codigo} | {m.descripcion} | {m.costo_total}")

    print("\n🧱 Rubros:")
    rubros = session.exec(select(Rubro)).all()
    for r in rubros:
        print(f"{r.codigo} - {r.nombre}")
