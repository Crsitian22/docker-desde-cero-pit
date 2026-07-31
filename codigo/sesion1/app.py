from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return "<h1>Hola Docker desde el PIT 2026 - UNI</h1><p>Mi primera app contenerizada con exito.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
