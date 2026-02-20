import os
from flask import Flask, render_template
# Importamos los Blueprints
from app.routes.citas import citas_bp
from app.routes.alistamientos import alistamientos_bp
# Importamos los servicios para el conteo
from app.services.alistamientos_service import obtener_alistamientos
from app.services.citas_service import obtener_citas

def create_app():
    app = Flask(__name__)

    # Registro de Blueprints
    app.register_blueprint(citas_bp)
    app.register_blueprint(alistamientos_bp)

    # --- VISTAS HTML ---

    @app.route("/")
    def home():
        # 1. Obtenemos las listas actuales
        lista_motos = obtener_alistamientos()
        lista_citas = obtener_citas()

        # 2. Contamos los elementos
        conteo_motos = len(lista_motos)
        conteo_citas = len(lista_citas)

        # 3. Renderizamos pasando las variables
        return render_template("dashboard.html", 
                               motos_count=conteo_motos, 
                               citas_count=conteo_citas)

    @app.route("/alistamientos-view")
    def alistamientos_view():
        return render_template("alistamientos.html")

    @app.route("/citas-view")
    def citas_view():
        return render_template("citas.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)