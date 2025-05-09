// firebase-config.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js";

// REEMPLAZÁ ESTOS VALORES con los de tu proyecto Firebase
const firebaseConfig = {
  apiKey: "AIzaSyDdhhOgNNR6g90tuLO5AhR3sL4S-d_OM0Q",
  authDomain: "mtrl-fb9da.firebaseapp.com",
  projectId: "mtrl-fb9da",
  storageBucket: "mtrl-fb9da.firebasestorage.com",
  messagingSenderId: "866092445579",
  appId: "1:866092445579:web:f2ef6ca33393978f6f498e",
  measurementId: "G-MDLK1ECZPM"
};



// Inicializar Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);