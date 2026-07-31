# Sesion 3: Docker Compose Y Aplicaciones Multi-Contenedor

## Objetivo

Levantar proyectos con varios servicios, entender `docker-compose.yml`, integrar Flask con PostgreSQL y configurar variables con `.env`.

## Por que Compose

Una aplicacion real no vive sola: puede necesitar base de datos, proxy, cache o workers. Ejecutar todo con `docker run` se vuelve repetitivo. Compose permite describir el stack completo en YAML.

```mermaid
flowchart LR
    A["compose.yml"] --> B["docker compose"] --> C["web + db + red + volumen"]
    style A fill:#1f6feb,stroke:#58a6ff,color:#fff
    style B fill:#8957e5,stroke:#bc8cff,color:#fff
    style C fill:#238636,stroke:#3fb950,color:#fff
```

## Estructura base

```yaml
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: apppass
```

## Comandos esenciales

| Comando | Descripcion |
|---|---|
| `docker compose up -d` | Levantar en segundo plano |
| `docker compose up -d --build` | Levantar reconstruyendo imagenes |
| `docker compose ps` | Ver servicios activos |
| `docker compose logs -f` | Ver logs en vivo |
| `docker compose down` | Detener y eliminar contenedores |
| `docker compose down -v` | Detener y eliminar contenedores + volumenes |
| `docker compose exec web sh` | Entrar al contenedor web |

## Variables con .env

```bash
cp .env.example .env
```

En `compose.yml`:
```yaml
environment:
  POSTGRES_DB: ${POSTGRES_DB}
  POSTGRES_USER: ${POSTGRES_USER}
  POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
```

Docker Compose lee automaticamente el archivo `.env` del mismo directorio.

## DNS interno

Dentro de la red de Compose, los servicios se encuentran por nombre:
- La app se conecta a PostgreSQL usando `db` como hostname
- No es necesario usar `localhost` ni IP

```python
conn = psycopg2.connect(host="db", database="appdb")
```

## Ciclo de trabajo

1. Escribir `compose.yml`
2. Crear `.env` con variables
3. `docker compose up -d --build`
4. Probar la app
5. `docker compose down` cuando termines
