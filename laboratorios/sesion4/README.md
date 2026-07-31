# Laboratorio Sesion 4: Datos Persistentes Y Redes Internas

## Objetivo

Mejorar el stack Flask + PostgreSQL para que la base de datos sea interna, use volumen persistente, tenga healthcheck y pueda respaldarse.

## Archivos

Codigo base: [`../../codigo/sesion4`](../../codigo/sesion4/)

```text
codigo/sesion4/
  app.py
  requirements.txt
  Dockerfile
  docker-compose.yml
  .env.example
  .dockerignore
```

## Preparar Variables

```bash
cd codigo/sesion4
cp .env.example .env
```

En Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

## Levantar El Stack

```bash
docker compose up -d --build
docker compose ps
```

Probar la app:

```bash
curl http://localhost:5000
curl http://localhost:5000/add
curl http://localhost:5000
```

## Revisar Red Interna

```bash
docker network ls
docker network inspect sesion4_backend
docker compose exec web sh
```

Dentro del contenedor `web`, el hostname `db` resuelve a PostgreSQL.

## Verificar Persistencia

```bash
# Agregar datos
curl http://localhost:5000/add

# Detener sin borrar volumenes
docker compose down

# Volver a levantar
docker compose up -d

# Los datos siguen ahi
curl http://localhost:5000
```

## Backup de PostgreSQL

```bash
docker compose exec -T db pg_dump -U appuser appdb > backup.sql
```
