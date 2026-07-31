# Laboratorio Sesión 2: Multi-Stage Build y Optimización de Imágenes

## Instrucciones de ejecución:
```bash
# 1. Construir versión estándar
docker build -t flask-app:normal -f Dockerfile .

# 2. Construir versión optimizada multistage
docker build -t flask-app:optimizada -f Dockerfile.multistage .

# 3. Comparar pesos
docker images | grep flask-app

# 4. Publicar en Docker Hub (Reemplazar tu_usuario)
# docker login
# docker tag flask-app:optimizada tu_usuario/mi-flask:v1.0
# docker push tu_usuario/mi-flask:v1.0
```
