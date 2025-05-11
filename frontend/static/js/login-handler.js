// login-handler.js
import { auth } from "./firebase-config.js";
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
} from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

// ✅ Mostrar formulario según localStorage
window.addEventListener("DOMContentLoaded", () => {
  const mostrarRegistro = localStorage.getItem("mostrarRegistro");
  if (mostrarRegistro === "true") {
    const checkbox = document.getElementById("check");
    if (checkbox) checkbox.checked = true;
  }
  localStorage.removeItem("mostrarRegistro");
});

// ✅ Registro
document.addEventListener("DOMContentLoaded", () => {
  const registerBtn = document.querySelector(".registration .button");
  const loginBtn = document.querySelector(".login .button");

  if (registerBtn) {
    registerBtn.addEventListener("click", () => {
      const email = document.querySelector(".registration input[type='text']").value;
      const pass1 = document.getElementById("register-pass1").value;
      const pass2 = document.getElementById("register-pass2").value;

      if (pass1 !== pass2) {
        alert("Las contraseñas no coinciden.");
        return;
      }

      createUserWithEmailAndPassword(auth, email, pass1)
        .then((userCredential) => {
          alert("Registro exitoso");
          console.log(userCredential.user);
        })
        .catch((error) => {
          alert(error.message);
          console.error(error);
        });
    });
  }

  // ✅ Login
  if (loginBtn) {
    loginBtn.addEventListener("click", () => {
      const email = document.querySelector(".login input[type='text']").value;
      const password = document.querySelector(".login input[type='password']").value;

      signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
          alert("Inicio de sesión exitoso");
          console.log(userCredential.user);
          window.location.href = "/dashboard"; // Redirigí según tu flujo
        })
        .catch((error) => {
          alert(error.message);
          console.error(error);
        });
    });
  }
});