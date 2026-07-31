# LAB 4 — Produccion: Healthchecks, Backups y Seguridad

El laboratorio final integra todos los conceptos del curso y aplica practicas de produccion real.

## Objetivo

- Implementar y verificar healthchecks completos.
- Automatizar backups de PostgreSQL.
- Aplicar limites de recursos (CPU y memoria).
- Endurecer la seguridad de los contenedores.
- Configurar logging drivers y rotacion de logs.

## Estructura

```
lab4/
├── docker-compose.prod.yml
├── backup.sh
├── .env.example
├── Dockerfile
├── requirements.txt
├── app/
├── nginx/
└── db/
```

## Paso 1: Preparar y levantar

```bash
cd laboratorios/sesion-final/labs-finales/lab4
cp .env.example .env
docker compose -f docker-compose.prod.yml up -d --build
```

## Paso 2: Verificar healthchecks

```bash
docker compose -f docker-compose.prod.yml ps
docker inspect tareas-db --format '{{.State.Health.Status}}'
docker inspect tareas-app --format '{{.State.Health.Status}}'
```

## Paso 3: Backup manual

```bash
chmod +x backup.sh
./backup.sh
ls -lh backups/
```

## Paso 4: Restaurar desde backup

```bash
docker exec tareas-db createdb -U admin tareas_db_restored
docker cp backups/backup-XXXXXXXX.dump tareas-db:/tmp/restore.dump
docker exec tareas-db pg_restore -U admin -d tareas_db_restored -F c /tmp/restore.dump
```

## Paso 5: Verificar seguridad

```bash
docker inspect tareas-app --format '{{.HostConfig.ReadonlyRootfs}}'
docker inspect tareas-app --format '{{.HostConfig.SecurityOpt}}'
docker stats --no-stream
```

## Paso 6: Logs

```bash
docker compose -f docker-compose.prod.yml logs -f --tail 50
docker inspect tareas-app --format '{{.HostConfig.LogConfig}}'
```
