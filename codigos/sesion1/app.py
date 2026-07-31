from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hola():
    return "<h1>¡Hola Docker desde el PIT 2026 - UNI! 🚀</h1><p>Primera aplicación contenerizada con éxito (Sesión 1).</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
