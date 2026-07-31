# Laboratorio Sesión 1: Primera Aplicación Web en Flask

## Archivos del laboratorio:
- `app.py`: Servidor web Flask.
- `requirements.txt`: Dependencias Python.
- `Dockerfile`: Instrucciones de compilación.

## Instrucciones de ejecución:
```bash
# 1. Construir la imagen
docker build -t mi-flask:v1 .

# 2. Ejecutar el contenedor en segundo plano
docker run --name flask-app -d -p 5000:5000 mi-flask:v1

# 3. Probar en el navegador
# Open http://localhost:5000

# 4. Limpieza
docker stop flask-app
docker rm flask-app
```
