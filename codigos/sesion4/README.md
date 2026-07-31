# Laboratorio Sesión 4: Persistencia, Healthchecks y Backups SQL

```bash
# Backup de base de datos
docker compose exec -T db pg_dump -U admin_user posgrado_db > respaldo_backup.sql

# Restauración
docker compose exec -T db psql -U admin_user -d posgrado_db < respaldo_backup.sql
```
