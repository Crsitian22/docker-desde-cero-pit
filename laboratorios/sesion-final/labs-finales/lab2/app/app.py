from flask import Flask, jsonify, request, render_template
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'tareas_db'),
        user=os.environ.get('DB_USER', 'admin'),
        password=os.environ.get('DB_PASS', 'SuperSecreta123!')
    )

@app.route('/')
def index():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM tareas ORDER BY id;")
        tareas = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('index.html', tareas=tareas)
    except Exception as e:
        return render_template('index.html', tareas=[], error=str(e))

@app.route('/health')
def health():
    try:
        conn = get_db()
        conn.close()
        return jsonify({"status": "healthy"}), 200
    except:
        return jsonify({"status": "unhealthy"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
