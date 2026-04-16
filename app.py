import os

from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["APP_NAME"] = os.getenv("APP_NAME", "DevOps Somativa 1")
    app.config["APP_VERSION"] = os.getenv("APP_VERSION", "1.0.0")

    @app.get("/")
    def home():
        return jsonify(
            {
                "message": "Aplicacao Python em execucao com CI/CD e Docker.",
                "status": "ok",
                "project": app.config["APP_NAME"],
                "version": app.config["APP_VERSION"],
            }
        )

    @app.get("/health")
    def health():
        return jsonify({"status": "healthy"}), 200

    @app.get("/about")
    def about():
        return jsonify(
            {
                "stack": "Flask",
                "delivery": "GitHub Actions",
                "container": "Docker",
            }
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
