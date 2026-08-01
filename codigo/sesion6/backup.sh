#!/bin/bash
# Script de backup automatizado para PostgreSQL
# Uso: ./backup.sh

set -euo pipefail

CONTAINER="tareas-db"
DB_USER="${POSTGRES_USER:-admin}"
DB_NAME="${POSTGRES_DB:-tareas_db}"
BACKUP_DIR="./backups"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/backup-${TIMESTAMP}.dump"

mkdir -p "${BACKUP_DIR}"

echo "Creando backup de ${DB_NAME}..."
docker exec ${CONTAINER} pg_dump -U ${DB_USER} -d ${DB_NAME} -F c > "${BACKUP_FILE}"

echo "Backup creado: ${BACKUP_FILE}"
echo "Tamano: $(du -h "${BACKUP_FILE}" | cut -f1)"

# Limpiar backups antiguos (mantener ultimos 5)
ls -t ${BACKUP_DIR}/backup-*.dump 2>/dev/null | tail -n +6 | xargs -r rm
echo "Limpieza completada."
