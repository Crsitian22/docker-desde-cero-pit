# Laboratorio Sesion 3: Flask + PostgreSQL Con Docker Compose

## Objetivo

Levantar una aplicacion Flask y una base de datos PostgreSQL con un solo archivo `docker-compose.yml`.

## Archivos

Codigo base: [`../../codigo/sesion3`](../../codigo/sesion3/)

```text
codigo/sesion3/
  app.py
  requirements.txt
  Dockerfile
  docker-compose.yml
  .env.example
```

## Preparar Variables

```bash
cd codigo/sesion3
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
docker compose logs -f
```

Probar en http://localhost:5000

## Explorar El Stack

```bash
docker compose exec web sh
docker compose exec db psql -U appuser -d appdb
```

## Apagar

```bash
docker compose down
```
