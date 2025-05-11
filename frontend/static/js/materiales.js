window.baseMateriales = [];

const tablaMateriales = document.getElementById("tabla-materiales");
const buscadorMateriales = document.getElementById("buscador-materiales");

async function cargarMateriales() {
  try {
    const res = await fetch("/api/materiales_completo");
    window.baseMateriales = await res.json();
    renderizarTabla(window.baseMateriales);
  } catch (error) {
    console.error("Error al cargar materiales:", error);
  }
}

function renderizarTabla(datos) {
  if (!tablaMateriales) return;
  tablaMateriales.innerHTML = "";
  datos.forEach(m => {
    const fila = `
      <tr>
        <td class="px-4 py-2">${m.codigo}</td>
        <td class="px-4 py-2">${m.descripcion}</td>
        <td class="px-4 py-2">${m.unidad}</td>
        <td class="px-4 py-2">$${m.costo_total?.toFixed(2) || '-'}</td>
        <td class="px-4 py-2">${m.rubro_nombre || "-"}</td>
        <td class="px-4 py-2">${m.fecha || "-"}</td>
        <td class="px-4 py-2">${m.fuente || "-"}</td>
      </tr>`;
    tablaMateriales.insertAdjacentHTML("beforeend", fila);
  });
}

if (buscadorMateriales) {
  buscadorMateriales.addEventListener("input", () => {
    const texto = buscadorMateriales.value.toLowerCase();
    const filtrados = window.baseMateriales.filter(m =>
      m.descripcion.toLowerCase().includes(texto) ||
      m.codigo.toLowerCase().includes(texto)
    );
    renderizarTabla(filtrados);
  });
}

window.mostrarSeccion = function(nombre) {
  const presupuestos = document.querySelector("main > .flex");
  const materiales = document.getElementById("seccion-materiales");

  if (nombre === "materiales") {
    presupuestos?.classList.add("hidden");
    materiales?.classList.remove("hidden");
    if (window.baseMateriales.length === 0) cargarMateriales();
  } else {
    presupuestos?.classList.remove("hidden");
    materiales?.classList.add("hidden");
  }
};