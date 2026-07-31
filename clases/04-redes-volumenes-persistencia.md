# Sesion 4: Redes, Volumenes Y Persistencia

## Objetivo

Entender como los servicios se comunican dentro de Docker, como persistir datos y como proteger componentes internos como PostgreSQL.

## 1. Redes Docker

Cuando usas Docker Compose, cada proyecto recibe una red interna por defecto. Dentro de esa red, los contenedores se encuentran usando el nombre del servicio.

Ejemplo mental:

- `web` no se conecta a `localhost` para llegar a PostgreSQL.
- `web` se conecta al host `db`, porque `db` es el nombre del servicio en Compose.
- Solo publicamos puertos cuando necesitamos acceder desde el host o navegador.

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
```

En este caso, `web` esta publicado hacia el host, pero `db` puede permanecer interno.

## 2. Puerto Publicado Vs Comunicacion Interna

| Caso | Direccion correcta |
|---|---|
| Navegador hacia la app | `localhost:5000` |
| App hacia PostgreSQL | `db:5432` |
| Otro servicio interno hacia la app | `web:5000` |

Regla practica: si el usuario no necesita entrar directamente, no publiques el puerto.

## 3. Redes Explicitas

La red por defecto suele bastar para proyectos pequenos. Una red explicita ayuda cuando quieres documentar mejor la arquitectura o separar trafico.

```yaml
services:
  web:
    networks:
      - backend

  db:
    networks:
      - backend

networks:
  backend:
```

## 4. Volumenes

Un contenedor es reemplazable. Los datos importantes no deben depender del filesystem del contenedor.

### Tipos de volumenes

| Tipo | Uso | Ejemplo |
|---|---|---|
| **Volumen nombrado** | Datos que Docker gestiona | `datos_postgres:/var/lib/postgresql/data` |
| **Bind mount** | Montar carpeta del host | `./app:/app` (desarrollo) |
| **tmpfs** | Datos temporales en memoria | Solo Linux |

### Volumen nombrado en Compose

```yaml
services:
  db:
    image: postgres:16
    volumes:
      - datos_postgres:/var/lib/postgresql/data

volumes:
  datos_postgres:
```

Con esto, si haces `docker compose down`, los datos persisten. Solo se borran con `docker compose down -v`.

## 5. Healthchecks

Un healthcheck le dice a Docker como verificar si el servicio esta listo.

```yaml
db:
  image: postgres:16
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
    interval: 5s
    timeout: 5s
    retries: 5
```

```yaml
web:
  depends_on:
    db:
      condition: service_healthy
```

## 6. Backup de PostgreSQL

```bash
# Crear backup
docker compose exec -T db pg_dump -U admin appdb > backup.sql

# Restaurar backup
docker compose exec -T db psql -U admin -d appdb < backup.sql
```

## Resumen

| Concepto | Comando / Practica |
|---|---|
| Red interna | Los servicios se llaman por nombre |
| No publicar DB | Quitar `ports` de PostgreSQL |
| Volumen nombrado | Persistir datos entre reinicios |
| Healthcheck | Verificar que el servicio esta listo |
| Backup | `pg_dump` + `docker exec` |
