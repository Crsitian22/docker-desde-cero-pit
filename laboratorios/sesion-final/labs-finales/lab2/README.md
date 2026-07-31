# LAB 2 — Dockerfile y Construccion de Imagenes Custom

En este laboratorio construiremos nuestra propia imagen Docker usando Dockerfile.

## Objetivo

- Entender las instrucciones del Dockerfile.
- Construir imagenes con `docker build` y optimizar el cache.
- Crear una imagen multi-stage para reducir tamano.
- Escribir un `.dockerignore`.

## Estructura

```
lab2/
├── Dockerfile
├── Dockerfile.multistage
├── .dockerignore
├── requirements.txt
└── app/
    ├── app.py
    └── templates/
        └── index.html
```

## Paso 1: Construir imagen

```bash
cd laboratorios/sesion-final/labs-finales/lab2
docker build -t gestor-tareas:v1 .
docker images | grep gestor
```

## Paso 2: Multi-stage build

```bash
docker build -t gestor-tareas:multi -f Dockerfile.multistage .
docker images | grep gestor
```

## Paso 3: Comparar tamanos

```bash
docker images | grep gestor
```
