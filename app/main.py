import os
from flask import Flask, render_template

from app.routes.citas import citas_bp
from app.routes.alistamientos import alistamientos_bp
from app.services.alistamientos_service import obtener_alistamientos
from app.services.citas_service import obtener_citas


def create_app():
    app = Flask(__name__)

    # Registro de Blueprints
    app.register_blueprint(citas_bp)
    app.register_blueprint(alistamientos_bp)

    # Vistas HTML
    @app.route("/")
    def home():
        lista_motos = obtener_alistamientos()
        lista_citas = obtener_citas()
        conteo_motos = len(lista_motos)
        conteo_citas = len(lista_citas)
        return render_template(
            "dashboard.html", motos_count=conteo_motos, citas_count=conteo_citas
        )

    @app.route("/alistamientos-view")
    def alistamientos_view():
        return render_template("alistamientos.html")

    @app.route("/citas-view")
    def citas_view():
        return render_template("citas.html")

    return app


# Esta es la línea clave para Render/Gunicorn
app = create_app()

# Este bloque solo se ejecuta cuando corres el código localmente
if __name__ == "__main__":
    # Cambiamos a debug=True solo para tus pruebas locales
    app.run(debug=True)
