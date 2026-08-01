# LAB 3 — Docker Compose: Orquestacion Multi-servicio

Levantaremos un stack completo con Flask, PostgreSQL y Nginx usando un solo archivo `docker-compose.yml`.

## Objetivo

- Entender la estructura de un archivo `docker-compose.yml`.
- Configurar redes segmentadas (frontend/backend).
- Usar healthchecks y `depends_on`.
- Dominar los comandos de Docker Compose.

## Estructura

```
lab3/
├── docker-compose.yml
├── .env.example
├── Dockerfile
├── requirements.txt
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
├── nginx/
│   └── nginx.conf
└── db/
    └── init.sql
```

## Paso 1: Preparar entorno

```bash
cd laboratorios/sesion-final/labs-finales/lab3
cp .env.example .env
```

## Paso 2: Levantar el stack

```bash
docker compose up -d --build
docker compose ps
```

Abrir http://localhost

## Paso 3: Explorar

```bash
docker compose logs -f
docker compose exec app sh
docker compose exec db psql -U admin -d tareas_db -c 'SELECT * FROM tareas;'
```

## Paso 4: Verificar redes

```bash
docker network ls
docker network inspect lab3_frontend
docker network inspect lab3_backend
```

## Paso 5: Apagar

```bash
docker compose down
docker compose down -v  # tambien borra volumenes
```
