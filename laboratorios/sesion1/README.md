# Laboratorio Sesion 1: Contenedores Desde Cero

## Objetivo

Validar la instalacion de Docker, ejecutar contenedores de prueba, construir una imagen propia desde una app Flask y ejecutarla publicando el puerto 5000.

## Archivos

Codigo base: [`../../codigo/sesion1`](../../codigo/sesion1/)

```text
codigo/sesion1/
  app.py
  requirements.txt
  Dockerfile
```

## Paso 1: Validar Docker

```bash
docker --version
docker info
docker run hello-world
```

## Paso 2: Ejecutar Nginx de prueba

```bash
docker run --name web-demo -d -p 8080:80 nginx
docker ps
```

Abrir `http://localhost:8080`

## Paso 3: Detener y limpiar Nginx

```bash
docker stop web-demo
docker ps -a
docker rm web-demo
docker images
```

## Paso 4: Construir imagen Flask

```bash
cd codigo/sesion1
docker build -t mi-flask:v1 .
docker images
```

## Paso 5: Ejecutar la app

```bash
docker run -d --name flask-app -p 5000:5000 mi-flask:v1
curl http://localhost:5000
```

## Paso 6: Limpieza

```bash
docker stop flask-app
docker rm flask-app
```
