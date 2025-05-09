
# MTRL Web Service App

Una aplicación web desarrollada para gestionar presupuestos de materiales de construcción, con autenticación de usuarios mediante Firebase, visualización interactiva de datos y diseño moderno utilizando Tailwind CSS.

---

## 🚀 Características principales

- 🔐 **Autenticación de usuarios** con Firebase (login/registro/logout)
- 🧱 **Carga dinámica de materiales** con autocompletado inteligente
- 📊 **Visualización de presupuesto** con gráficos interactivos (Chart.js y Plotly)
- 💾 **Guardado automático** de presupuestos por usuario en Firestore
- 🎨 Estética basada en paleta de colores inspirada en Van Gogh

---

## 🧪 Tecnologías utilizadas

- **Frontend:** HTML, Tailwind CSS, JavaScript (modular)
- **Gráficos:** [Chart.js](https://www.chartjs.org/), [Plotly.js](https://plotly.com/javascript/)
- **Backend (Auth/DB):** Firebase Authentication + Firestore

---

## ⚙️ Instalación y ejecución

1. Cloná este repositorio:

```bash
git clone https://github.com/tu-usuario/MTRL_web_service_app.git
cd MTRL_web_service_app
```

2. Serví el frontend con tu herramienta preferida:

- Usando Python (por ejemplo con Flask o FastAPI)
- Servidor local simple:

```bash
python3 -m http.server
```

3. Configurá tu archivo `firebase-config.js` con las claves de tu proyecto Firebase.

---

## 📁 Estructura del proyecto

```
/static/
  ├── js/
  │    ├── presupuestos.js
  │    └── firebase-config.js
  ├── css/
  │    └── login.css
  └── images/
       └── logoteca.png, default_avatar.png

/templates/
  ├── dashboard.html
  └── login.html

main.py (si usás un backend como FastAPI)
```

---

## 📊 Capturas

![Dashboard](./screenshots/dashboard.png)

---

## 📬 Contribuciones

¡Toda mejora o sugerencia es bienvenida! Podés abrir un issue o un pull request.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.
