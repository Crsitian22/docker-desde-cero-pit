# Sesion 2: Dockerfile, Imagenes y Docker Hub

## Objetivo

Crear imagenes propias desde una app Flask, entender cada instruccion del Dockerfile, comprender el sistema de capas y cache, optimizar builds con `.dockerignore`, comparar imagenes base, versionar con tags y publicar en Docker Hub.

## Flujo principal

```text
Dockerfile  ->  imagen  ->  contenedor
receta      ->  molde   ->  proceso ejecutandose
```

## 1. Versionamiento de imagenes

Versionar una imagen significa darle un nombre y un tag:

```text
mi-flask:v1
mi-flask:v2
mi-flask:prod
mi-flask:2026-01
```

### Ejemplo: app Flask versionada

```bash
mkdir flask-versionado
cd flask-versionado
```

Archivos base en [`../../codigo/sesion2/`](../../codigo/sesion2/):

```bash
docker build -t mi-flask:v1 .
docker run -d --name flask-v1 -p 5000:5000 mi-flask:v1
curl http://localhost:5000
docker stop flask-v1
docker rm flask-v1
```

## 2. Instrucciones del Dockerfile

| Instruccion | Para que sirve |
|---|---|
| `FROM` | Define la imagen base |
| `WORKDIR` | Define el directorio de trabajo dentro de la imagen |
| `COPY` | Copia archivos desde la maquina local a la imagen |
| `RUN` | Ejecuta comandos durante la construccion de la imagen |
| `EXPOSE` | Documenta que puerto usa la aplicacion |
| `CMD` | Comando por defecto cuando arranca el contenedor |

### FROM

```text
FROM ubuntu       -> tengo Linux base
FROM python       -> tengo Linux + Python
FROM node         -> tengo Linux + Node.js
```

### WORKDIR

Sin `WORKDIR`:
```dockerfile
COPY app.py /app/app.py
CMD ["python", "/app/app.py"]
```

Con `WORKDIR`:
```dockerfile
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

### COPY

```dockerfile
COPY requirements.txt .
```

El punto final significa la carpeta actual dentro de la imagen (`/app` porque antes pusimos `WORKDIR /app`).

### RUN

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

```text
RUN se ejecuta cuando construyo la imagen.
CMD se ejecuta cuando arranco el contenedor.
```

`--no-cache-dir` evita guardar cache innecesario de pip y reduce el tamano de la imagen.

### EXPOSE

```dockerfile
EXPOSE 5000
```

`EXPOSE` documenta el puerto pero no lo publica. Para publicar usamos `-p`:

```bash
docker run -p 5000:5000 mi-flask:v1
```

```text
5000 de mi maquina -> 5000 del contenedor
```

### CMD

Forma recomendada (exec form):
```dockerfile
CMD ["python", "app.py"]
```

Evitar para produccion (shell form):
```dockerfile
CMD python app.py
```

La forma con lista maneja mejor senales del sistema y argumentos.

## 3. Capas y cache

Una imagen Docker es una pila de capas:

```text
Imagen mi-flask:v1
+------------------------------------+
| COPY app.py .                      | capa 5
+------------------------------------+
| RUN pip install ...                | capa 4
+------------------------------------+
| COPY requirements.txt .            | capa 3
+------------------------------------+
| WORKDIR /app                       | capa 2
+------------------------------------+
| FROM python:3.12-slim              | capa 1
+------------------------------------+
```

Si cambio `app.py`, Docker reconstruye desde la capa 5 y reutiliza las demas.

## 4. .dockerignore

```text
__pycache__/
*.pyc
.git/
.env
venv/
```

Reduce el contexto de build y evita enviar archivos innecesarios al daemon.

## 5. Comparar imagenes base

```bash
docker build -t flask:normal -f Dockerfile .
docker build -t flask:slim -f Dockerfile.slim .
docker build -t flask:alpine -f Dockerfile.alpine .
docker build -t flask:multi -f Dockerfile.multistage .
docker images | grep flask
```

| Imagen base | Tamano aproximado |
|---|---|
| `python:3.12` | ~900 MB |
| `python:3.12-slim` | ~150 MB |
| `python:3.12-alpine` | ~50 MB |
| Multi-stage con alpine | ~40 MB |

## 6. Docker Hub

```bash
docker login
docker tag mi-flask:v1 tu_usuario/mi-flask:v1
docker push tu_usuario/mi-flask:v1
```
