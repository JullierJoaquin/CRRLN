# 🏗️ CRRLN - Presupuestos de Obras Rápidos y Profesionales

CRRLN es una aplicación web pensada para facilitar la creación, gestión y exportación de presupuestos de obras de construcción en Argentina, con foco en la región del Litoral (Rosario, Córdoba, Buenos Aires).

> ⚠️ *Este proyecto se encuentra en desarrollo activo.*

---

## 🚀 Características principales

- Generación de presupuestos por ítem, rubro y región
- Cálculo automático con base de datos precargada
- Exportación a Excel y PDF
- Interfaz moderna (Tailwind)
- Panel interactivo con tabla editable
- Autenticación segura (FastAPI Users)
- Login tradicional + preparado para login social (Google, GitHub, etc.)

---

## ⚙️ Tecnologías utilizadas

- **Python 3.10**
- **FastAPI**
- **SQLAlchemy**
- **Jinja2 + Tailwind CSS**
- **FastAPI Users** (gestión de usuarios)
- **Uvicorn** (ASGI server)
- **SQLite** (modo local, lista para migrar)
- **python-dotenv** (manejo de secretos)
- **Docker-ready** (opcional)

---

## 🧑‍💻 Instalación local

1. Cloná el repositorio:
```bash
git clone https://github.com/JullierJoaquin/CRRLN.git
cd CRRLN
```

2. Activá un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
```

3. Instalá las dependencias:
```bash
pip install -r requirements.txt
```

4. Configurá las variables de entorno en un archivo `.env`:
```env
CRRLN_SECRET=tu_clave_segura
```

5. Ejecutá el servidor:
```bash
uvicorn backend.main:app --reload
```

6. Accedé en tu navegador:
```
http://127.0.0.1:8000
```

---

## 🔐 Autenticación

- Registro: `/auth/register`
- Login JWT: `/auth/jwt/login`
- Panel de usuarios: `/users/me`

Próximamente:
- Login con Google / GitHub
- Recuperación de contraseña
- Control de sesiones

---

## 📁 Estructura del proyecto

```
CRRLN/
├── backend/
│   ├── main.py
│   ├── db/
│   ├── users/
│   ├── templates/
│   └── static/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📈 Roadmap

- [x] Interfaz básica de presupuestos
- [x] Sistema de usuarios con login seguro
- [ ] Login con Google y redes sociales
- [ ] Dashboard personal con historial
- [ ] Alerta de cambios en precios
- [ ] Modo offline y exportación sin conexión
- [ ] Sistema de versión de presupuestos

---

## 🤝 Licencia

Este proyecto está bajo licencia MIT. Libre para usar y modificar con atribución.

---

## 👨‍💻 Autor

Desarrollado por [Joaquín Jullier](https://github.com/JullierJoaquin) — estudiante de arquitectura y programador autodidacta apasionado por la integración entre tecnología, diseño y datos.

---

## 📬 ¿Sugerencias o ideas?

¡Abrí un issue o escribime! Toda colaboración es bienvenida.
