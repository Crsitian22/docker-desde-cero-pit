from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Aplicación Optimizada con Multi-Stage Build ⚡</h1><p>Sesión 2: Dockerfile Profesional en Alpine Linux</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
