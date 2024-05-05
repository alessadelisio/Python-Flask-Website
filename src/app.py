from flask import Flask

from .routes.health import router as health_router

app = Flask(__name__)

app.register_blueprint(health_router)
