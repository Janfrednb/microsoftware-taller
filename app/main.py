import os
from flask import Flask, render_template

# Importo los 'Blueprints' (mis archivos de rutas separados) para conectarlos aquí.
from app.routes.citas import citas_bp
from app.routes.alistamientos import alistamientos_bp

# Importo las funciones de mis servicios para obtener datos y mostrarlos en el inicio.
from app.services.alistamientos_service import obtener_alistamientos
from app.services.citas_service import obtener_citas


# Defino una función para crear la aplicación.
# Esto es una buena práctica (Application Factory) para mantener el código ordenado.
def create_app():
    # Inicializo la aplicación Flask. __name__ le dice a Flask dónde buscar los recursos.
    app = Flask(__name__)

    # --- REGISTRO DE BLUEPRINTS ---
    # Aquí es donde "enchufo" las rutas que creé en los otros archivos.
    # Si no hago esto, la app principal no sabrá que existen las rutas de citas o alistamientos.
    app.register_blueprint(citas_bp)
    app.register_blueprint(alistamientos_bp)

    # --- VISTAS HTML (FRONTEND) ---
    # A diferencia de los Blueprints que devuelven datos JSON, estas rutas sirven para
    # mostrar las páginas web reales al usuario.

    @app.route("/")
    def home():
        # 1. Llamo a mis servicios para traer las listas de datos actuales.
        lista_motos = obtener_alistamientos()
        lista_citas = obtener_citas()

        # 2. Uso len() para contar cuántos registros tengo en cada lista.
        conteo_motos = len(lista_motos)
        conteo_citas = len(lista_citas)

        # 3. Renderizo la plantilla 'dashboard.html'.
        # Le paso las variables 'motos_count' y 'citas_count' para que el HTML pueda mostrar los números.
        return render_template(
            "dashboard.html", motos_count=conteo_motos, citas_count=conteo_citas
        )

    @app.route("/alistamientos-view")
    def alistamientos_view():
        # Esta ruta simplemente carga el archivo HTML donde gestionaré los alistamientos.
        return render_template("alistamientos.html")

    @app.route("/citas-view")
    def citas_view():
        # Esta ruta carga el archivo HTML para gestionar las citas.
        return render_template("citas.html")

    return app


# Este bloque verifica si estoy ejecutando este archivo directamente.
if __name__ == "__main__":
    app = create_app()
    # Arranco el servidor. 'debug=True' es muy útil porque me muestra los errores en pantalla
    # y reinicia el servidor automáticamente cuando guardo cambios.
    app.run(debug=True)
