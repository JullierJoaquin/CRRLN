import pdfplumber
import pandas as pd
from datetime import date
from sqlmodel import Session
from backend.db import engine
from backend.models.rubro import Rubro
from backend.models.material import Material

FUENTE = "Revista Cifras - Mayo 2025"
FECHA = date(2025, 5, 1)

def cargar_cifras_pdf(ruta_pdf):
    with pdfplumber.open(ruta_pdf) as pdf, Session(engine) as session:
        rubro_actual = None
        for pagina in pdf.pages:
            tablas = pagina.extract_tables()
            for tabla in tablas:
                for fila in tabla:
                    if not fila or not fila[0]:
                        continue

                    # Detectar rubro si solo tiene dos columnas
                    if len(fila) == 2 and fila[0].strip().startswith("Rubro"):
                        codigo = fila[0].strip().split(" ")[-1]
                        nombre = fila[1].strip()
                        rubro_actual = Rubro(codigo=codigo, nombre=nombre)
                        session.add(rubro_actual)
                        session.commit()
                        continue

                    # Detectar material con estructura esperada
                    if len(fila) >= 6 and fila[0].strip().isdigit():
                        try:
                            codigo = fila[0].strip()
                            descripcion = fila[1].strip()
                            unidad = fila[2].strip()
                            costo_material = float(fila[3].replace(".", "").replace(",", "."))
                            costo_ejecucion = float(fila[4].replace(".", "").replace(",", "."))
                            costo_total = float(fila[5].replace(".", "").replace(",", "."))

                            material = Material(
                                codigo=codigo,
                                descripcion=descripcion,
                                unidad=unidad,
                                costo_material=costo_material,
                                costo_ejecucion=costo_ejecucion,
                                costo_total=costo_total,
                                rubro_id=rubro_actual.id if rubro_actual else None,
                                fuente=FUENTE,
                                fecha=FECHA
                            )
                            session.add(material)
                        except Exception as e:
                            print("Error en fila:", fila, "→", e)

        session.commit()
        print("✅ Datos cargados exitosamente.")

if __name__ == "__main__":
    cargar_cifras_pdf("data/350_Revista CIFRAS Digital Mayo 2025 - Costos x rubro.xls - CostosUnitarios.pdf")