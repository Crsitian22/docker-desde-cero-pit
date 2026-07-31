from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('POSTGRES_DB', 'appdb'),
        user=os.environ.get('POSTGRES_USER', 'appuser'),
        password=os.environ.get('POSTGRES_PASSWORD', 'apppass')
    )

@app.route('/')
def index():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({"status": "ok", "db_version": version, "message": "Sesion 4 - Persistencia activa"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/add')
def add():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS visitas (id SERIAL PRIMARY KEY, ts TIMESTAMP DEFAULT NOW());")
        cur.execute("INSERT INTO visitas DEFAULT VALUES;")
        cur.execute("SELECT count(*) FROM visitas;")
        count = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "ok", "total_visitas": count})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
