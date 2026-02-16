from flask import Flask
from app.routes.citas import citas_bp
from app.routes.alistamientos import alistamientos_bp  # 👈 nuevo import

def create_app():
    app = Flask(__name__)

    app.register_blueprint(citas_bp)
    app.register_blueprint(alistamientos_bp)

    @app.route("/")
    def home():
        return {"message": "Microsoftware Taller API running"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
