from flask import Flask, render_template, jsonify
import platform
import os
import socket
import datetime

app = Flask(__name__)
start_time = datetime.datetime.now()

@app.route('/')
def index():
    uptime = str(datetime.datetime.now() - start_time).split('.')[0]
    return render_template(
        'index.html',
        container_id=socket.gethostname(),
        os_name=f"{platform.system()} {platform.release()}",
        python_version=platform.python_version(),
        platform_arch=platform.machine(),
        uptime=uptime
    )

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "container_hostname": socket.gethostname(),
        "institution": "Universidad Nacional de Ingeniería (UNI)",
        "program": "PIT VIRTUAL",
        "course": "Docker desde 0 - 11va Edición",
        "session": "Sesión 2 - Creación, Optimización y Publicación de Imágenes",
        "python_version": platform.python_version()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
