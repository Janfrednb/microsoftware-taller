# 🏍️ MicroTaller - Gestión de Servicios

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=flat&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=flat&logo=bootstrap&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Pytest-green?style=flat&logo=pytest&logoColor=white)

Sistema de administración para talleres mecánicos desarrollado con **Python** y **Flask**. Esta herramienta permite gestionar el flujo de trabajo diario de un taller de motocicletas con una arquitectura modular y escalable.

---

## ✨ Características Principales

- **📊 Dashboard Dinámico:** Visualización en tiempo real de métricas clave (Citas del día y Alistamientos activos).
- **📅 Agenda de Citas:** API RESTful para agendar, consultar y cancelar citas con clientes.
- **🔧 Gestión de Alistamientos:** Control de checklist de ingreso (frenos, luces, aceite) mediante formularios dinámicos.
- **🎨 Diseño Minimal UI:** Interfaz moderna y responsive utilizando **Bootstrap 5** y JavaScript (Fetch API).
- **🏗️ Arquitectura Limpia:** Código organizado bajo el patrón **MVC** (Model-View-Controller) separando Rutas, Servicios y Modelos.

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3, Flask (Blueprints para modularidad).
- **Frontend:** HTML5, CSS3, Jinja2, JavaScript (ES6+).
- **Estilos:** Bootstrap 5 & Bootstrap Icons.
- **Testing:** Pytest (Pruebas unitarias e integración).

---

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/microsoftware-taller.git](https://github.com/tu-usuario/microsoftware-taller.git)
   cd microsoftware-taller
   ```

Crear y activar el entorno virtual:

Bash

# En Windows:

python -m venv venv
.\venv\Scripts\activate

# En Mac/Linux:

python3 -m venv venv
source venv/bin/activate
Instalar dependencias:

Bash
pip install -r requirements.txt
(Si no tienes el archivo, instala: pip install flask pytest)

Ejecutar la aplicación:

Bash
python -m app.main
Abrir en el navegador:
Visita: http://127.0.0.1:5000

🧪 Ejecutar Pruebas (Testing)
El proyecto incluye pruebas automatizadas para asegurar la calidad del código y el correcto funcionamiento de la API.

Para correr los tests:

Bash
pytest
📂 Estructura del Proyecto
La arquitectura está diseñada para ser fácil de mantener y escalar:

Plaintext
app/
├── models/ # Definición de Datos (Clases POPO)
├── routes/ # Endpoints de la API (Blueprints)
├── services/ # Lógica de Negocio (CRUD y Validaciones)
├── templates/ # Interfaz de Usuario (HTML + Jinja2)
└── main.py # Configuración y arranque de la App
tests/ # Pruebas Unitarias y de Integración
👤 Autor
Desarrollado por Janfred Naranjo.
📧 janfrednb@gmail.com
