function agregarMaterial() {
  const input = document.getElementById("nuevo-material");
  const nombre = input.value.trim();
  if (!nombre) return;

  const tabla = document.getElementById("tabla-materiales");
  const nuevaFila = document.createElement("tr");
  nuevaFila.className = "border-b";

  nuevaFila.innerHTML = `
    <td class="px-4 py-2">${nombre}</td>
    <td class="px-4 py-2 unidad">-</td>
    <td class="px-4 py-2 precio">0</td>
    <td class="px-4 py-2">
      <input type="number" min="0" class="cantidad w-20 p-1 border rounded text-center"
             oninput="calcularSubtotal(this)">
    </td>
    <td class="px-4 py-2 subtotal">$0</td>
    <td class="px-4 py-2">
      <button onclick="eliminarFila(this)"
              class="bg-[#202F3C] hover:bg-blue-800 text-white px-3 py-2 rounded shadow"
              title="Eliminar">
        <svg xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 24 24" class="w-4 h-4">
          <path d="M9 3v1H4v2h1v13c0 1.1.9 2 2 2h10a2 2 0 0 0 2-2V6h1V4h-5V3H9zm2 0h2v1h-2V3zM7 6h10v13H7V6z"/>
        </svg>
      </button>
    </td>
  `;

  tabla.appendChild(nuevaFila);
  input.value = "";
  input.focus();
}


function calcularSubtotal(input) {
  const row = input.closest("tr");
  const cantidad = parseFloat(input.value) || 0;
  const precio = parseFloat(row.querySelector(".precio").innerText) || 0;
  const subtotal = cantidad * precio;
  row.querySelector(".subtotal").innerText = `$${subtotal.toFixed(2)}`;
}

function eliminarFila(boton) {
  const fila = boton.closest("tr");
  fila.remove();
}
