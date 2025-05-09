
console.log("✅ presupuestos.js cargado correctamente");

const materialesBase = [
  { nombre: "Cemento", unidad: "bolsa", precio: 5500 },
  { nombre: "Arena", unidad: "m³", precio: 3500 },
  { nombre: "Grava", unidad: "m³", precio: 4000 },
  { nombre: "Ladrillo común", unidad: "unidad", precio: 90 },
  { nombre: "Hierro 8mm", unidad: "barra", precio: 1800 },
  { nombre: "Hierro 12mm", unidad: "barra", precio: 3200 },
  { nombre: "Cal hidratada", unidad: "bolsa", precio: 5200 },
  { nombre: "Pintura látex blanca", unidad: "l", precio: 950 },
  { nombre: "Cable 2,5mm", unidad: "metro", precio: 280 },
  { nombre: "Caño PVC 40mm", unidad: "metro", precio: 900 },
];

window.agregarMaterial = function () {
  const materialNombre = document.getElementById("nuevo-material").value.trim();
  const materialObj = materialesBase.find(m => m.nombre.toLowerCase() === materialNombre.toLowerCase());

  if (!materialObj) {
    alert("Por favor seleccioná un material válido.");
    return;
  }

  const unidad = materialObj.unidad;
  const precio = materialObj.precio;
  const precioTexto = `$${precio.toLocaleString()}`;

  const fila = document.createElement("tr");
  fila.innerHTML = `
    <td class="px-4 py-2">${materialNombre}</td>
    <td class="px-4 py-2">${unidad}</td>
    <td class="px-4 py-2 precio">${precioTexto}</td>
    <td class="px-4 py-2">
      <input type="number" min="1" value="1" class="w-16 border rounded p-1 text-center"
             oninput="calcularSubtotal(this)">
    </td>
    <td class="px-4 py-2 subtotal">$${precio.toFixed(2)}</td>
    <td class="px-4 py-2">
      <button class="text-red-600 hover:underline" onclick="this.closest('tr').remove()">Eliminar</button>
    </td>
  `;

  document.getElementById("tabla-materiales").appendChild(fila);
  document.getElementById("nuevo-material").value = "";
  document.querySelector(".unidad").textContent = "-";
  document.querySelector(".precio").textContent = "-";
};

document.addEventListener("DOMContentLoaded", () => {
  const inputMaterial = document.getElementById("nuevo-material");
  const listaSugerencias = document.getElementById("sugerencias");
  const unidadCampo = document.querySelector(".unidad");
  const precioCampo = document.querySelector(".precio");

  inputMaterial.addEventListener("input", () => {
    const valor = inputMaterial.value.toLowerCase().trim();
    listaSugerencias.innerHTML = "";

    if (!valor) {
      listaSugerencias.classList.add("hidden");
      unidadCampo.textContent = "-";
      precioCampo.textContent = "-";
      return;
    }

    const filtrados = materialesBase.filter(m => m.nombre.toLowerCase().includes(valor));
    if (filtrados.length === 0) {
      listaSugerencias.classList.add("hidden");
      return;
    }

    filtrados.forEach(material => {
      const item = document.createElement("li");
      item.textContent = material.nombre;
      item.className = "px-4 py-2 hover:bg-gray-100 cursor-pointer";
      item.addEventListener("click", () => {
        inputMaterial.value = material.nombre;
        unidadCampo.textContent = material.unidad;
        precioCampo.textContent = `$${material.precio.toLocaleString()}`;
        listaSugerencias.classList.add("hidden");
      });
      listaSugerencias.appendChild(item);
    });

    listaSugerencias.classList.remove("hidden");
  });

  document.addEventListener("click", (e) => {
    if (!inputMaterial.contains(e.target) && !listaSugerencias.contains(e.target)) {
      listaSugerencias.classList.add("hidden");
    }
  });
});

window.calcularSubtotal = function (input) {
  const row = input.closest("tr");
  const cantidad = parseFloat(input.value) || 0;
  const precioTexto = row.querySelector(".precio").textContent;
  const precio = parseFloat(precioTexto.replace("$", "").replace(/\./g, "").replace(",", ".")) || 0;
  const subtotal = cantidad * precio;
  row.querySelector(".subtotal").textContent = `$${subtotal.toFixed(2)}`;
};

import { auth } from "./firebase-config.js";
import {
  onAuthStateChanged,
  signOut
} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

// Mostrar info del usuario
onAuthStateChanged(auth, (user) => {
  if (user) {
    document.getElementById("user-name").textContent = user.displayName || user.email;
    document.getElementById("user-photo").src = user.photoURL || "/static/images/default_avatar.png";
  } else {
    window.location.href = "/login";
  }
});

// Función logout
window.logout = function () {
  signOut(auth).then(() => {
    window.location.href = "/login";
  }).catch((error) => {
    console.error("Error al cerrar sesión:", error);
  });
};
