# routes.py
from flask_rest import app

@app.route('/')
def index():
    return 'Hello, World!'
