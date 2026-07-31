from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('POSTGRES_DB', 'posgrado_db'),
        user=os.environ.get('POSTGRES_USER', 'admin_user'),
        password=os.environ.get('POSTGRES_PASSWORD', 'secreto_super_seguro')
    )
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({
            "status": "success",
            "message": "¡Conexión exitosa a PostgreSQL desde Flask con Docker Compose!",
            "database_version": db_version
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
