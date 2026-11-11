import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
APP_ENV = os.environ.get("APP_ENV", "dev")
APP_COLOR = os.environ.get("APP_COLOR", "#1f6feb")


@app.route("/")
def index():
    html = (
        f"^<html^>^<body style='background-color:{APP_COLOR};color:white;'^>"
        f"^<h1^>Legeni Webapp^</h1^>"
        f"^<p^>Version {APP_VERSION} - Env: {APP_ENV}^</p^>"
        f"^</body^>^</html^>"
    )
    return html, 200


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/ready")
def ready():
    return jsonify(ready=True, env=APP_ENV), 200


@app.route("/api/info")
def info():
    return jsonify(
        app="legeni-webapp",
        version=APP_VERSION,
        environment=APP_ENV,
        color=APP_COLOR,
        status="ok",
    ), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
