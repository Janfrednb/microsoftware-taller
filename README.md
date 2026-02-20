# 🏍️ MicroTaller - Gestión de Servicios

Sistema de administración para talleres mecánicos desarrollado con **Python** y **Flask**. Esta herramienta permite gestionar el flujo de trabajo diario de un taller de motocicletas con una interfaz limpia, moderna y eficiente.

---

## ✨ Características Principales

* **📊 Dashboard Dinámico:** Visualización rápida de métricas clave (Citas del día y Alistamientos activos).
* **📅 Agenda de Citas:** Sistema completo para agendar y cancelar citas con clientes.
* **🔧 Gestión de Alistamientos:** Control de ingresos de motocicletas para mantenimiento preventivo y correctivo.
* **🎨 Diseño Minimal UI:** Interfaz inspirada en estándares modernos, utilizando **Bootstrap 5** y tipografía **Public Sans**.
* **🏗️ Arquitectura Limpia:** Código organizado por capas (Rutas, Servicios y Modelos).

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** [Flask](https://flask.palletsprojects.com/) (Python)
* **Frontend:** HTML5, CSS3, Jinja2
* **Estilos:** [Bootstrap 5](https://getbootstrap.com/)
* **Iconos:** [Bootstrap Icons](https://icons.getbootstrap.com/)

---

## 🚀 Instalación y Configuración

Para correr este proyecto localmente, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/microsoftware-taller.git](https://github.com/tu-usuario/microsoftware-taller.git)

2. Crear y activar el entorno virtual:
# En bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate

3. Instalar dependencias:
    pip install flask

4. Ejecutar aplicación:
    python -m app.main

5. Abrir el navegador:
    http://127.0.0.1:5000

Estructura del proyecto:

app/
├── models/      # Definición de clases (Cita, Moto)
├── routes/      # Controladores y rutas de la API
├── services/    # Lógica de negocio y manejo de datos
├── templates/   # Vistas HTML (Jinja2)
└── main.py      # Punto de entrada de la aplicación

