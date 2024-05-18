from flask import Flask, render_template

from src.routes.health import router as health_router
from src.routes.upload import router as upload_router

app = Flask(__name__)

app.register_blueprint(health_router)
app.register_blueprint(upload_router)

@app.route('/')
def index():
    return render_template('index.html')
