# Codigo Sesion 1

App Flask minima para contenedores.

```bash
docker build -t mi-flask:v1 .
docker run -d --name flask-app -p 5000:5000 mi-flask:v1
```

Probar en http://localhost:5000
