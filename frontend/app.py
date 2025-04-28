import streamlit as st
import pandas as pd

# Cargar los datos (puede ser reemplazado luego por llamada a la API)
@st.cache_data
def cargar_datos():
    return pd.DataFrame({
        "nombre": ["Cemento", "Ladrillo", "Arena", "Hierro", "Mano de obra oficial"],
        "unidad": ["bolsa", "unidad", "m3", "kg", "hora"],
        "precio": [8500, 120, 7500, 520, 2300],
        "rubro": ["Material", "Material", "Material", "Material", "Mano de obra"]
    })

datos = cargar_datos()

st.title("CRRLN")

# Selección de ítems
st.subheader("Seleccioná ítems del presupuesto")
seleccion = st.multiselect("Elegí materiales o mano de obra:", datos["nombre"].tolist())

# Formulario de cantidades
presupuesto = []
for item in seleccion:
    fila = datos[datos["nombre"] == item].iloc[0]
    cantidad = st.number_input(f"Ingresá cantidad de {item} ({fila['unidad']}):", min_value=0.0, step=1.0)
    subtotal = cantidad * fila["precio"]
    presupuesto.append({
        "nombre": item,
        "unidad": fila["unidad"],
        "precio_unitario": fila["precio"],
        "cantidad": cantidad,
        "subtotal": subtotal
    })

# Mostrar presupuesto
if presupuesto:
    df_presupuesto = pd.DataFrame(presupuesto)
    st.subheader("🧾 Resultado del presupuesto")
    st.dataframe(df_presupuesto)
    st.markdown(f"### 💰 Total: ${df_presupuesto['subtotal'].sum():,.2f}")

    # Placeholder botón exportación
    st.button("📤 Exportar a Excel (próximamente)")

else:
    st.info("Seleccioná al menos un ítem para comenzar.")

