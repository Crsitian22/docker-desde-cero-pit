# Laboratorio Sesion 2: Dockerfile, Imagenes y Docker Hub

## Objetivo

Construir una imagen profesional de una app Flask usando Dockerfile, `.dockerignore`, tags, revision de capas y publicacion en Docker Hub.

## Archivos

Codigo base: [`../../codigo/sesion2`](../../codigo/sesion2/)

```text
codigo/sesion2/
  app.py
  requirements.txt
  Dockerfile
  Dockerfile.multistage
  Dockerfile.slim
  Dockerfile.alpine
  .dockerignore
```

## Paso 1: Construir imagen versionada

```bash
cd codigo/sesion2
docker build -t mi-flask:v1 .
docker run -d --name flask-v1 -p 5000:5000 mi-flask:v1
curl http://localhost:5000
docker stop flask-v1
docker rm flask-v1
```

## Paso 2: Revisar capas

```bash
docker history mi-flask:v1
```

## Paso 3: Demostrar cache

```bash
# Segunda construccion (mas rapida)
docker build -t mi-flask:v1 .

# Cambiar app.py y reconstruir
docker build -t mi-flask:v2 .
```

## Paso 4: Capa escribible

```bash
docker run -it --name prueba-escritura mi-flask:v1 sh
echo "archivo temporal" > /app/test.txt
exit
docker rm prueba-escritura
```

## Paso 5: Comparar imagenes base

```bash
docker build -t flask:slim -f Dockerfile.slim .
docker build -t flask:alpine -f Dockerfile.alpine .
docker build -t flask:multi -f Dockerfile.multistage .
docker images | grep flask
```

## Paso 6: Publicar en Docker Hub

```bash
docker login
docker tag mi-flask:v1 TU_USUARIO/mi-flask:v1
docker push TU_USUARIO/mi-flask:v1
```
