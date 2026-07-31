from flask import Flask
import platform, os

app = Flask(__name__)

@app.route('/')
def index():
    info = f"Python {platform.python_version()}"
    return f"<h1>App Optimizada - Sesion 2</h1><p>{info}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
