# Sesion 6: Proyecto Final Y Despliegue Completo

## Objetivo

Integrar todos los conceptos del curso en un proyecto completo: entornos separados para desarrollo y produccion, limpieza de recursos, debugging, script de despliegue automatizado y backup de datos.

## 1. Multi-Entorno

### Desarrollo

```bash
docker compose -f compose.yml -f compose.dev.yml up -d --build
```

Caracteristicas:
- Bind mount para hot-reload del codigo
- Puerto de PostgreSQL expuesto para debugging
- `FLASK_ENV=development`

### Produccion

```bash
docker compose -f compose.yml -f compose.prod.yml up -d --build
```

Caracteristicas:
- Imagen multi-stage optimizada
- Nginx como reverse proxy
- `restart: always` para recuperacion automatica
- Sin puertos internos expuestos

## 2. Script de Despliegue

```bash
#!/bin/bash
ENTORNO=${1:-dev}

echo "Desplegando en entorno: $ENTORNO"

if [ "$ENTORNO" == "prod" ]; then
    docker compose -f compose.yml -f compose.prod.yml up -d --build
    echo "Aplicacion desplegada en PRODUCCION en http://localhost"
else
    docker compose -f compose.yml -f compose.dev.yml up -d --build
    echo "Aplicacion desplegada en DESARROLLO en http://localhost:5000"
fi
```

## 3. Limpieza de Recursos

```bash
# Ver espacio usado
docker system df

# Limpiar todo lo no usado
docker system prune -a --volumes

# Limpiar solo imagenes sin tag
docker image prune

# Limpiar solo contenedores detenidos
docker container prune
```

## 4. Protocolo de Debugging

| Problema | Comando |
|---|---|
| Contenedor no arranca | `docker compose logs web` |
| Error de conexion a DB | `docker compose exec web sh` -> `ping db` |
| Puerto ocupado | `docker ps` para ver conflictos |
| Imagen no se actualiza | `docker compose up -d --build --force-recreate` |
| Datos corruptos | `docker compose down -v` y restaurar backup |

## 5. Checklist de Produccion

- [ ] Healthchecks configurados para todos los servicios
- [ ] Volumenes nombrados para datos persistentes
- [ ] `.env` fuera del repositorio (en `.gitignore`)
- [ ] Nginx como reverse proxy
- [ ] Restart policies configuradas
- [ ] Backups automatizados
- [ ] Imagenes con tags especificos (no `latest`)
- [ ] Usuario no-root en contenedores
