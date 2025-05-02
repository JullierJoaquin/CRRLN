# MTRL 🔐📐

MTRL es una aplicación web desarrollada con **FastAPI** que permite manejar presupuestos de forma segura mediante autenticación con **Firebase**. Está pensada como base para un sistema moderno de presupuestado en arquitectura o construcción.

---

## 🛠️ Tecnologías utilizadas

- **FastAPI** – Backend moderno y rápido
- **Firebase Authentication** – Login de usuarios con Google u otros métodos
- **Firebase Admin SDK** – Verificación de tokens en el backend
- **Jinja2** – Motor de plantillas para HTML
- **HTML + Tailwind CSS** – Interfaz simple y personalizable

---

## 🚀 Funcionalidades

- 🔒 Login seguro usando Firebase (Google Auth y más)
- 🔐 Protección de páginas (como `/presupuestos`) solo para usuarios autenticados
- 🧪 Middleware que valida el token JWT con Firebase
- ⚙️ Carga de variables de entorno desde `.env`

---

## 📁 Estructura de carpetas

MTRL/
├── backend/
│ ├── main.py # App principal
│ └── firebase_credentials.json
├── static/ # Archivos CSS, JS
├── templates/
│ ├── login.html # Página de login
│ └── presupuestos.html # Página protegida
├── .env # Variables de entorno
└── requirements.txt # Dependencias


---

## 🔐 Configuración

1. **Clona el repositorio:**
```bash
git clone https://github.com/JullierJoaquin/MTRL.git
cd MTRL
```

2. Agrega tus credenciales de Firebase:

    Descarga tu archivo JSON desde Firebase Console
    Guárdalo en backend/firebase_credentials.json
    

3. Crea un archivo .env:
```bash
SECRET_KEY=clave_super_segura_generada
FIREBASE_CREDENTIALS=backend/firebase_credentials.json
```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```


5. Inicia el servidor:
```bash
uvicorn backend.main:app --reload
```


- Panel de usuarios: `/users/me`

Próximamente:
- Recuperación de contraseña
- Control de sesiones
- Soporte para guardar presupuestos
- Registro de nuevos usuarios en base de datos
- Exportación de reportes a PDF / Excel
- Panel de administración

---

## 🤝 Licencia

Este proyecto está bajo licencia MIT. Libre para usar y modificar con atribución.

---

## 📬 ¿Sugerencias o ideas?

¡Abrí un issue o escribime! Toda colaboración es bienvenida.